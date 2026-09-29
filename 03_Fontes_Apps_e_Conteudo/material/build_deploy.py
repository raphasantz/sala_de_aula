# -*- coding: utf-8 -*-
"""Gera os projetos Vercel + Supabase dos dois AulaViva (PI-I e LP2), separadamente.
Cada projeto: index.html (app com sync na nuvem), prof.html (painel), api/sync.js,
supabase/schema.sql, README.md. API zero-dependências (PostgREST via fetch)."""
import io
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
OUT = os.path.join(_ROOT, "deploy")

NUVEM = r"""
<script>
/* ========== Sincronização em nuvem (Vercel + Supabase) ========== */
(function(){
  var DISC = "__DISC__";
  var API  = "/api/sync";
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

SYNC_JS = r"""// API de progresso do AulaViva — Vercel Serverless + Supabase (PostgREST)
// Env: SUPABASE_URL, SUPABASE_SERVICE_KEY, PROF_TOKEN
// GET  /api/sync?aluno=CODE          -> save do aluno
// PUT  /api/sync?aluno=CODE  {nome,turma,payload} -> upsert do save
// GET  /api/sync?lista=1&token=...   -> lista da turma (painel do professor)
const DISC = "__DISC__";
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
"""

SCHEMA_SQL = """-- AulaViva Cloud — tabela de progresso (usada pelos dois projetos: pi1 e lp2)
-- Execute UMA vez no SQL Editor do seu projeto Supabase.
create table if not exists public.progresso (
  id         bigint generated always as identity primary key,
  disc       text not null,               -- 'pi1' | 'lp2'
  code       text not null,               -- código anônimo do aparelho/aluno
  nome       text default '',
  turma      text default '',
  payload    jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now(),
  unique (disc, code)
);

alter table public.progresso enable row level security;
-- Sem políticas públicas: somente a API (service key) lê/grava.
-- O painel do professor usa a mesma API com PROF_TOKEN.

comment on table public.progresso is
  'Progresso do AulaViva por aluno (code) e disciplina (disc).';

-- Índice para o painel da turma (ordena por atualização)
create index if not exists idx_progresso_disc_at
  on public.progresso (disc, updated_at desc);
"""

PROF_HTML = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel do Professor — AulaViva __LABEL__</title>
<style>
 body{font-family:"Segoe UI",system-ui,sans-serif;background:#f4f7fb;color:#1f2937;margin:0}
 header{background:#0d2b4e;color:#fff;padding:14px 20px;display:flex;gap:12px;align-items:center}
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
    <p style="margin:0 0 10px"><b>Token do professor</b> (o mesmo definido em PROF_TOKEN no Vercel):</p>
    <input id="tok" type="password" placeholder="cole o PROF_TOKEN">
    <button onclick="carregar()">Ver turma</button>
    <button class="gh" onclick="csv()">Exportar CSV</button>
    <p class="nota">Mostra nome, turma, pontos, módulos concluídos e última sincronização de cada
    aluno que jogou com a nuvem ativada. Atualize a página (ou clique de novo) para recarregar.</p>
  </div>
  <div class="card" style="margin-top:14px" id="resultado"></div>
</div>
<script>
let LINHAS = [];
function api(){ return "/api/sync"; }
async function carregar(){
  const tok = document.getElementById("tok").value.trim();
  const r = await fetch(api() + "?lista=1&token=" + encodeURIComponent(tok));
  const el = document.getElementById("resultado");
  if (!r.ok){ el.innerHTML = "<p class='nota'>Falha: " + r.status + " (token errado?)</p>"; return; }
  LINHAS = await r.json();
  if (!LINHAS.length){ el.innerHTML = "<p class='nota'>Nenhum aluno sincronizado ainda.</p>"; return; }
  let h = "<table><tr><th>#</th><th>Aluno</th><th>Turma</th><th>Pontos</th>"
        + "<th>Módulos concluídos</th><th>Aulas/concluídas</th><th>Última sync</th></tr>";
  LINHAS.forEach((x, i) => {
    const p = x.payload || {};
    const mods = Object.keys(p.done || {}).length;
    const aulas = Object.keys(p.aulas || {}).length;
    const dt = x.updated_at ? new Date(x.updated_at).toLocaleString("pt-BR") : "";
    h += "<tr><td>" + (i+1) + "</td><td><b>" + (x.nome || "(sem nome)") + "</b></td><td>"
      + (x.turma || "-") + "</td><td class='ok'>" + (p.pts || 0) + "</td><td>" + mods
      + "</td><td>" + aulas + "</td><td>" + dt + "</td></tr>";
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

README = """# AulaViva __LABEL__ na nuvem (Vercel + Supabase)

