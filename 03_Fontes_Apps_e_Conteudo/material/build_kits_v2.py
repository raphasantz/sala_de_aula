# -*- coding: utf-8 -*-
"""Monta os KITS v2 (nuvem) das duas disciplinas:
  1) Kit_Sala_de_Aula_v2.zip        → Supabase (edge functions unificadas avpi1/avlp2)
  2) Manutencao_Redserver_v2.zip    → servidor da escola (api.php v2)
Apps gerados a partir de material/_base/*.BASE.html (API/DISC injetados).
Inclui painel prof.html v2 (gate: token + nome ADM 'Juh').
Uso: python3 build_kits_v2.py
"""
import os
import re
import shutil
import zipfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
_OUT = os.path.join(_ROOT, "output")
_BASE = os.path.join(_HERE, "_base")

DISCS = {
    "pi1": {"slug": "Programacao_para_Internet_I",
            "titulo": "Programação para Internet I",
            "sb_func": "avpi1"},
    "lp2": {"slug": "Linguagem_de_Programacao_II",
            "titulo": "Linguagem de Programação II",
            "sb_func": "avlp2"},
}
SB_BASE = "https://fzpipqrgnjupyfugztjo.supabase.co"
# FIX: URL RELATIVA — funciona em qualquer domínio (ngrok, raquel.redserver.top,
# localhost) e segue a convenção do repositório (apps-nuvem → ../aulaviva/api.php).
RS_BASE = "../aulaviva/api.php"

# ---------------------------------------------------------------- edge (Deno)
EDGE_AV = r"""// AulaViva · Edge Function unificada (__DISC__) — Supabase
// Rotas: ?disc=__DISC__&a=get|put|reg|login|logout|check|lista|arq|arqup|entrega|minhas|entregas
// Variáveis: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, PROF_TOKEN
const DISC = "__DISC__";
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
"""

