// AulaViva — arquivos (materiais da turma) — Supabase Storage
// Deploy como function nome: arquivos   (UMA vez, serve as duas disciplinas)
const PROF_TOKEN = "prof-raquel-2026"; // <- mesmo token do sync
const URLB = Deno.env.get("SUPABASE_URL") || "";
const KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "";
const BUCKET = "materiais";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};
function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status, headers: { ...CORS, "Content-Type": "application/json" },
  });
}
const H = () => ({ apikey: KEY, Authorization: "Bearer " + KEY });

Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  const url = new URL(req.url);
  const disc = url.searchParams.get("disc") === "lp2" ? "lp2" : "pi1";
  try {
    if (req.method === "GET") {           // lista pública p/ alunos e painel
      const r = await fetch(URLB + "/storage/v1/object/list/" + BUCKET, {
        method: "POST", headers: { ...H(), "Content-Type": "application/json" },
        body: JSON.stringify({ prefix: disc + "/", limit: 300 }),
      });
      if (!r.ok) return json({ erro: await r.text() }, 500);
      const objs = await r.json();
      return json((objs || []).map((o: any) => ({
        nome: String(o.name).replace(/^\d+-/, ""),
        tamanho: o.metadata && o.metadata.size ? o.metadata.size : 0,
        atualizado: o.updated_at,
        url: URLB + "/storage/v1/object/public/" + BUCKET + "/" + disc + "/" + o.name,
      })));
    }
    if (req.method === "POST") {          // upload (somente com PROF_TOKEN)
      const body = await req.json();
      if (body.token !== PROF_TOKEN) return json({ erro: "token" }, 403);
      const nome = String(body.nome || "arquivo").replace(/[^\w.\-() ]+/g, "_");
      const bin = Uint8Array.from(atob(body.base64), (c) => c.charCodeAt(0));
      const caminho = disc + "/" + Date.now() + "-" + nome;
      const r = await fetch(URLB + "/storage/v1/object/" + BUCKET + "/" + caminho, {
        method: "POST",
        headers: { ...H(), "Content-Type": body.tipo || "application/octet-stream",
                   "x-upsert": "true" },
        body: bin,
      });
      if (!r.ok) return json({ erro: await r.text() }, 500);
      return json({ ok: true,
        url: URLB + "/storage/v1/object/public/" + BUCKET + "/" + caminho });
    }
    if (req.method === "DELETE") {        // excluir (somente com PROF_TOKEN)
      const body = await req.json();
      if (body.token !== PROF_TOKEN) return json({ erro: "token" }, 403);
      const r = await fetch(URLB + "/storage/v1/object/" + BUCKET + "/" +
        disc + "/" + encodeURIComponent(body.nome), { method: "DELETE", headers: H() });
      if (!r.ok) return json({ erro: await r.text() }, 500);
      return json({ ok: true });
    }
    return json({ erro: "método" }, 405);
  } catch (e) {
    return json({ erro: String(e) }, 500);
  }
});
