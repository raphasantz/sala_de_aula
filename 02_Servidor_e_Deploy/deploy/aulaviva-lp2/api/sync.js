// API de progresso do AulaViva — Vercel Serverless + Supabase (PostgREST)
// Env: SUPABASE_URL, SUPABASE_SERVICE_KEY, PROF_TOKEN
// GET  /api/sync?aluno=CODE          -> save do aluno
// PUT  /api/sync?aluno=CODE  {nome,turma,payload} -> upsert do save
// GET  /api/sync?lista=1&token=...   -> lista da turma (painel do professor)
const DISC = "lp2";
const TABELA = "progresso";

function cfg(){
  const URL = process.env.SUPABASE_URL || "";
  const KEY = process.env.SUPABASE_SERVICE_KEY || "";
  return { URL: URL.replace(/\/$/, ""), KEY };
}
function headers(KEY){
  return { apikey: KEY, Authorization: "Bearer " + KEY, "Content-Type": "application/json" };
}

module.exports = async function handler(req, res){
  const { URL, KEY } = cfg();
  if (!URL || !KEY){ res.status(500).json({ erro: "Supabase não configurado (env)" }); return; }
  const base = URL + "/rest/v1/" + TABELA;
  const q = req.query || {};
  try{
    if (req.method === "GET"){
      if (q.lista === "1"){
        const PROF = process.env.PROF_TOKEN || "";
        if (!PROF || q.token !== PROF){ res.status(403).json({ erro: "token inválido" }); return; }
        const r = await fetch(base + "?disc=eq." + DISC + "&order=updated_at.desc",
                              { headers: headers(KEY) });
        if (!r.ok){ res.status(500).json({ erro: await r.text() }); return; }
        const rows = await r.json();
        res.status(200).json((rows || []).map(x => ({
          nome: x.nome, turma: x.turma, updated_at: x.updated_at, payload: x.payload })));
        return;
      }
      const code = q.aluno;
      if (!code){ res.status(400).json({ erro: "parâmetro aluno obrigatório" }); return; }
      const r = await fetch(base + "?disc=eq." + DISC + "&code=eq." + encodeURIComponent(code)
                            + "&limit=1", { headers: headers(KEY) });
      if (!r.ok){ res.status(500).json({ erro: await r.text() }); return; }
      const rows = await r.json();
      res.status(200).json(rows && rows.length ? rows[0] : {});
      return;
    }
    if (req.method === "PUT" || req.method === "POST"){
      const code = q.aluno;
      if (!code){ res.status(400).json({ erro: "parâmetro aluno obrigatório" }); return; }
      const body = typeof req.body === "string" ? JSON.parse(req.body) : (req.body || {});
      const row = {
        disc: DISC, code: code,
        nome: body.nome || "", turma: body.turma || "",
        payload: body.payload || {},
        updated_at: new Date().toISOString(),
      };
      const r = await fetch(base + "?on_conflict=disc,code", {
        method: "POST",
        headers: Object.assign(headers(KEY),
          { Prefer: "resolution=merge-duplicates,return=minimal" }),
        body: JSON.stringify(row),
      });
      if (!r.ok){ res.status(500).json({ erro: await r.text() }); return; }
      res.status(200).json({ ok: true });
      return;
    }
    res.status(405).json({ erro: "método não suportado" });
  }catch(e){
    res.status(500).json({ erro: String(e && e.message || e) });
  }
}