# ---------------------------------------------------------------- painel v2
PROF_HTML = r"""<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel da Professora · AulaViva</title>
<style>
 :root{--navy:#0d2b4e;--azul:#1b5faa;--amber:#f59e0b}
 *{box-sizing:border-box;margin:0;padding:0}
 body{font-family:"Segoe UI",system-ui,Arial,sans-serif;background:#f4f7fb;color:#1f2937}
 header{background:var(--navy);color:#fff;padding:12px 18px;display:flex;gap:10px;align-items:center;
   justify-content:space-between;flex-wrap:wrap;position:sticky;top:0}
 header h1{font-size:18px}
 .wrap{max-width:1080px;margin:0 auto;padding:18px 14px 70px}
 .card{background:#fff;border-radius:16px;padding:18px;box-shadow:0 3px 14px rgba(13,43,78,.08);margin-bottom:16px}
 .btn{border:none;border-radius:10px;padding:10px 18px;font-weight:800;cursor:pointer;
   font-family:inherit;background:var(--azul);color:#fff;font-size:14px}
 .btn.amb{background:var(--amber);color:#3a2700}
 .btn.gh{background:#e3ecf7;color:var(--navy)}
 input[type=text],input[type=password]{border:2px solid #d9d4ee;border-radius:10px;padding:10px 12px;
   font-size:15px;font-family:inherit;width:100%;margin:6px 0}
 table{width:100%;border-collapse:collapse;font-size:14px}
 th{background:var(--navy);color:#fff;padding:8px 10px;text-align:left}
 td{border:1px solid #dbe6f2;padding:7px 10px}
 tr:nth-child(even) td{background:#f6fafd}
 tr.click{cursor:pointer} tr.click:hover td{background:#fff7e6}
 .tag{display:inline-block;border-radius:20px;padding:2px 10px;font-size:12px;font-weight:800}
 .tag.ok{background:#e8f7e6;color:#1e7b34}.tag.no{background:#fdecef;color:#c0392b}
 .nota{font-size:13px;color:#5b6b7c;margin-top:8px}
 .err{background:#fbeae8;border-left:5px solid #e21b3c;border-radius:8px;padding:8px 12px;
   font-size:13.5px;color:#8c2418;margin:8px 0;display:none}
 #modal{position:fixed;inset:0;background:rgba(8,20,38,.62);display:none;align-items:center;
   justify-content:center;z-index:20}
 .mbox{background:#fff;border-radius:18px;padding:24px;max-width:640px;width:94%;
   max-height:88vh;overflow:auto;box-shadow:0 12px 44px rgba(0,0,0,.4)}
 .hist td{font-size:12.5px}
 @media(max-width:760px){header h1{font-size:15px}.wrap{padding:12px 10px 60px}
   .card{padding:14px}table{display:block;overflow-x:auto}.btn{padding:9px 13px;font-size:13px}
   .mbox{padding:16px;width:97%}}
</style></head><body>
<header><h1>👩‍ Painel da Professora · AulaViva</h1>
 <a class="btn amb" href="__APP__" style="text-decoration:none">← Voltar ao app</a></header>
<div class="wrap">
 <div class="card" id="gate">
  <h2 style="color:var(--navy)">🔒 Acesso restrito</h2>
  <p class="nota">Painel exclusivo da professora (ADM). Informe seu nome e o token.</p>
  <input type="text" id="gnome" placeholder="Nome (ADM)">
  <input type="password" id="gtok" placeholder="Token do painel">
  <div class="err" id="gerr"></div>
  <button class="btn amb" onclick="entrar()">Entrar 🔓</button>
 </div>
 <div id="painel" style="display:none">
  <div class="card">
   <h2 style="color:var(--navy)">👥 Progresso dos alunos</h2>
   <div style="margin:10px 0;display:flex;gap:8px;flex-wrap:wrap">
    <button class="btn gh" onclick="baixarCSV()">⬇ CSV completo (com respostas)</button>
    <button class="btn gh" onclick="abrirEnvio()">📎 Enviar material à turma</button>
    <button class="btn gh" onclick="verEntregas()">📤 Entregas recebidas</button>
    <button class="btn gh" onclick="carregar()">🔄 Atualizar</button>
   </div>
   <div id="lista"><p class="nota">carregando…</p></div>
   <p class="nota">Clique na linha do aluno para ver TODAS as respostas registradas e as entregas.</p>
  </div>
 </div>
</div>
<div id="modal"><div class="mbox" id="mbox"></div></div>
<script>
const API = "__API__"; const DISC = "__DISC__";
let TOK = ""; let ALUNOS = [];
function api(rota, corpo, extra){
  const q = API + "?disc=" + DISC + "&a=" + rota + (extra || "");
  if (corpo !== undefined)
    return fetch(q,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(corpo)});
  return fetch(q);
}
function entrar(){
  const nome = document.getElementById("gnome").value.trim();
  const tok  = document.getElementById("gtok").value.trim();
  const err  = document.getElementById("gerr");
  err.style.display = "none";
  if (!/juh/i.test(nome)){ err.textContent = "Acesso restrito ao perfil ADM (professora).";
    err.style.display = "block"; return; }
  TOK = tok;
  carregar(true);
}
function carregar(primeira){
  api("lista", undefined, "&token=" + encodeURIComponent(TOK))
   .then(r => { if (!r.ok) throw 0; return r.json(); })
   .then(xs => { ALUNOS = xs; document.getElementById("gate").style.display = "none";
     document.getElementById("painel").style.display = "block"; renderLista(); })
   .catch(() => { const e = document.getElementById("gerr");
     e.textContent = "Token inválido ou servidor offline."; e.style.display = "block"; });
}
function renderLista(){
  if (!ALUNOS.length){ document.getElementById("lista").innerHTML =
    "<p class='nota'>Nenhum aluno ainda.</p>"; return; }
  let h = `<table><tr><th>Aluno</th><th>Turma</th><th>⭐ Pts</th><th>Aulas</th><th>Ex.</th>
    <th>Chefes</th><th>Onde parou</th><th>Respostas</th><th>Atualizado</th></tr>`;
  for (const x of ALUNOS){
    h += `<tr class="click" onclick="detalhe(${ALUNOS.indexOf(x)})"><td><b>${x.nome}</b></td>
     <td>${x.turma || "—"}</td><td>${x.pts}</td><td>${x.aulas}</td><td>${x.exercicios}</td>
     <td>${x.chefes}</td><td>${x.pos ? "Módulo " + x.pos.mi : "início"}</td>
     <td>${(x.hist || []).length}</td><td>${(x.atualizado || "").slice(0,10)}</td></tr>`;
  }
  document.getElementById("lista").innerHTML = h + "</table>";
}
function detalhe(i){
  const x = ALUNOS[i];
  const hist = (x.hist || []);
  let h = `<h3 style="color:var(--navy)">📝 ${x.nome} <span class="nota">(${x.turma || "sem turma"})</span></h3>
   <p class="nota">⭐ ${x.pts} pts · ${x.aulas} aulas · ${x.chefes} chefes ·
   ${hist.length} respostas registradas</p>`;
  if (hist.length){
    h += `<table class="hist"><tr><th>Quando</th><th>Tipo</th><th>Mod</th><th>Aula</th>
      <th>Pergunta</th><th>Escolha</th><th>Resultado</th></tr>`;
    for (const r of hist.slice().reverse().slice(0, 200))
      h += `<tr><td>${r.ts || ""}</td><td>${r.t === "boss" ? "chefe" : "checkpoint"}</td>
        <td>${r.mod}</td><td>${r.aula}</td><td>${(r.perg || "").slice(0,60)}</td>
        <td>${["▲","◆","●","■"][r.esc] || r.esc}</td>
        <td><span class="tag ${r.ok ? "ok" : "no"}">${r.ok ? "acertou" : "errou"}</span></td></tr>`;
    h += "</table>";
  } else h += "<p class='nota'>Sem respostas registradas ainda.</p>";
  h += `<div style="margin-top:12px"><button class="btn gh" onclick="fechar()">Fechar</button></div>`;
  document.getElementById("mbox").innerHTML = h;
  document.getElementById("modal").style.display = "flex";
}
function fechar(){ document.getElementById("modal").style.display = "none"; }
function baixarCSV(){
  const sep = ";";
  let csv = "Aluno" + sep + "Turma" + sep + "Pontos" + sep + "Aulas" + sep + "Exercicios" + sep +
    "Chefes" + sep + "Modulo_atual" + sep + "Respostas_certas" + sep + "Respostas_erradas" + sep +
    "Atualizado" + sep + "Historico" + "\n";
  for (const x of ALUNOS){
    const hist = x.hist || [];
    const det = hist.map(r => `${r.ts}|${r.t === "boss" ? "chefe" : "chk"}|m${r.mod}|${r.aula}|p${r.q}|${r.ok ? "C" : "E"}`).join(" ");
    csv += [x.nome, x.turma || "", x.pts, x.aulas, x.exercicios, x.chefes,
      x.pos ? x.pos.mi : "", hist.filter(r => r.ok).length, hist.filter(r => !r.ok).length,
      x.atualizado || "", '"' + det.replace(/"/g, "''") + '"'].join(sep) + "\n";
  }
  const b = new Blob(["\uFEFF" + csv], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a"); a.href = URL.createObjectURL(b);
  a.download = "aulaviva_" + DISC + "_respostas.csv"; a.click();
}
function abrirEnvio(){
  document.getElementById("mbox").innerHTML = `<h3 style="color:var(--navy)">📎 Enviar material</h3>
   <input type="file" id="fin" accept=".pdf,.docx,.doc,.pptx,.txt,.png,.jpg">
   <div class="err" id="ferr" style="display:none"></div>
   <div style="margin-top:10px;display:flex;gap:8px">
    <button class="btn amb" onclick="enviar()">Enviar ✔</button>
    <button class="btn gh" onclick="fechar()">Fechar</button></div><p id="fst" class="nota"></p>`;
  document.getElementById("modal").style.display = "flex";
}
function enviar(){
  const f = document.getElementById("fin").files[0];
  const err = document.getElementById("ferr"); err.style.display = "none";
  if (!f){ err.textContent = "Escolha um arquivo."; err.style.display = "block"; return; }
  if (f.size > 15 * 1024 * 1024){ err.textContent = "Arquivo > 15 MB."; err.style.display = "block"; return; }
  document.getElementById("fst").textContent = "Enviando " + f.name + " …";
  const r = new FileReader();
  r.onload = () => api("arqup", { token: TOK, nome: f.name,
      base64: String(r.result).split(",")[1], tipo: f.type })
    .then(x => x.json())
    .then(() => { document.getElementById("fst").textContent = "✔ enviado!"; fechar(); })
    .catch(() => { err.textContent = "Falha no envio."; err.style.display = "block"; });
  r.readAsDataURL(f);
}
function verEntregas(){
  api("entregas", undefined, "&token=" + encodeURIComponent(TOK))
   .then(r => r.json()).then(xs => {
    let h = `<h3 style="color:var(--navy)">📤 Entregas recebidas (${xs.length})</h3>`;
    if (!xs.length) h += "<p class='nota'>Nenhuma entrega ainda.</p>";
    else h += `<table><tr><th>Quando</th><th>Aluno</th><th>Arquivo</th><th>Tamanho</th></tr>` +
      xs.map(x => `<tr><td>${(x.created_at || "").slice(0,16).replace("T"," ")}</td>
        <td>${x.aluno}</td><td><a href="${x.url}" target="_blank">${x.nome}</a></td>
        <td>${Math.round((x.tamanho || 0) / 1024)} KB</td></tr>`).join("") + "</table>";
    h += `<div style="margin-top:12px"><button class="btn gh" onclick="fechar()">Fechar</button></div>`;
    document.getElementById("mbox").innerHTML = h;
    document.getElementById("modal").style.display = "flex";
  }).catch(() => alert("Falha ao listar entregas."));
}
</script></body></html>
"""

