// AulaViva — sync (zero dependências) — Linguagem de Programação II
// Supabase → Edge Functions → New function → Name: __FNAME__ → cole isto → Verify JWT OFF → Deploy
const DISC = "lp2";
const PROF_TOKEN = "prof-raquel-2026"; // <- senha do painel do professor

const BASE = (Deno.env.get("SUPABASE_URL") || "").replace(/\/$/, "") + "/rest/v1/progresso";
const KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, PUT, POST, OPTIONS",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS, "Content-Type": "application/json" },
  });
}

const H = () => ({
  apikey: KEY,
  Authorization: "Bearer " + KEY,
  "Content-Type": "application/json",
});

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const url = new URL(req.url);
  try {
    if (req.method === "GET") {
      if (url.searchParams.get("lista") === "1") {
        if (url.searchParams.get("token") !== PROF_TOKEN) return json({ erro: "token" }, 403);
        const r = await fetch(BASE + "?disc=eq." + DISC + "&order=updated_at.desc", { headers: H() });
        if (!r.ok) return json({ erro: await r.text() }, 500);
        return json(await r.json());
      }
      const code = url.searchParams.get("aluno");
      if (!code) return json({ erro: "aluno" }, 400);
      const r = await fetch(BASE + "?disc=eq." + DISC + "&code=eq." + encodeURIComponent(code) + "&limit=1", { headers: H() });
      if (!r.ok) return json({ erro: await r.text() }, 500);
      const rows = await r.json();
      return json(rows && rows.length ? rows[0] : {});
    }
    if (req.method === "PUT" || req.method === "POST") {
      const code = url.searchParams.get("aluno");
      if (!code) return json({ erro: "aluno" }, 400);
      const body = await req.json();
      const r = await fetch(BASE + "?on_conflict=disc,code", {
        method: "POST",
        headers: { ...H(), Prefer: "resolution=merge-duplicates,return=minimal" },
        body: JSON.stringify({
          disc: DISC,
          code,
          nome: body.nome || "",
          turma: body.turma || "",
          payload: body.payload || {},
          updated_at: new Date().toISOString(),
        }),
      });
      if (!r.ok) return json({ erro: await r.text() }, 500);
      return json({ ok: true });
    }
    return json({ erro: "método" }, 405);
  } catch (e) {
    return json({ erro: String(e) }, 500);
  }
});
