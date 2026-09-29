// AulaViva · Edge Function unificada (pi1) — Supabase
// Rotas: ?disc=pi1&a=get|put|reg|login|logout|check|lista|arq|arqup|entrega|minhas|entregas
// Variáveis: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, PROF_TOKEN
const DISC = "pi1";
const URL_SB = Deno.env.get("SUPABASE_URL")!;
const KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const PROF_TOKEN = Deno.env.get("PROF_TOKEN") || "TROQUE_ESTE_TOKEN_2026";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS" };
const json = (d: unknown, st = 200) =>
  new Response(JSON.stringify(d), { status: st, headers: { ...cors, "Content-Type": "application/json" } });
const fail = (msg: string, code = "erro", st = 400) => json({ ok: false, erro: code, msg }, st);

async function sb(table: string) {
  return { from: table };
}
async function q(path: string, init?: RequestInit) {
  const r = await fetch(`${URL_SB}/rest/v1/${path}`, {
    ...init,
    headers: { apikey: KEY, Authorization: `Bearer ${KEY}`,
      "Content-Type": "application/json", Prefer: "return=representation",
      ...(init?.headers || {}) },
  });
  return r;
}
function norm(s: string) {
  return s.trim().toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .replace(/\s+/g, " ");
}
async function sha(salt: string, senha: string) {
  const b = new TextEncoder().encode(salt + "|" + senha);
  const h = await crypto.subtle.digest("SHA-256", b);
  return [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, "0")).join("");
}
function randHex(n = 8) {
  const a = new Uint8Array(n); crypto.getRandomValues(a);
  return [...a].map(x => x.toString(16).padStart(2, "0")).join("");
}
function novoCode() {
  let s = ""; for (let i = 0; i < 12; i++) s += String.fromCharCode(65 + Math.floor(Math.random() * 26));
  return s;
}
function getCookie(req: Request) {
  const c = req.headers.get("Cookie") || "";
  const m = c.match(new RegExp("aulaviva_" + DISC + "=([A-Za-z0-9]+)"));
  return m ? m[1] : "";
}
function setCookieHeaders(code: string | null) {
  const base = `aulaviva_${DISC}=${code || ""}; Path=/; Max-Age=${code ? 60 * 60 * 24 * 120 : 0}; HttpOnly; SameSite=Lax`;
  return { "Set-Cookie": base };
}
async function b64ToBytes(b64: string) { return Uint8Array.from(atob(b64), c => c.charCodeAt(0)); }

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: cors });
  const u = new URL(req.url);
  const a = u.searchParams.get("a") || "get";
  const code = getCookie(req);
  try {
    if (a === "get") {
      if (!code) return json({ ok: true, nome: null });
      const pc = await q(`aulaviva_progresso?disc=eq.${DISC}&code=eq.${code}&select=payload`);
      const pr = await pc.json();
      const cc = await q(`aulaviva_contas?disc=eq.${DISC}&code=eq.${code}&select=nome,turma`);
      const cr = await cc.json();
      if (!cr.length) return json({ ok: true, nome: null });
      return json({ ok: true, nome: cr[0].nome, turma: cr[0].turma,
        payload: pr.length ? pr[0].payload : null });
    }
    if (a === "put") {
      if (!code) return fail("sem sessão", "sem_sessao", 401);
      const d = await req.json();
      const payload = d.payload || {};
      await q("aulaviva_progresso", { method: "POST",
        body: JSON.stringify([{ disc: DISC, code, nome: d.nome || "", turma: d.turma || "",
          payload }]),
        headers: { Prefer: "resolution=merge-duplicates,return=minimal" } });
      return json({ ok: true, code }, 200);
    }
    if (a === "reg") {
      const d = await req.json();
      const nome = String(d.nome || "").trim();
      if (nome.length < 3) return fail("nome muito curto", "nome");
      if (String(d.senha || "").length < 4) return fail("senha muito curta", "senha");
      const nl = norm(nome);
      const ex = await q(`aulaviva_contas?disc=eq.${DISC}&nome_lc=eq.${encodeURIComponent(nl)}&select=code`);
      if ((await ex.json()).length) return fail("nome já cadastrado", "nome", 409);
      const novo = novoCode(); const salt = randHex();
      const hash = await sha(salt, d.senha);
      const ins = await q("aulaviva_contas", { method: "POST",
        body: JSON.stringify([{ disc: DISC, code: novo, nome, nome_lc: nl,
          turma: d.turma || "", salt, senha_hash: hash,
          adm: /juh/i.test(nome) ? 1 : 0 }]) });
      if (!ins.ok) { console.error(await ins.text()); return fail("falha ao criar conta", "interno", 500); }
      return new Response(JSON.stringify({ ok: true, nome, payload: null }),
        { headers: { ...cors, "Content-Type": "application/json", ...setCookieHeaders(novo) } });
    }
    if (a === "login") {
      const d = await req.json();
      const nl = norm(String(d.nome || ""));
      const r = await q(`aulaviva_contas?disc=eq.${DISC}&nome_lc=eq.${encodeURIComponent(nl)}&select=code,nome,turma,salt,senha_hash`);
      const cs = await r.json();
      if (!cs.length) return fail("credenciais inválidas", "cred", 401);
      const c = cs[0];
      const h = await sha(c.salt, String(d.senha || ""));
      if (h !== c.senha_hash) return fail("credenciais inválidas", "cred", 401);
      const pc = await q(`aulaviva_progresso?disc=eq.${DISC}&code=eq.${c.code}&select=payload`);
      const pr = await pc.json();
      return new Response(JSON.stringify({ ok: true, nome: c.nome, turma: c.turma,
        payload: pr.length ? pr[0].payload : null }),
        { headers: { ...cors, "Content-Type": "application/json", ...setCookieHeaders(c.code) } });
    }
    if (a === "logout") {
      return new Response(JSON.stringify({ ok: true }),
        { headers: { ...cors, "Content-Type": "application/json", ...setCookieHeaders(null) } });
    }
    if (a === "check") {
      const nl = norm(u.searchParams.get("nome") || "");
      const r = await q(`aulaviva_contas?disc=eq.${DISC}&nome_lc=eq.${encodeURIComponent(nl)}&select=code`);
      return json({ ok: true, existe: (await r.json()).length > 0 });
    }
    if (a === "lista") {
      if (u.searchParams.get("token") !== PROF_TOKEN) return fail("token inválido", "token", 403);
      const cs = await (await q(`aulaviva_contas?disc=eq.${DISC}&select=code,nome,turma&order=nome`)).json();
      const ps = await (await q(`aulaviva_progresso?disc=eq.${DISC}&select=code,payload,updated_at`)).json();
      const by = new Map(ps.map((p: any) => [p.code, p]));
      return json(cs.map((c: any) => {
        const p = by.get(c.code) || { payload: {} };
        const pl = p.payload || {};
        return { nome: c.nome, turma: c.turma, pts: pl.pts || 0,
          aulas: (pl.aulas && Object.values(pl.aulas).flat().length) || 0,
          exercicios: (pl.exok && Object.values(pl.exok).flat().length) || 0,
          chefes: pl.boss ? Object.keys(pl.boss).length : 0,
          pos: pl.pos || null, hist: pl.hist || [], atualizado: p.updated_at || "" };
      }));
    }
    if (a === "arq") {
      // Privacidade: material exclusivo da professora (nome contém "professor"/
      // "painel") só é listado para ADM — mesma regra do botão 👩‍ Painel no app.
      let adm = false;
      if (code) {
        const cr = await (await q(`aulaviva_contas?disc=eq.${DISC}&code=eq.${code}&select=nome,adm`)).json();
        adm = cr.length > 0 && (cr[0].adm === 1 || /juh/i.test(String(cr[0].nome || "")));
      }
      const r = await (await q(`aulaviva_arquivos?disc=eq.${DISC}&select=nome,tipo,tamanho,updated_at&order=updated_at.desc`)).json();
      return json(r.filter((x: any) => adm || !/professor|painel/i.test(String(x.nome || "")))
        .map((x: any) => ({ ...x,
          url: `${URL_SB}/storage/v1/object/public/materiais/${DISC}/${encodeURIComponent(x.nome)}` })));
    }
    if (a === "arqup") {
      if (u.searchParams.get("token") !== PROF_TOKEN) return fail("token inválido", "token", 403);
      const d = await req.json();
      const nome = String(d.nome || "arquivo.pdf").replace(/[^\w.\- ]+/g, "");
      const bytes = await b64ToBytes(String(d.base64 || ""));
      if (bytes.length < 2 || bytes.length > 15 * 1024 * 1024) return fail("arquivo inválido ou > 15 MB");
      const up = await fetch(`${URL_SB}/storage/v1/object/materiais/${DISC}/${encodeURIComponent(nome)}`, {
        method: "POST", headers: { Authorization: `Bearer ${KEY}`, apikey: KEY,
          "Content-Type": d.tipo || "application/octet-stream", "x-upsert": "true" }, body: bytes });
      if (!up.ok) { console.error(await up.text()); return fail("falha no storage", "interno", 500); }
      await q("aulaviva_arquivos", { method: "POST",
        body: JSON.stringify([{ disc: DISC, nome, tipo: d.tipo || "", tamanho: bytes.length }]),
        headers: { Prefer: "resolution=merge-duplicates,return=minimal" } });
      return json({ ok: true, nome });
    }
    if (a === "entrega") {
      if (!code) return fail("sem sessão", "sem_sessao", 401);
      const d = await req.json();
      const nome = String(d.nome || "atividade.pdf").replace(/[^\w.\- ]+/g, "");
      const ext = (nome.split(".").pop() || "").toLowerCase();
      if (!["txt", "doc", "docx", "pdf", "odt"].includes(ext)) return fail("formato não permitido");
      const bytes = await b64ToBytes(String(d.base64 || ""));
      if (bytes.length < 2 || bytes.length > 12 * 1024 * 1024) return fail("arquivo inválido ou > 12 MB");
      const cc = await (await q(`aulaviva_contas?disc=eq.${DISC}&code=eq.${code}&select=nome`)).json();
      const aluno = norm(cc.length ? cc[0].nome : "aluno").replace(/[^a-z0-9]+/g, "_");
      const ts = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
      const caminho = `${DISC}/${code}/${ts}_${aluno}_${nome}`;
      const up = await fetch(`${URL_SB}/storage/v1/object/entregas/${caminho.split("/").map(encodeURIComponent).join("/")}`, {
        method: "POST", headers: { Authorization: `Bearer ${KEY}`, apikey: KEY,
          "Content-Type": d.tipo || "application/octet-stream" }, body: bytes });
      if (!up.ok) { console.error(await up.text()); return fail("falha no storage", "interno", 500); }
      await q("aulaviva_entregas", { method: "POST",
        body: JSON.stringify([{ disc: DISC, code, aluno, nome, caminho, tamanho: bytes.length }]),
        headers: { Prefer: "return=minimal" } });
      return json({ ok: true, arquivo: caminho });
    }
    if (a === "minhas") {
      if (!code) return fail("sem sessão", "sem_sessao", 401);
      const r = await (await q(`aulaviva_entregas?disc=eq.${DISC}&code=eq.${code}&select=nome,tamanho,created_at&order=created_at.desc`)).json();
      return json(r.map((x: any) => ({ ...x, atualizado: x.created_at })));
    }
    if (a === "entregas") {
      if (u.searchParams.get("token") !== PROF_TOKEN) return fail("token inválido", "token", 403);
      const r = await (await q(`aulaviva_entregas?disc=eq.${DISC}&select=id,aluno,nome,tamanho,created_at,caminho,code&order=created_at.desc&limit=400`)).json();
      const cs = await (await q(`aulaviva_contas?disc=eq.${DISC}&select=code,nome`)).json();
      const nm = new Map(cs.map((c: any) => [c.code, c.nome]));
      const tok = encodeURIComponent(u.searchParams.get("token") || "");
      return json(r.map((x: any) => ({ ...x, aluno: nm.get(x.code) || x.aluno,
        url: `${u.origin}${u.pathname}?disc=${DISC}&a=dlent&id=${x.id}&token=${tok}` })));
    }
    if (a === "dlent") {
      if (u.searchParams.get("token") !== PROF_TOKEN) return fail("token inválido", "token", 403);
      const id = u.searchParams.get("id") || "";
      const r = await (await q(`aulaviva_entregas?disc=eq.${DISC}&id=eq.${id}&select=caminho,nome`)).json();
      if (!r.length) return fail("entrega não encontrada", "nf", 404);
      const obj = await fetch(`${URL_SB}/storage/v1/object/entregas/${r[0].caminho.split("/").map(encodeURIComponent).join("/")}`,
        { headers: { Authorization: `Bearer ${KEY}`, apikey: KEY } });
      if (!obj.ok) return fail("objeto indisponível", "nf", 404);
      const bytes = await obj.arrayBuffer();
      return new Response(bytes, { headers: { ...cors, "Content-Type": "application/octet-stream",
        "Content-Disposition": `attachment; filename="${r[0].nome}"` } });
    }
    return fail("rota desconhecida", "rota", 404);
  } catch (e) {
    console.error("edge " + DISC + "/" + a + ":", e);
    return fail("erro interno", "interno", 500);
  }
});