# ---------------------------------------------------------------- SQL supabase
SQL_SB = r"""-- AulaViva v2 · Supabase (rodar UMA vez no SQL Editor)
create table if not exists aulaviva_contas (
  id bigserial primary key,
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  nome text not null,
  nome_lc text not null,
  turma text default '',
  salt text not null,
  senha_hash text not null,
  adm int default 0,
  created_at timestamptz default now(),
  unique (disc, code),
  unique (disc, nome_lc)
);
create table if not exists aulaviva_progresso (
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  nome text default '',
  turma text default '',
  payload jsonb default '{}',
  updated_at timestamptz default now(),
  primary key (disc, code)
);
create table if not exists aulaviva_arquivos (
  disc text not null check (disc in ('pi1','lp2')),
  nome text not null,
  tipo text default '',
  tamanho bigint default 0,
  updated_at timestamptz default now(),
  primary key (disc, nome)
);
create table if not exists aulaviva_entregas (
  id bigserial primary key,
  disc text not null check (disc in ('pi1','lp2')),
  code text not null,
  aluno text default '',
  nome text not null,
  caminho text not null,
  tamanho bigint default 0,
  created_at timestamptz default now()
);
create index if not exists ix_ent_code on aulaviva_entregas (disc, code);

-- Buckets
insert into storage.buckets (id, name, public) values ('materiais','materiais', true)
  on conflict (id) do nothing;
insert into storage.buckets (id, name, public) values ('entregas','entregas', false)
  on conflict (id) do nothing;

-- Materiais: leitura pública, escrita só pela função (service role)
drop policy if exists "materiais leitura publica" on storage.objects;
create policy "materiais leitura publica" on storage.objects
  for select using (bucket_id = 'materiais');
-- Entregas: bucket privado — só a função (service role) lê/escreve.

-- RLS: tabelas fechadas (só a edge function, com service role, acessa)
alter table aulaviva_contas     enable row level security;
alter table aulaviva_progresso  enable row level security;
alter table aulaviva_arquivos   enable row level security;
alter table aulaviva_entregas   enable row level security;

-- Migração v1 → v2 (se a tabela aulaviva_alunos existir):
-- insert into aulaviva_progresso (disc, code, nome, turma, payload)
--   select disc, code, nome, turma, coalesce(payload::jsonb,'{}') from aulaviva_alunos
--   on conflict (disc, code) do nothing;
"""

