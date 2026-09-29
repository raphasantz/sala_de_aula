# -*- coding: utf-8 -*-
"""Gera o kit SEM VERCEL: AulaViva + Supabase Edge Function (sync).
Cada disciplina: index.html, prof.html, edge-sync.ts (colar no Supabase), README.md."""
import io
import os
import zipfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
OUT = os.path.join(_ROOT, "deploy-supabase")

REF = "fzpipqrgnjupyfugztjo"  # projeto Supabase da professora

NUVEM = r"""
<script>
/* ========== Sync direto com Supabase Edge Function (sem Vercel) ========== */
(function(){
  var DISC = "__DISC__";
  var API  = "__API__";
  function lsGet(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
  function lsSet(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }
  var code = lsGet("aulaviva_code_" + DISC);
  if (!code){
    code = (window.crypto && crypto.randomUUID) ? crypto.randomUUID()
           : String(Date.now()) + "-" + Math.floor(Math.random()*1e9);
    lsSet("aulaviva_code_" + DISC, code);
  }
  var elNuvem = null;
  function status(t){ if (!elNuvem) elNuvem = document.getElementById("nuvem");
    if (elNuvem) elNuvem.textContent = t; }
  function pill(){ var d = document.querySelector("header .dir");
    if (d && !document.getElementById("nuvem")){
      var s = document.createElement("span"); s.id = "nuvem"; s.className = "pill ghost";
      s.textContent = "☁️ …"; d.prepend(s); elNuvem = s; } }
  pill(); setTimeout(pill, 600); setTimeout(pill, 1500);

  var pend = false, timer = null;
  function enviar(){
    timer = null; if (!pend) return; pend = false;
    try{
      fetch(API + "?disc=" + DISC + "&aluno=" + encodeURIComponent(code), {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome: S.nome || "", turma: S.turma || "", payload: {
          mi: S.mi, pts: S.pts, seq: S.seq, exok: S.exok, done: S.done, boss: S.boss,
          pos: S.pos, aulas: S.aulas, scored: S.scored, nome: S.nome, turma: S.turma } })
      }).then(function(r){ status(r.ok ? "☁️ salvo" : "☁️ offline"); })
        .catch(function(){ status("☁️ offline"); });
    }catch(e){ status("☁️ offline"); }
  }
  function marcar(){ pend = true; if (!timer) timer = setTimeout(enviar, 1200); }

  var ARQ = API.replace(/sync(-lp2)?/, "arquivos");
  function pillArq(){
    var d = document.querySelector("header .dir");
    if (d && !document.getElementById("btArq")){
      var b = document.createElement("button");
      b.className = "pill"; b.id = "btArq"; b.textContent = "📎 Materiais";
      b.onclick = abrirMateriais; d.prepend(b);
    }
  }
  pillArq(); setTimeout(pillArq, 600); setTimeout(pillArq, 1500);
  function abrirMateriais(){
    S.flow = null; setHud();
    app.innerHTML = '<div class="cardp"><h2>📎 Materiais da turma</h2>' +
      '<p style="margin:6px 0 12px">Documentos enviados pela professora: apostilas, listas, ' +
      'slides, provas antigas. Clique para baixar ou abrir.</p>' +
      '<div id="listaArq"><p class="nota">carregando…</p></div>' +
      '<div class="nav"><button class="btn gh" onclick="irHome()">← Voltar à trilha</button></div></div>';
    fetch(ARQ + "?disc=" + DISC + "&lista=1")
      .then(function(r){ return r.ok ? r.json() : []; })
      .then(function(xs){
        var el = document.getElementById("listaArq");
        if (!xs || !xs.length){ el.innerHTML = "<p class='nota'>Nenhum material enviado ainda. " +
          "Peça para a professora enviar pelo Painel do Professor. 🙂</p>"; return; }
        el.innerHTML = xs.map(function(x){
          var kb = x.tamanho ? Math.max(1, Math.round(x.tamanho/1024)) + " KB" : "";
          var dt = (x.atualizado || "").slice(0, 10);
          return '<div style="display:flex;justify-content:space-between;gap:10px;align-items:center;' +
            'background:#f4f8fc;border:1px solid #dfe8f2;border-radius:10px;padding:10px 12px;margin:8px 0">' +
            '<a href="' + x.url + '" target="_blank" download style="color:#1b5faa;font-weight:700;' +
            'text-decoration:none">⬇ ' + x.nome + '</a>' +
            '<span style="font-size:12px;color:#5b6b7c">' + kb + ' · ' + dt + '</span></div>';
        }).join("");
      })
      .catch(function(){ document.getElementById("listaArq").innerHTML =
        "<p class='nota'>Offline no momento — tente novamente com internet.</p>"; });
  }

  var _save0 = window.save;
  window.save = function(){ var r = _save0.apply(this, arguments); marcar(); return r; };

  fetch(API + "?disc=" + DISC + "&aluno=" + encodeURIComponent(code))
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(j){
      if (j && j.payload && typeof j.payload.pts === "number"){
        var localVazio = !(S.nome) && !(S.pts > 0)
          && !Object.keys(S.done || {}).length && !Object.keys(S.aulas || {}).length;
        if (localVazio){
          Object.assign(S, j.payload); S.flow = null;
          _save0.call(this);
          if (typeof updateNomeBtn === "function") updateNomeBtn();
          if (typeof renderHome === "function") renderHome();
          status("☁️ sincronizado");
        } else { status("☁️ ok"); marcar(); }
      } else { status("☁️ conectado"); marcar(); }
    })
    .catch(function(){ status("☁️ offline"); });
})();
</script>
</body>"""