Projeto serverless que salva o progresso dos alunos do AulaViva __LABEL__ no Supabase.
Funciona **online e offline**: sem internet, o app continua salvando no aparelho
(localStorage) e sincroniza quando a conexão volta.

## 1) Criar o banco (Supabase) — uma única vez
1. Crie um projeto em https://supabase.com (grátis).
2. Abra **SQL Editor** e execute o conteúdo de `supabase/schema.sql`.
3. Em **Settings → API**, copie:
   - `Project URL`  → variável `SUPABASE_URL`
   - `service_role key` (SEGREDO!) → variável `SUPABASE_SERVICE_KEY`

## 2) Publicar no Vercel
1. Suba esta pasta como um projeto no Vercel (drag-and-drop em https://vercel.com/new
   ou `vercel deploy` pela CLI).
2. Em **Project → Settings → Environment Variables**, crie:
   - `SUPABASE_URL` = URL do projeto Supabase
   - `SUPABASE_SERVICE_KEY` = service role key
   - `PROF_TOKEN` = uma senha sua para o painel do professor (ex.: gere uma frase longa)
3. Deploy. Ao abrir:
   - `/` → app do aluno (com o selo ☁️ no topo: salvo / offline / sincronizado);
   - `/prof.html` → painel da turma (pede o PROF_TOKEN, mostra tabela e exporta CSV).

## 3) Como o aluno usa
- Abre o link do Vercel no celular/PC → digita o nome (cadastro) → joga.
- O progresso sobe sozinho (≈1 s após cada salvamento) e volta em qualquer aparelho:
  no aparelho novo, com o local vazio, o app baixa o save da nuvem automaticamente.
- O código anônimo do aparelho fica no localStorage (`aulaviva_code___DISC__`).

## 4) API (referência)
| Método | Rota | Uso |
|---|---|---|
| GET  | `/api/sync?aluno=CODE` | baixa o save do aluno |
| PUT  | `/api/sync?aluno=CODE` (corpo JSON) | salva/atualiza (upsert) |
| GET  | `/api/sync?lista=1&token=PROF_TOKEN` | lista da turma (painel) |

## 5) Segurança (resumo)
- RLS do Supabase **fechado**: só a `service_role` (usada pela API) acessa a tabela.
- A service key fica **somente** nas env vars do Vercel (nunca no HTML).
- O painel exige `PROF_TOKEN`; os dados dos alunos são anônimos (code + nome opcional).

## 6) Os dois projetos
Este repositório/projeto atende apenas a disciplina __LABEL__ (`disc = '__DISC__'`).
O projeto irmão da outra disciplina usa a MESMA tabela (coluna `disc` separa os saves)
— execute o schema.sql uma única vez no Supabase compartilhado.
"""


def build(disc, label, src_html):
    dst = os.path.join(OUT, "aulaviva-" + disc)
    os.makedirs(os.path.join(dst, "api"), exist_ok=True)
    os.makedirs(os.path.join(dst, "supabase"), exist_ok=True)
    html = io.open(src_html, encoding="utf-8").read()
    assert "</body>" in html
    html = html.replace("</body>", NUVEM.replace("__DISC__", disc), 1)
    io.open(os.path.join(dst, "index.html"), "w", encoding="utf-8").write(html)
    io.open(os.path.join(dst, "api", "sync.js"), "w", encoding="utf-8").write(
        SYNC_JS.replace("__DISC__", disc))
    io.open(os.path.join(dst, "prof.html"), "w", encoding="utf-8").write(
        PROF_HTML.replace("__LABEL__", label))
    io.open(os.path.join(dst, "supabase", "schema.sql"), "w", encoding="utf-8").write(SCHEMA_SQL)
    io.open(os.path.join(dst, "README.md"), "w", encoding="utf-8").write(
        README.replace("__LABEL__", label).replace("__DISC__", disc))
    print("projeto gerado:", dst)


if __name__ == "__main__":
    build("pi1", "Programação para Internet I",
          os.path.join(_ROOT, "output", "AulaViva_Programacao_para_Internet_I.html"))
    build("lp2", "Linguagem de Programação II",
          os.path.join(_ROOT, "output", "AulaViva_Linguagem_de_Programacao_II.html"))
    print("deploy pronto em deploy/")