README_SB = r"""# Kit Sala de Aula v2 — Nuvem (Supabase)

## Novidades desta versão
- **Login por aluno**: nome completo + senha criada pelo aluno. Nome **não pode duplicar**.
- **Retomada automática**: ao reabrir o link, o aluno cai **direto onde parou**.
- **Nome completo** no topo; **🗺 Trilha** e o título levam à tela inicial.
- **📤 Entregar**: aluno anexa txt/doc/docx/pdf/odt (fica ligado ao nome dele).
- **Histórico de respostas**: cada resposta (checkpoint e chefe) fica gravada p/ correção.
- **Perfis**: ADM = conta com nome “Juh” (vê o botão 👩‍ Painel); USUÁRIO = aluno normal
  (não vê painel; guia/apostila do professor não estão no kit do aluno). Em 📎 Materiais,
  itens com “professor”/“painel” no nome só aparecem para o ADM (a edge function filtra).
- **Bug corrigido**: alternativas com tags HTML (`<head>` etc.) agora aparecem como texto.

## Instalação (10 min)
1. **SQL**: Supabase → SQL Editor → rode o conteúdo de `supabase/aulaviva_v2.sql`.
2. **Funções** (substituem sync/arquivos antigos):
   - Edge Functions → **Add new function** → nome `avpi1` → cole `functions/avpi1/index.ts` → Deploy.
   - Repita com nome `avlp2` → cole `functions/avlp2/index.ts` → Deploy.
   - Em cada função: Settings → Environment Variables →
     `SUPABASE_URL` = URL do projeto; `SUPABASE_SERVICE_ROLE_KEY` = **secret** key
     (Settings → API Keys → secret); `PROF_TOKEN` = token do painel (crie um novo!).
   - **Verify JWT: DESLIGADO** nas duas.
   - (Opcional) apague as funções antigas `sync`, `sync-lp2`, `arquivos`, `arquivos-lp2`.
3. **Hospede** os 4 arquivos HTML (apps + painéis) no mesmo lugar de antes
   (GitHub Pages / Netlify / pasta do servidor).
4. Teste: abra o app → Criar conta → jogue → feche e reabra (deve voltar onde parou) →
   Painel: nome “Juh” + token.

## Arquivos
| Arquivo | O que é |
|---|---|
| `AulaViva_..._I.html` / `..._II.html` | apps dos alunos (nuvem, com login) |
| `prof_pi1.html` / `prof_lp2.html` | painel da professora (token + nome Juh) |
| `functions/avpi1/index.ts`, `functions/avlp2/index.ts` | edge functions unificadas |
| `supabase/aulaviva_v2.sql` | tabelas + buckets + políticas |
"""