EDGE_TS = r"""// AulaViva — sync (zero dependências) — __LABEL__
// Supabase → Edge Functions → New function → Name: __FNAME__ → cole isto → Verify JWT OFF → Deploy
const DISC = "__DISC__";
const PROF_TOKEN = "__PROFTOKEN__"; // <- senha do painel do professor

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
"""


STORAGE_SQL = """-- Bucket público de materiais da turma (execute 1x no SQL Editor)
insert into storage.buckets (id, name, public)
values ('materiais', 'materiais', true)
on conflict (id) do nothing;

-- leitura pública (alunos baixam sem login):
drop policy if exists materiais_leitura_publica on storage.objects;
create policy materiais_leitura_publica
  on storage.objects for select
  using (bucket_id = 'materiais');

-- uploads/exclusões: SOMENTE pela Edge Function 'arquivos' (service role).
-- Nenhuma policy de insert para anon => ninguém mais consegue enviar.
"""

EDGE_ARQ = r"""// AulaViva — arquivos (materiais da turma) — Supabase Storage
// Deploy como function nome: arquivos   (UMA vez, serve as duas disciplinas)
const PROF_TOKEN = "__PROFTOKEN__"; // <- mesmo token do sync
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
"""

PROF_HTML = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel do Professor — AulaViva __LABEL__</title>
<style>
 body{font-family:"Segoe UI",system-ui,sans-serif;background:#f4f7fb;color:#1f2937;margin:0}
 header{background:#0d2b4e;color:#fff;padding:14px 20px}
 header h1{font-size:19px;margin:0}
 .wrap{max-width:1000px;margin:0 auto;padding:18px}
 .card{background:#fff;border-radius:14px;padding:18px;box-shadow:0 3px 14px rgba(13,43,78,.09)}
 input,button{border-radius:10px;padding:11px 14px;font-size:15px;font-family:inherit}
 input{border:2px solid #d9d4ee;width:320px;max-width:70vw}
 button{border:none;background:#f59e0b;color:#3a2700;font-weight:800;cursor:pointer}
 button.gh{background:#e3ecf7;color:#0d2b4e}
 table{width:100%;border-collapse:collapse;margin-top:14px;font-size:14.5px}
 th{background:#0d2b4e;color:#fff;padding:9px 10px;text-align:left}
 td{border:1px solid #c9d8e8;padding:8px 10px}
 tr:nth-child(even) td{background:#f4f8fc}
 .nota{font-size:12.5px;color:#5b6b7c;margin-top:8px;line-height:1.5}
 .ok{color:#1e7b34;font-weight:700}
</style>
</head>
<body>
<header><h1>👩‍🏫 Painel do Professor — AulaViva __LABEL__</h1></header>
<div class="wrap">
  <div class="card">
    <p style="margin:0 0 10px"><b>Token do professor</b> (o PROF_TOKEN que você definiu no código da Edge Function):</p>
    <input id="tok" type="password" placeholder="cole o PROF_TOKEN">
    <button onclick="carregar()">Ver turma</button>
    <button class="gh" onclick="csv()">Exportar CSV</button>
    <p class="nota">Nome, turma, pontos, módulos concluídos e última sincronização de cada aluno.</p>
  </div>
  <div class="card" style="margin-top:14px" id="resultado"></div>
  <div class="card" style="margin-top:14px">
    <p style="margin:0 0 10px"><b>📎 Enviar material para a turma</b>
       <span class="nota">(apostilas, listas, slides — os alunos baixam pelo botão 📎 do AulaViva)</span></p>
    <input type="file" id="farq" style="width:auto;max-width:70vw">
    <button onclick="enviarArq()">Enviar</button>
    <div id="stArq" class="nota"></div>
    <div id="listaProf" style="margin-top:10px"></div>
  </div>
<script>
const ARQ = API.replace(/sync(-lp2)?/, "arquivos");
async function enviarArq(){
  const tok = document.getElementById("tok").value.trim();
  const f = document.getElementById("farq").files[0];
  const st = document.getElementById("stArq");
  if (!f || !tok){ st.textContent = "Escolha o arquivo e digite o PROF_TOKEN antes."; return; }
  const b64 = await new Promise(res => { const r = new FileReader();
    r.onload = () => res(r.result.split(",")[1]); r.readAsDataURL(f); });
  st.textContent = "Enviando " + f.name + " …";
  try{
    const r = await fetch(ARQ + "?disc=" + (API.indexOf("lp2") > 0 ? "lp2" : "pi1"), {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token: tok, nome: f.name, base64: b64, tipo: f.type }) });
    st.textContent = r.ok ? "✔ Disponível para a turma!" : "Falha no envio: HTTP " + r.status;
    listarProf();
  }catch(e){ st.textContent = "Erro de rede: " + e; }
}
async function listarProf(){
  const tok = document.getElementById("tok").value.trim();
  if (!tok) return;
  const r = await fetch(ARQ + "?disc=" + (API.indexOf("lp2") > 0 ? "lp2" : "pi1") +
                        "&lista=1&token=" + encodeURIComponent(tok));
  if (!r.ok) return;
  const xs = await r.json();
  document.getElementById("listaProf").innerHTML = xs.length
    ? "<b>Disponíveis agora:</b> " + xs.map(x => x.nome).join(" · ")
    : "<span class='nota'>Nenhum material enviado ainda.</span>";
}
</script>
</div>
<script>
let LINHAS = [];
const API = "__API__";
async function carregar(){
  const tok = document.getElementById("tok").value.trim();
  const r = await fetch(API + "?lista=1&token=" + encodeURIComponent(tok));
  const el = document.getElementById("resultado");
  if (!r.ok){ el.innerHTML = "<p class='nota'>Falha: " + r.status + " (token errado?)</p>"; return; }
  LINHAS = await r.json();
  if (!LINHAS.length){ el.innerHTML = "<p class='nota'>Nenhum aluno sincronizado ainda.</p>"; return; }
  let h = "<table><tr><th>#</th><th>Aluno</th><th>Turma</th><th>Pontos</th>"
        + "<th>Módulos</th><th>Aulas</th><th>Última sync</th></tr>";
  LINHAS.forEach((x, i) => {
    const p = x.payload || {};
    h += "<tr><td>" + (i+1) + "</td><td><b>" + (x.nome || "(sem nome)") + "</b></td><td>"
      + (x.turma || "-") + "</td><td class='ok'>" + (p.pts || 0) + "</td><td>"
      + Object.keys(p.done || {}).length + "</td><td>" + Object.keys(p.aulas || {}).length
      + "</td><td>" + (x.updated_at ? new Date(x.updated_at).toLocaleString("pt-BR") : "") + "</td></tr>";
  });
  el.innerHTML = h + "</table>";
}
function csv(){
  if (!LINHAS.length){ alert("Carregue a turma primeiro."); return; }
  let s = "nome;turma;pontos;modulos;aulas;ultima_sync\n";
  LINHAS.forEach(x => { const p = x.payload || {};
    s += [x.nome||"", x.turma||"", p.pts||0, Object.keys(p.done||{}).length,
          Object.keys(p.aulas||{}).length, x.updated_at||""].join(";") + "\n"; });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([s], {type:"text/csv"}));
  a.download = "aulaviva_turma.csv"; a.click();
}
</script>
</body>
</html>
"""

README = """# AulaViva __LABEL__ — SOMENTE Supabase (sem Vercel, sem GitHub)

## 1) Criar a atendente (Edge Function) — 3 minutos
1. No painel do Supabase, menu esquerdo: **Edge Functions**;
2. Clique em **New function**;
3. **Name**: `__FNAME__`  (se já existir uma com esse nome, abra-a para editar);
4. Apague todo o código que aparecer no editor e **cole o conteúdo de `edge-sync.ts`**;
5. **Antes do Deploy**: na linha `const PROF_TOKEN = "...`, troque pelo token que você inventar
   (ex.: `prof-raquel-2026`) — ele é a senha do seu painel;
6. Clique em **Deploy** e espere o selo ficar verde.

Pronto: sua API está viva em
`https://__REF__.supabase.co/functions/v1/__FNAME__`

## 2) Usar o app — zero instalação
- **Duplo clique no `index.html`** deste kit (ou envie o arquivo aos alunos pelo
  Classroom/Drive/WhatsApp — funciona até offline);
- O selo ☁️ no topo mostra: conectado / salvo / offline;
- Trocou de aparelho? Com o local vazio, o app baixa o save da nuvem sozinho.

## 3) Painel da turma
- Abra **`prof.html`** (duplo clique), digite o PROF_TOKEN e veja a tabela + CSV.

## 4) Se o selo ficar ☁️ offline
- Confira se a função `sync` está **Deployed** (Edge Functions);
- Confira se o `schema.sql` foi executado no SQL Editor (tabela `progresso`);
- Abra `https://__REF__.supabase.co/functions/v1/__FNAME__?aluno=teste` no navegador:
  deve aparecer `{}`  (chaves vazias) — se aparecer erro, me mande o texto dele.
"""


def vacina(txt):
    """Cinto de seguranca: se o HTML-base ainda for v1 sem o escape rich()
    (hotfix tags HTML), aplica as mesmas substituicoes do hotfix para o kit
    nao nascer 'congelado no tempo' com tags cruas no innerHTML.
    Se a base ja tem rich() (v2), nao mexe em nada."""
    if "function rich" in txt:
        return txt
    RICH = (
        "function rich(s){ s = String(s)"
        ".replace(/&(?!amp;|lt;|gt;|quot;|apos;|nbsp;|#\\d+;|#x[0-9a-fA-F]+;)/g, \"&amp;\")"
        ".replace(/<(?!\\/?(?:b|i|u|br|sub|super|strike)(?:\\s[^>]*)?\\s*\\/?>)/g, \"&lt;\");"
        " return s; }"
        "\n"
    )
    repl = [
        ("function save(){", RICH + "function save(){", 1),
        ('<div class="perg">${q[0]}</div>',
         '<div class="perg">${rich(q[0])}</div>', 1),
        ('</span>${a}</button>', '</span>${rich(a)}</button>', 1),
        ('${q[3]||""}', '${rich(q[3]||"")}', 4),
        ("${q[1][" + "q[2]]}</b>", "${rich(q[1][" + "q[2]])}</b>", 1),
        ("${q[1][certo]}</b>", "${rich(q[1][certo])}</b>", 1),
    ]
    if any(txt.count(old) != n for old, _, n in repl):
        print("AVISO: base v1 com padroes diferentes do hotfix tags HTML; "
              "verificar manualmente antes de gerar o kit.")
        return txt
    for old, new, _ in repl:
        txt = txt.replace(old, new)
    print("base v1 vacinada com rich() automaticamente")
    return txt


def build(disc, label):
    fname = "sync" if disc == "pi1" else "sync-lp2"
    api = f"https://{REF}.supabase.co/functions/v1/{fname}"
    dst = os.path.join(OUT, "aulaviva-" + disc)
    os.makedirs(dst, exist_ok=True)
    html = io.open(os.path.join(_ROOT, "output",
                   "AulaViva_Programacao_para_Internet_I.html" if disc == "pi1"
                   else "AulaViva_Linguagem_de_Programacao_II.html"),
                   encoding="utf-8").read()
    html = vacina(html)
    html = html.replace("</body>",
                        NUVEM.replace("__DISC__", disc).replace("__API__", api), 1)
    io.open(os.path.join(dst, "index.html"), "w", encoding="utf-8").write(html)
    io.open(os.path.join(dst, "prof.html"), "w", encoding="utf-8").write(
        PROF_HTML.replace("__LABEL__", label).replace("__API__", api))
    fname_arq = "arquivos"
    io.open(os.path.join(dst, "arquivos.ts"), "w", encoding="utf-8").write(
        EDGE_ARQ.replace("__PROFTOKEN__", "prof-raquel-2026"))
    io.open(os.path.join(dst, "edge-sync.ts"), "w", encoding="utf-8").write(
        EDGE_TS.replace("__DISC__", disc).replace("__LABEL__", label)
               .replace("__PROFTOKEN__", "prof-raquel-2026"))
    io.open(os.path.join(dst, "storage_materiais.sql"), "w", encoding="utf-8").write(
        STORAGE_SQL)
    io.open(os.path.join(dst, "README.md"), "w", encoding="utf-8").write(
        README.replace("__LABEL__", label).replace("__REF__", REF).replace("__FNAME__", fname))
    print("kit gerado:", dst)


if __name__ == "__main__":
    build("pi1", "Programação para Internet I")
    build("lp2", "Linguagem de Programação II")
    zpath = os.path.join(_ROOT, "output", "AulaViva_Kit_SoSupabase.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for proj in ["aulaviva-pi1", "aulaviva-lp2"]:
            base = os.path.join(OUT, proj)
            for a in os.listdir(base):
                z.write(os.path.join(base, a), os.path.join(proj, a))
    print("ZIP:", zpath, round(os.path.getsize(zpath)/1024, 1), "KB")