README_RS = r"""# Manutenção Redserver v2 — AulaViva com contas, entregas e respostas

Kit "drop-in" no repositório/servidor (mesmos caminhos de produção):

| Arquivo deste kit            | Destino em Kit_Sala_de_Aula/            |
|------------------------------|------------------------------------------|
| api_v2.php                   | aulaviva/api.php (SUBSTITUIR o conteúdo) |
| aulaviva_v2.sql              | rodar 1× no MySQL (banco `loja_turma`)   |
| AulaViva_pi1_index.html      | apps-nuvem/AulaViva_pi1_index.html       |
| AulaViva_lp2_index.html      | apps-nuvem/AulaViva_lp2_index.html       |
| Painel_Professor_pi1.html    | apps-nuvem/Painel_Professor_pi1.html     |
| Painel_Professor_lp2.html    | apps-nuvem/Painel_Professor_lp2.html     |

## O que muda no servidor
1. **Banco**: rode `aulaviva_v2.sql` (cria as tabelas `aulaviva_contas/progresso/
   arquivos/entregas` no banco `loja_turma`, que já existe). A migração opcional
   do v1 (`aulaviva_alunos`) está comentada no final do SQL.
2. **API**: substitua o conteúdo de `aulaviva/api.php` pelo `api_v2.php`.
   Credenciais por ambiente no pool php-fpm do vhost (padrão do v1):
   `env[LOJA_DB_PASS] = <senha do loja_app>` e
   `env[AULAVIVA_PROF_TOKEN] = <token NOVO>` (o antigo circulou em docs — rotacione).
3. **Pastas**: crie `aulaviva/materiais/{pi1,lp2}` e `aulaviva/entregas/{pi1,lp2}`
   com permissão de escrita pelo usuário do php (ex.: `chown -R www-data`).
4. **nginx**: nada muda. O cookie de sessão só usa `Secure` quando a requisição
   chega via HTTPS (ngrok conta como HTTPS) — em HTTP puro o login também funciona.
5. **Apps/painel**: os 4 HTML apontam para `../aulaviva/api.php` (URL relativa —
   funciona em qualquer domínio). Aluno com aba antiga aberta precisa recarregar.

## Regras de acesso
- Aluno: cria conta com **nome único + senha**; cookie httpOnly mantém a sessão;
  ao reabrir o link, **volta direto onde parou**.
- ADM (“Juh”): vê o botão **Painel** no app; o painel ainda exige o token.
- USUÁRIO: não vê painel; guia/apostila do professor **não estão no kit do aluno**;
  em 📎 Materiais, itens com “professor”/“painel” no nome **não aparecem** para aluno
  (filtro no app e também no servidor — rota `arq` do `api.php`).
- Entregas: botão **📤 Entregar** (txt/doc/docx/pdf/odt, até 12 MB) →
  ficam em `aulaviva/entregas/<disc>/<code>/` e listadas no painel.
- Todas as respostas (checkpoint + chefe) ficam no payload (`hist`) → painel
  mostra por aluno e o CSV exporta o histórico completo.

## Segurança (não pule!)
- Nenhuma senha/token no código: `getenv` com fallback de dev (como no v1).
- Senhas de alunos: `password_hash` (bcrypt) — nunca em texto puro.
- Erros de BD vão para `error_log`; navegador recebe mensagem genérica.
"""


def montar():
    tmp = os.path.join(_ROOT, "material", "_kits_v2")
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    resumo = []
    for nome_kit, api_tpl in (("Kit_Sala_de_Aula_v2", SB_BASE + "/functions/v1/__FUNC__"),
                              ("Manutencao_Redserver_v2", RS_BASE)):
        # kit redserver usa os NOMES DO REPOSITÓRIO (drop-in em apps-nuvem/)
        repo_names = (nome_kit == "Manutencao_Redserver_v2")
        d = os.path.join(tmp, nome_kit)
        os.makedirs(d, exist_ok=True)
        for disc, cfg in DISCS.items():
            base = os.path.join(_BASE, f"AulaViva_{cfg['slug']}.BASE.html")
            html = open(base, encoding="utf-8").read()
            api = api_tpl.replace("__FUNC__", cfg["sb_func"])
            app_nome = (f"AulaViva_{disc}_index.html" if repo_names
                        else f"AulaViva_{cfg['slug']}.html")
            prof_nome = (f"Painel_Professor_{disc}.html" if repo_names
                         else f"prof_{disc}.html")
            html = (html.replace('"__API__"', json_str(api))
                        .replace('"__PAINEL__"', json_str(prof_nome)))
            # FIX/assert: DISC da base precisa bater com a disciplina do kit
            # (regressão antiga: LP2 saía com DISC "pi1" e misturava as turmas)
            assert f'const DISC = "{disc}";' in html, f"DISC errado em {app_nome}"
            open(os.path.join(d, app_nome), "w", encoding="utf-8").write(html)
            prof = PROF_HTML.replace("__API__", api).replace("__DISC__", disc) \
                            .replace("__APP__", app_nome)
            open(os.path.join(d, prof_nome), "w", encoding="utf-8").write(prof)
            if nome_kit == "Kit_Sala_de_Aula_v2":
                fdir = os.path.join(d, "functions", cfg["sb_func"])
                os.makedirs(fdir, exist_ok=True)
                open(os.path.join(fdir, "index.ts"), "w", encoding="utf-8") \
                    .write(EDGE_AV.replace("__DISC__", disc))
        if nome_kit == "Kit_Sala_de_Aula_v2":
            os.makedirs(os.path.join(d, "supabase"), exist_ok=True)
            open(os.path.join(d, "supabase", "aulaviva_v2.sql"), "w", encoding="utf-8").write(SQL_SB)
            open(os.path.join(d, "README_DEPLOY.md"), "w", encoding="utf-8").write(README_SB)
        else:
            shutil.copy(os.path.join(_ROOT, "redserver", "api_v2.php"),
                        os.path.join(d, "api_v2.php"))
            shutil.copy(os.path.join(_ROOT, "redserver", "aulaviva_v2.sql"),
                        os.path.join(d, "aulaviva_v2.sql"))
            open(os.path.join(d, "README_DEPLOY.md"), "w", encoding="utf-8").write(README_RS)
        zp = os.path.join(_OUT, nome_kit + ".zip")
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
            for raiz, _, arqs in os.walk(d):
                for a in sorted(arqs):
                    fp = os.path.join(raiz, a)
                    z.write(fp, os.path.join(nome_kit, os.path.relpath(fp, d)))
        resumo.append((zp, len(os.listdir(d))))
    return resumo


def json_str(s):
    import json as _j
    return _j.dumps(s)


if __name__ == "__main__":
    for zp, n in montar():
        print("OK:", zp, f"({os.path.getsize(zp)//1024} KB)")
