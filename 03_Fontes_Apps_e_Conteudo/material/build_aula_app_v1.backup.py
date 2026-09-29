# -*- coding: utf-8 -*-
"""Gera o APP-AULA interativo (.html único, offline): a teoria das 72 aulas em
cartas de jogo com checkpoints, exercícios e 'chefe do módulo' (teste rápido).
Modos: Aluno (ritmo próprio) e Turma (projetor).
Uso: python3 build_aula_app.py
"""
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

import importlib as _il
_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))
MODULOS = _PKG.MODULOS
QA = _PKG.quizzes
comuns = _PKG.comuns

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}


def conv_bloco(b):
    k = b[0]
    if k == "p":
        return {"t": "p", "h": b[1]}
    if k == "h":
        return {"t": "h", "x": b[1]}
    if k == "lista":
        return {"t": "ul", "it": b[1]}
    if k == "lista_num":
        return {"t": "ol", "it": b[1]}
    if k in ("conceito", "analogia"):
        return {"t": "bx", "k": {"conceito": "con", "analogia": "ana"}[k],
                "ti": b[1][0], "x": b[1][1]}
    if k == "dica":
        return {"t": "bx", "k": "dica", "ti": None, "x": b[1]}
    if k == "atencao":
        return {"t": "bx", "k": "aten", "ti": None, "x": b[1]}
    if k == "codigo":
        return {"t": "cd", "ti": b[1].get("titulo", ""), "lg": b[1].get("ling", "php"),
                "ln": b[1].get("linhas", [])}
    if k == "tabela":
        return {"t": "tb", "cab": b[1]["cab"], "lin": b[1]["lin"]}
    return None


DATA = {"mods": []}
for m in MODULOS:
    aulas = []
    for a in m["aulas"]:
        base = QA.ALIASES.get(a["num"], a["num"])
        qs = [[q[0], q[1], q[2], q[3]] for q in QA.Q.get(base, [])]
        cards = [c for c in (conv_bloco(b) for b in a["blocos"]) if c]
        aulas.append({"n": a["num"], "ti": a["titulo"], "cards": cards, "qs": qs})
    DATA["mods"].append({
        "n": m["num"],
        "ti": m["titulo"],
        "parte": ROMAN[m["parte_num"]],
        "parte_ti": m["parte_titulo"],
        "faixa": m["aulas_faixa"],
        "obj": m["objetivos"],
        "aulas": aulas,
        "exs": [{"ti": e["titulo"], "tp": e["tipo"], "en": e["enunciado"],
                 "ps": e.get("passos", [])} for e in m["exercicios"]],
        "boss": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
                 for q in m["teste_rapido"]],
    })

HTML = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AulaViva — __TITULO__</title>
<style>
 :root{--navy:#0d2b4e;--navy2:#143a66;--azul:#1b5faa;--sky:#e9f1fa;--amber:#f59e0b;
   --amberd:#9a6206;--verde:#26890c;--verm:#e21b3c;--roxo:#6d28d9;--ink:#1f2937;
   --soft:#5b6b7c;--bg:#f4f7fb;--card:#ffffff;}
 *{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
 body{font-family:"Segoe UI",system-ui,Roboto,Arial,sans-serif;background:var(--bg);color:var(--ink)}
 header{background:var(--navy);color:#fff;padding:10px 16px;display:flex;gap:12px;
   align-items:center;justify-content:space-between;position:sticky;top:0;z-index:9;
   box-shadow:0 2px 0 #081b33}
 header h1{font-size:19px}
 header .dir{display:flex;gap:8px;align-items:center}
 .pill{background:var(--amber);color:#3a2700;border:none;border-radius:20px;padding:6px 14px;
   font-weight:800;font-size:12.5px;cursor:pointer;font-family:inherit}
 .pill.ghost{background:transparent;color:#cfe1f5;border:2px solid #2a527f}
 .wrap{max-width:960px;margin:0 auto;padding:16px 14px 60px}
 body.turma .wrap{max-width:1200px}
 body.turma{font-size:1.22rem}
 body.turma .cardp{padding:34px 30px}
 body.turma .cardp p,body.turma .cardp li{font-size:1.35rem;line-height:1.55}
 body.turma .cardp h3{font-size:1.6rem}
 body.turma .perg{font-size:1.7rem !important}
 body.turma .op{font-size:1.35rem !important;min-height:74px}
 body.turma code,body.turma .codewrap{font-size:1.05rem !important}
 .bar{height:10px;background:#dfe8f2;border-radius:8px;overflow:hidden;margin:10px 0 16px}
 .bar i{display:block;height:100%;background:linear-gradient(90deg,var(--amber),#ffcf4d);width:0;
   transition:width .3s}
 .cardp{background:var(--card);border-radius:18px;padding:24px 22px;
   box-shadow:0 3px 14px rgba(13,43,78,.09);animation:pop .25s ease}
 @keyframes pop{from{transform:translateY(8px);opacity:.4}to{transform:none;opacity:1}}
 .kick{font-size:12px;font-weight:800;letter-spacing:.6px;color:var(--amberd);text-transform:uppercase}
 .cardp h2{color:var(--navy);font-size:24px;margin:4px 0 12px}
 .cardp h3{color:var(--azul);font-size:17px;margin:14px 0 6px}
 .cardp p{font-size:16.5px;line-height:1.6;margin:8px 0;text-align:justify}
 .cardp ul,.cardp ol{margin:8px 0 8px 22px}
 .cardp li{font-size:16px;line-height:1.5;margin:5px 0}
 .bx{border-radius:14px;padding:14px 16px;margin:12px 0;border-left:6px solid}
 .bx b.ti{display:block;font-size:12.5px;letter-spacing:.5px;margin-bottom:4px;text-transform:uppercase}
 .bx.con{background:#e9f1fa;border-color:var(--azul)} .bx.con b.ti{color:var(--azul)}
 .bx.ana{background:#f1edfb;border-color:var(--roxo)} .bx.ana b.ti{color:var(--roxo)}
 .bx.dica{background:#fef4e2;border-color:var(--amber)} .bx.dica b.ti{color:var(--amberd)}
 .bx.aten{background:#fbeae8;border-color:var(--verm)} .bx.aten b.ti{color:var(--verm)}
 .bx p{margin:2px 0;font-size:15.5px}
 .codewrap{background:#0f2237;border-radius:12px;margin:12px 0;overflow:hidden}
 .codebar{background:#1a3a5c;color:#bbd4ee;font:700 11.5px Consolas,monospace;
   padding:6px 12px;display:flex;justify-content:space-between}
 .codewrap pre{padding:12px 14px;overflow-x:auto;font:13.5px/1.5 Consolas,monospace;color:#dce9f7}
 .tbl{width:100%;border-collapse:collapse;margin:12px 0;font-size:14.5px}
 .tbl th{background:var(--navy);color:#fff;padding:8px 10px;text-align:left}
 .tbl td{border:1px solid #c9d8e8;padding:7px 10px;vertical-align:top}
 .tbl tr:nth-child(even) td{background:#f4f8fc}
 .nav{display:flex;gap:10px;margin-top:16px;flex-wrap:wrap}
 .btn{border:none;border-radius:12px;padding:12px 22px;font-size:15.5px;font-weight:800;
   cursor:pointer;font-family:inherit;background:var(--azul);color:#fff}
 .btn.amb{background:var(--amber);color:#3a2700}
 .btn.gh{background:#e3ecf7;color:var(--navy)}
 .btn:disabled{opacity:.4;cursor:default}
 .perg{font-size:20px;font-weight:800;color:var(--ink);margin:6px 0 14px;line-height:1.4}
 .op{display:flex;gap:12px;align-items:center;width:100%;text-align:left;border:none;
   border-radius:14px;padding:14px 16px;margin:9px 0;font-size:16.5px;font-weight:600;
   color:#fff;cursor:pointer;font-family:inherit;line-height:1.35}
 .op .fm{font-size:22px}
 .op.c0{background:#e21b3c}.op.c1{background:#1368ce}.op.c2{background:#ffa602;color:#3a2700}
 .op.c3{background:#26890c}
 .op:disabled{cursor:default}
 .op.ok{outline:5px solid #0e5c00;outline-offset:-5px}
 .op.no{outline:5px solid #7d0018;outline-offset:-5px;opacity:.85}
 .fb{border-radius:14px;padding:14px 16px;margin-top:12px;color:#fff;font-size:15.5px}
 .fb.ok{background:var(--verde)} .fb.no{background:var(--verm)}
 .hud{display:flex;gap:14px;font-weight:800;color:var(--navy);font-size:15px;align-items:center}
 .modgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
 .modcard{background:#fff;border-radius:16px;padding:16px;cursor:pointer;border:3px solid #e6edf6;
   transition:border-color .15s, transform .15s;position:relative}
 .modcard:hover{border-color:var(--azul);transform:translateY(-3px)}
 .modcard h3{color:var(--navy);font-size:16.5px;margin:4px 0}
 .modcard .sub{font-size:12.5px;color:var(--soft)}
 .modcard .st{position:absolute;top:12px;right:14px;font-size:20px}
 .prog{font-size:11.5px;font-weight:800;color:var(--azul);margin-top:8px}
 .mini{height:7px;background:#e3ecf7;border-radius:6px;overflow:hidden;margin-top:5px}
 .mini i{display:block;height:100%;background:var(--verde)}
 .exitem{background:#fffdf6;border:2px solid #ead9b5;border-radius:14px;padding:13px 15px;margin:10px 0}
 .exitem label{display:flex;gap:10px;align-items:flex-start;cursor:pointer}
 .exitem input{width:22px;height:22px;margin-top:3px;accent-color:var(--verde)}
 .exitem b{color:var(--navy)}
 .exitem .en{font-size:14.5px;color:var(--soft);margin-top:4px}
 .fimbox{text-align:center;padding:30px 20px}
 .fimbox .em{font-size:52px}
 .nota{font-size:12.5px;color:var(--soft);margin-top:10px;line-height:1.5}
 .dica-turma{background:#143a66;color:#cfe1f5;border-radius:12px;padding:10px 14px;font-size:13px;
   margin-bottom:12px}
 #modal{position:fixed;inset:0;background:rgba(8,20,38,.62);display:flex;align-items:center;
   justify-content:center;z-index:20}
 .mbox{background:#fff;border-radius:18px;padding:26px 24px;max-width:430px;width:92%;
   box-shadow:0 12px 44px rgba(0,0,0,.4);animation:pop .25s ease}
 .mbox h3{color:var(--navy);margin-bottom:4px;font-size:20px}
 .mbox input{width:100%;border:2px solid #d9d4ee;border-radius:10px;padding:11px 13px;
   font-size:15.5px;margin:8px 0;font-family:inherit}
 .mbox input:focus{outline:3px solid #ffd57e;border-color:var(--amber)}

/* ---------- responsivo (celular/projetor pequeno) ---------- */
@media (max-width:760px){
  header{padding:10px 12px; flex-wrap:wrap; gap:8px}
  header h1{font-size:16px}
  header .dir{gap:6px; flex-wrap:wrap}
  .pill{padding:6px 10px; font-size:11.5px}
  .wrap{padding:12px 10px 60px}
  .cardp{padding:16px 14px}
  .cardp h2{font-size:19px}
  .cardp p, .cardp li{font-size:14.5px}
  .pergunta{font-size:17px}
  .op{font-size:14.5px; min-height:52px; padding:10px 12px 10px 46px}
  .op .forma{font-size:17px; left:12px}
  .codewrap pre{font-size:10.5px; overflow-x:auto}
  .modgrid{grid-template-columns:1fr}
  .mbox{padding:18px 14px; width:94%}
  .mbox input{width:100%}
  table{display:block; overflow-x:auto}
  .btn{padding:10px 16px; font-size:14px}
}
</style>
</head>
<body>
<header>
  <h1>🎓 AulaViva · __TITULO__</h1>
  <div class="dir">
    <span class="hud" id="hud"></span>
    <button class="pill ghost" id="btMapa" onclick="abrirMapa()" style="display:none">🎯 Ir para</button>
    <button class="pill ghost" id="btAluno" onclick="editarNome()">👤 Identificar</button>
    <button class="pill ghost" id="btTurma" onclick="toggleTurma()">📽 Modo Turma</button>
    <button class="pill" onclick="irHome()">🗺 Trilha</button>
  </div>
</header>
<div class="wrap" id="app"></div>
<div id="mapa" style="display:none">
  <div class="mbox" style="max-width:600px">
    <h3>🎯 Ir diretamente para…</h3>
    <p class="nota">Um clique leva você à tela escolhida deste módulo (cartas ou checkpoints).</p>
    <div id="mapaLista" style="max-height:55vh;overflow:auto;padding:4px 0"></div>
    <div class="nav"><button class="btn gh" onclick="fecharMapa()">Fechar</button></div>
  </div>
</div>
<div id="modal" style="display:none">
  <div class="mbox">
    <h3>👤 Cadastro do aluno</h3>
    <p class="nota">Seu nome fica salvo <b>neste navegador</b> e aparece sempre no topo da tela,
       junto dos seus pontos. Preencha uma única vez.</p>
    <input id="inNome" type="text" maxlength="40" placeholder="Seu nome completo"
       onkeydown="if(event.key==='Enter')salvarNome()">
    <input id="inTurma" type="text" maxlength="20" placeholder="Turma (ex.: 2/2026) — opcional"
       onkeydown="if(event.key==='Enter')salvarNome()">
    <div class="nav">
      <button class="btn amb" onclick="salvarNome()">Salvar e jogar ✔</button>
      <button class="btn gh" onclick="fecharModal()">Agora não</button>
    </div>
    <p class="nota" style="margin-top:12px"><b>Vai trocar de computador?</b> Leve seu progresso junto
       (pen drive, Drive ou WhatsApp):</p>
    <div class="nav">
      <button class="btn gh" onclick="exportarProg()">📤 Exportar progresso</button>
      <button class="btn gh" onclick="document.getElementById('inFile').click()">📥 Importar progresso</button>
    </div>
    <input type="file" id="inFile" accept=".json,application/json" style="display:none"
       onchange="aoLerArquivo(event)">
  </div>
</div>
<script>
const DATA = __DATA__;
const FM = ["▲","◆","●","■"];
const K = "__KEY__";
const LBL = "__LBL__";
const app = document.getElementById("app");
const hud = document.getElementById("hud");
let S = { mi:0, step:0, flow:null, pts:0, seq:0, exok:{}, done:{}, boss:{},
          pos:null, aulas:{}, scored:{}, nome:"", turma:"" };
try{ const sv = localStorage.getItem(K); if (sv) Object.assign(S, JSON.parse(sv)); }catch(e){}
S.flow = null;
function save(){ try{ localStorage.setItem(K, JSON.stringify(
  {mi:S.mi, pts:S.pts, exok:S.exok, done:S.done, boss:S.boss,
   pos:S.pos, aulas:S.aulas, scored:S.scored, nome:S.nome, turma:S.turma})); }catch(e){} }
function esc(s){ return String(s); } // conteúdo próprio e confiável
function toggleTurma(){ document.body.classList.toggle("turma");
  document.getElementById("btTurma").textContent =
    document.body.classList.contains("turma") ? "👤 Modo Aluno" : "📽 Modo Turma"; }
function setHud(){ hud.innerHTML = S.flow ? `⭐ ${S.pts}` + (S.seq>=2?` 🔥${S.seq}`:"") : "";
  const bm = document.getElementById("btMapa");
  if (bm) bm.style.display = S.flow ? "" : "none"; }
function primeiroNome(){ return (S.nome || "").split(" ")[0] || ""; }
function updateNomeBtn(){ const b = document.getElementById("btAluno");
  if (b) b.textContent = S.nome ? "👤 " + primeiroNome() : "👤 Identificar"; }
function abrirModal(){ const m = document.getElementById("modal"); m.style.display = "flex";
  document.getElementById("inNome").value = S.nome || "";
  document.getElementById("inTurma").value = S.turma || "";
  setTimeout(() => document.getElementById("inNome").focus(), 60); }
function fecharModal(){ document.getElementById("modal").style.display = "none"; }
function editarNome(){ abrirModal(); }
function salvarNome(){ const v = document.getElementById("inNome").value.trim();
  if (!v){ document.getElementById("inNome").focus(); return; }
  S.nome = v; S.turma = document.getElementById("inTurma").value.trim();
  save(); updateNomeBtn(); fecharModal();
  if (!S.flow) renderHome(); }
function payloadProg(){ return { mi:S.mi, pts:S.pts, exok:S.exok, done:S.done, boss:S.boss,
  pos:S.pos, aulas:S.aulas, scored:S.scored, nome:S.nome, turma:S.turma }; }
function exportarProg(){
  try{
    const blob = new Blob([JSON.stringify(payloadProg())], {type:"application/json"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "aulaviva-progresso-" + (primeiroNome() || "aluno").toLowerCase() + ".json";
    if (document.body && document.body.appendChild) document.body.appendChild(a);
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    S._msg = "📤 Arquivo de progresso baixado ✔ leve-o para o outro computador.";
  }catch(e){ S._msg = "Não foi possível exportar neste navegador ⚠"; }
  fecharModal(); irHome();
}
function aplicarProg(txt){
  const d = JSON.parse(txt);
  if (typeof d.pts !== "number" || !d.aulas || !d.scored) throw new Error("formato");
  Object.assign(S, d); S.flow = null; S.seq = 0;
  save(); updateNomeBtn();
}
function aoLerArquivo(ev){
  const f = ev.target.files && ev.target.files[0]; if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try { aplicarProg(r.result);
      S._msg = "📥 Progresso de " + (primeiroNome() || "aluno") + " carregado com sucesso ✔";
    } catch(e){ S._msg = "Arquivo de progresso inválido ⚠"; }
    fecharModal(); irHome();
  };
  r.readAsText(f);
  ev.target.value = "";
}

/* ---------- realce de código ---------- */
const KW = /(echo|print|if|else|elseif|endif|for|endforeach|foreach|while|do|switch|case|break|default|function|return|true|false|null|exit|die|include|require|include_once|require_once|define|as|new|isset|empty)\b/;
function hiLine(line, lg){
  const out = [];
  if (lg === "html") return hiHtml(line);
  if (lg === "vb") return hiVb(line);
  if (lg === "sql") return hiSql(line);
  if (lg === "shell" || lg === "texto"){
    const i = line.indexOf("#");
    if (lg === "shell" && i >= 0){ out.push(["", line.slice(0,i)], ["c", line.slice(i)]); return out; }
    return [["", line]];
  }
  // php
  const ci = line.indexOf("//");
  let code = line, com = null;
  if (ci >= 0){ code = line.slice(0, ci); com = line.slice(ci); }
  let re = /("[^"]*"|'[^']*')|(<\?php\b|<\?=|\?>)|(<\/?[A-Za-z][^>]*>)|(\$[A-Za-z_]\w*)|\b([A-Za-z_]\w*)(?=\s*\()/g;
  let last = 0, m;
  while ((m = re.exec(code))){
    if (m.index > last) out.push(...tokSolta(code.slice(last, m.index)));
    if (m[1]) out.push(["s", m[1]]);
    else if (m[2]) out.push(["k", m[2]]);
    else if (m[3]) out.push(["t", m[3]]);
    else if (m[4]) out.push(["v", m[4]]);
    else if (m[5]) out.push(["f", m[5]]);
    last = re.lastIndex;
  }
  if (last < code.length) out.push(...tokSolta(code.slice(last)));
  if (com) out.push(["c", com]);
  return out;
}
function tokSolta(txt){
  const res = []; let re = KW, last = 0, m;
  const r2 = new RegExp(KW.source, "g");
  while ((m = r2.exec(txt))) {
    if (m.index > last) res.push(["", txt.slice(last, m.index)]);
    res.push(["k", m[0]]); last = r2.lastIndex;
  }
  if (last < txt.length) res.push(["", txt.slice(last)]);
  return res;
}
function hiHtml(line){
  const res = []; let re = /(<\/?[A-Za-z][^>]*>)|("[^"]*")/g, last = 0, m;
  while ((m = re.exec(line))){
    if (m.index > last) res.push(["", line.slice(last, m.index)]);
    res.push(m[1] ? ["t", m[1]] : ["s", m[2]]); last = re.lastIndex;
  }
  if (last < line.length) res.push(["", line.slice(last)]);
  return res;
}

function hiVb(line){
  const out=[]; let instr=false, ci=-1;
  for (let i=0;i<line.length;i++){ const ch=line[i];
    if (ch==='"') instr=!instr; else if (ch==="'" && !instr){ ci=i; break; } }
  const code = ci>=0 ? line.slice(0,ci) : line;
  const com  = ci>=0 ? line.slice(ci) : null;
  const re=/("[^"]*")|\b(Dim|As|Sub|End|Function|If|Then|Else|ElseIf|For|Next|Do|While|Loop|Until|Select|Case|Public|Private|Print|Set|New|Not|And|Or|Mod|To|Step|ByVal|ByRef|Type|Exit|On|Error|GoTo|Is|Nothing|True|False|Call|Each|In|Option)\b|\b(\d+(?:\.\d+)?)\b/g;
  let last=0,m;
  while((m=re.exec(code))){
    if (m.index>last) out.push(["", code.slice(last,m.index)]);
    if (m[1]) out.push(["s",m[1]]); else if (m[2]) out.push(["k",m[2]]); else out.push(["n",m[3]]);
    last=re.lastIndex;
  }
  if (last<code.length) out.push(["", code.slice(last)]);
  if (com) out.push(["c", com]);
  return out;
}
function hiSql(line){
  const out=[]; const ci=line.indexOf("--");
  const code = ci>=0 ? line.slice(0,ci) : line;
  const com  = ci>=0 ? line.slice(ci) : null;
  const re=/('[^']*')|\b(SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE|CREATE|TABLE|DATABASE|USE|SHOW|ORDER|BY|GROUP|AND|OR|NOT|LIKE|BETWEEN|IN|PRIMARY|KEY|AUTO_INCREMENT|INT|VARCHAR|DECIMAL|DATE|AS|COUNT|SUM|AVG|MAX|MIN|DESC|ASC)\b|\b(\d+(?:\.\d+)?)\b/gi;
  let last=0,m;
  while((m=re.exec(code))){
    if (m.index>last) out.push(["", code.slice(last,m.index)]);
    if (m[1]) out.push(["s",m[1]]); else if (m[2]) out.push(["k",m[2].toUpperCase()]); else out.push(["n",m[3]]);
    last=re.lastIndex;
  }
  if (last<code.length) out.push(["", code.slice(last)]);
  if (com) out.push(["c", com]);
  return out;
}
const COLS = { s:"#9ece6a", k:"#d38ae0", t:"#6cb6ff", v:"#f2777a", f:"#6cb6ff", c:"#7f96ad", n:"#e5c07b" };
function codeHtml(cd){
  const lines = cd.ln.map(l => {
    const segs = hiLine(l, cd.lg || "php");
    const inner = segs.map(([k, t]) =>
      k ? `<span style="color:${COLS[k]}">${t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}</span>`
        : t.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")).join("");
    return inner || "&nbsp;";
  }).join("\n");
  return `<div class="codewrap"><div class="codebar"><span>${cd.ti||"código"}</span><span>${(cd.lg||"php").toUpperCase()}</span></div><pre>${lines}</pre></div>`;
}

/* ---------- trilha (home) ---------- */
function irHome(){ S.flow = null; setHud(); renderHome(); }
function renderHome(){
  let h = S.nome
    ? `<h2 style="color:var(--navy);margin:6px 0 4px">Olá, ${primeiroNome()}! 👋</h2>
       <div class="kick">Trilha do semestre${S.turma ? " · Turma " + S.turma : ""} · seus pontos: ⭐ ${S.pts}</div>`
    : `<h2 style="color:var(--navy);margin:6px 0 4px">Trilha do semestre</h2>`;
  h += `<p class="nota">Cada módulo é uma fase: cartas de aula com checkpoints ✅, exercícios 🛠 e o
   <b>chefe do módulo</b> ⚡ (teste rápido). Seu progresso fica salvo <b>neste navegador</b> —
   ao reabrir o arquivo, use o botão “Continuar de onde parou”.</p>`;
  if (S._msg){ h += `<div class="cardp" style="border:3px solid var(--verde);margin:12px 0">
      <b style="color:var(--verde)">${S._msg}</b></div>`; S._msg = null; }
  if (S.pos){
    const pm = DATA.mods.find(x => x.n === S.pos.mi);
    if (pm){
      const fB = S.flow, sB = S.step;
      S.flow = buildFlow(pm); S.step = Math.min(S.pos.step, S.flow.length-1);
      const lb = stepLabel();
      S.flow = fB; S.step = sB;
      h += `<div class="cardp" style="border:3px solid var(--amber);margin:14px 0">
        <b style="color:var(--navy);font-size:17px">▶ Continuar de onde parou</b>
        <p style="margin:4px 0">Módulo ${pm.n} — ${pm.ti} · ${lb} · ⭐ ${S.pts} pts</p>
        <div class="nav"><button class="btn amb" onclick="continuar()">Continuar ▶</button>
        <button class="btn gh" onclick="S.pos=null;save();renderHome()">Só ver a trilha</button></div></div>`;
    }
  }
  h += `<div class="modgrid" style="margin-top:6px">`;
  for (const m of DATA.mods){
    const d = (S.aulas["m"+m.n] || []).length;
    const tot = m.aulas.length;
    const st = S.done["m"+m.n] ? "🏆" : d > 0 ? "⭐" : "📘";
    h += `<div class="modcard" onclick="abrirMod(${m.n})">
      <span class="st">${st}</span>
      <div class="kick">Módulo ${m.n} · Parte ${m.parte}</div>
      <h3>${m.ti}</h3>
      <div class="sub">${m.faixa} · ${tot} aulas interativas</div>
      <div class="prog">${d}/${tot} aulas concluídas</div>
      <div class="mini"><i style="width:${tot? Math.round(100*d/tot):0}%"></i></div>
    </div>`;
  }
  app.innerHTML = h + "</div>";
}

/* ---------- fluxo do módulo ---------- */
function buildFlow(m){
  const f = [{ k:"intro" }];
  m.aulas.forEach((a, ai) => {
    a.cards.forEach((c, ci) => f.push({ k:"card", ai, ci }));
    a.qs.forEach((q, qi) => f.push({ k:"chk", ai, qi }));
  });
  f.push({ k:"exs" });
  m.boss.forEach((q, qi) => f.push({ k:"boss", qi }));
  f.push({ k:"fim" });
  return f;
}
function abrirMod(n, step){
  const m = DATA.mods.find(x => x.n === n);
  S.mi = n; S.seq = 0;
  S.flow = buildFlow(m);
  const alvo = (step !== undefined) ? step
             : ((S.pos && S.pos.mi === n) ? S.pos.step : 0);
  S.step = Math.max(0, Math.min(S.flow.length - 1, alvo));
  S.pos = { mi:n, step:S.step };
  save(); setHud(); renderStep();
}
function continuar(){ if (S.pos) abrirMod(S.pos.mi, S.pos.step); }
function chip(i, txt){ return `<button class="btn gh" style="margin:3px 5px 3px 0;padding:8px 13px;
  font-size:13px" onclick="irPara(${i})">${txt}</button>`; }
function irPara(i){
  S.step = Math.max(0, Math.min(S.flow.length - 1, i));
  S.pos = { mi:S.mi, step:S.step }; save(); fecharMapa(); renderStep();
}
function abrirMapa(){
  if (!S.flow) return;
  const m = mod(); let h = "";
  S.flow.forEach((st, i) => {
    if (st.k === "card" && st.ci === 0){
      h += `<div class="kick" style="margin:11px 0 3px">${LBL} ${m.aulas[st.ai].n} — ${m.aulas[st.ai].ti}</div>`;
      h += chip(i, "🃏 Cartas da aula");
    } else if (st.k === "chk"){
      h += chip(i, "✅ Checkpoint " + (st.qi+1) + "/" + m.aulas[st.ai].qs.length +
                 (S.scored[chkId(st)] ? " ✔" : ""));
    } else if (st.k === "exs"){
      h += `<div class="kick" style="margin:11px 0 3px">Fechamento do módulo</div>` + chip(i, "🛠 Exercícios");
    } else if (st.k === "boss"){
      h += chip(i, "⚡ Chefe · pergunta " + (st.qi+1));
    }
  });
  document.getElementById("mapaLista").innerHTML = h;
  document.getElementById("mapa").style.display = "flex";
}
function fecharMapa(){ document.getElementById("mapa").style.display = "none"; }
function chkId(st){ return "m"+S.mi + (st.k === "boss" ? ":b"+st.qi : ":a"+st.ai+":q"+st.qi); }
function rotuloStep(i){
  const f = S.flow; if (!f || i < 0 || i >= f.length) return "";
  const st = f[i]; const m = mod();
  if (st.k === "intro") return "abertura da fase";
  if (st.k === "card")  return "carta " + (st.ci+1) + " · " + LBL + " " + m.aulas[st.ai].n;
  if (st.k === "chk")   return "checkpoint · " + LBL + " " + m.aulas[st.ai].n +
                               " (" + (st.qi+1) + "/" + m.aulas[st.ai].qs.length + ")";
  if (st.k === "exs")   return "exercícios do módulo";
  if (st.k === "boss")  return "chefe · pergunta " + (st.qi+1);
  return "finalização";
}
function stepLabel(){
  const st = S.flow[S.step]; const m = mod();
  if (st.k === "intro") return "abertura da fase";
  if (st.k === "card")  return "Aula " + m.aulas[st.ai].n + " · carta " + (st.ci+1);
  if (st.k === "chk")   return "Checkpoint da " + LBL + " " + m.aulas[st.ai].n;
  if (st.k === "exs")   return "Exercícios do módulo";
  if (st.k === "boss")  return "Chefe do módulo · pergunta " + (st.qi+1);
  return "finalização";
}
function mod(){ return DATA.mods.find(x => x.n === S.mi); }
function pct(){ return Math.round(100 * S.step / (S.flow.length - 1)); }
function topo(tit, kick){
  return `<div class="bar"><i style="width:${pct()}%"></i></div>
    <div class="kick">${kick}</div><div class="cardp"><h2>${tit}</h2>`;
}
function navBtns(volt, rotulo){
  const volta = (volt && S.step > 0)
    ? `<button class="btn gh" onclick="passo(-1)">← Voltar: ${rotuloStep(S.step-1)}</button>` : "";
  return `</div><div class="nav">${volta}
    <button class="btn" onclick="passo(1)">${rotulo||"Continuar →"}</button></div>`;
}
function passo(d){ S.step = Math.max(0, Math.min(S.flow.length-1, S.step+d));
  S.pos = { mi:S.mi, step:S.step }; save(); renderStep(); }

function renderStep(){
  const st = S.flow[S.step];
  const m = mod();
  window.scrollTo(0,0);
  if (st.k === "intro"){
    app.innerHTML = topo(`Módulo ${m.n} — ${m.ti}`, `Parte ${m.parte} · ${m.faixa}`) +
      `<p><b>${m.parte_ti}.</b> Nesta fase você vai viver ${m.aulas.length} aulas interativas.</p>
       <h3>🎯 Objetivos da fase</h3><ul>` +
      m.obj.map(o => `<li>${o}</li>`).join("") + `</ul>
       <p class="nota">Como funciona: cada <b>carta</b> traz um pedaço da aula; no fim de cada aula,
       <b>checkpoints</b> com perguntas que valem pontos (⭐) e sequência (🔥). Setas do teclado também avançam.</p>` +
      navBtns(false, "Começar a fase ▶");
    return;
  }
  if (st.k === "card"){
    const a = m.aulas[st.ai], c = a.cards[st.ci];
    let h = topo(`${LBL} ${a.n} — ${a.ti}`, `Módulo ${m.n} · carta ${st.ci+1}/${a.cards.length}`);
    h += cardHtml(c);
    h += navBtns(true, st.ci === a.cards.length-1 ? "Ir aos checkpoints ✅" : "Continuar →");
    app.innerHTML = h;
    return;
  }
  if (st.k === "chk" || st.k === "boss"){
    const isBoss = st.k === "boss";
    const q = isBoss ? m.boss[st.qi] : m.aulas[st.ai].qs[st.qi];
    const tit = isBoss ? `CHEFE DO MÓDULO ${m.n} ⚡` : `Checkpoint · ${LBL} ${m.aulas[st.ai].n}`;
    const id = chkId(st); const prev = S.scored[id];
    app.innerHTML = `<div class="bar"><i style="width:${pct()}%"></i></div>
      <div class="kick">${tit} · pergunta ${st.qi+1}/${isBoss? m.boss.length : m.aulas[st.ai].qs.length}${prev? " · já respondida ✔":""}</div>
      <div class="cardp"><div class="perg">${q[0]}</div>
      <div id="ops">` + q[1].map((a,i) =>
        `<button class="op c${i}${prev ? (i===q[2]?" ok":(i===prev.i?" no":"")) : ""}" ${prev?"disabled":""}
          onclick="resp(${i},${q[2]},this)"><span class="fm">${FM[i]}</span>${a}</button>`).join("") +
      `</div><div id="fb">${prev ? (prev.ok
          ? `<div class="fb ok"><b>✔ Você já respondeu esta pergunta.</b>${q[3]||""}</div>`
          : `<div class="fb no"><b>✘ Já respondida — correta: ${FM[q[2]]} — ${q[1][q[2]]}</b>${q[3]||""}</div>`) : ""}</div></div>
      <div class="nav">${S.step > 0 ? `<button class="btn gh" onclick="passo(-1)">← Voltar: ${rotuloStep(S.step-1)}</button>` : ""}
        <button class="btn" id="nx" style="display:${prev?"inline-block":"none"}" onclick="passo(1)">
        ${proximoRotulo(st)} ▶</button></div>`;
    return;
  }
  if (st.k === "exs"){
    const key = "m"+m.n;
    if (!S.exok[key]) S.exok[key] = [];
    app.innerHTML = topo(`Exercícios do Módulo ${m.n} 🛠`, "Marque ao concluir no laboratório") +
      `<p class="nota">Resolva no VS Code/XAMPP conforme o guia prático do professor. Marque cada item
       ao terminar — seu “visto” fica salvo.</p>` +
      m.exs.map((e,i) => `<div class="exitem"><label>
        <input type="checkbox" ${S.exok[key].includes(i)?"checked":""} onchange="markEx(${i},this.checked)">
        <span><b>${e.ti}</b> <span class="kick">[${e.tp}]</span><div class="en">${e.en}</div></span>
      </label></div>`).join("") +
      navBtns(true, "Encarar o chefe ⚡");
    return;
  }
  if (st.k === "fim"){
    const tot = m.aulas.length;
    S.done["m"+m.n] = tot;
    S.aulas["m"+m.n] = m.aulas.map(a => a.n);
    S.pos = null; save();
    const nx = DATA.mods.find(x => x.n === m.n+1);
    app.innerHTML = `<div class="cardp fimbox"><div class="em">🏆</div>
      <h2 style="color:var(--navy)">Módulo ${m.n} concluído${S.nome ? ", " + primeiroNome() : ""}! 🎉</h2>
      <p><b>${m.ti}</b> · Parte ${m.parte}</p>
      <p class="nota">Pontos acumulados: ⭐ ${S.pts}. Exercícios marcados:
      ${(S.exok["m"+m.n]||[]).length}/${m.exs.length}.</p>
      <div class="nav" style="justify-content:center">
        ${nx ? `<button class="btn amb" onclick="abrirMod(${nx.n})">Próxima fase: Módulo ${nx.n} ▶</button>` :
               `<button class="btn amb" onclick="abrirMod(1)">Recomeçar trilha 🔁</button>`}
        <button class="btn gh" onclick="irHome()">🗺 Trilha</button></div></div>`;
    return;
  }
}
function proximoRotulo(st){
  if (st.k === "boss") return st.qi === mod().boss.length-1 ? "Finalizar fase" : "Próxima";
  const a = mod().aulas[st.ai];
  if (st.qi === a.qs.length-1){
    return st.ai === mod().aulas.length-1 ? "Ir aos exercícios" : "Próxima aula";
  }
  return "Próxima";
}
function markEx(i, v){
  const key = "m"+S.mi; const arr = S.exok[key] || (S.exok[key] = []);
  if (v && !arr.includes(i)) arr.push(i);
  if (!v) S.exok[key] = arr.filter(x => x !== i);
  save();
}
function resp(i, certo, btn){
  const st = S.flow[S.step];
  const id = chkId(st);
  if (S.scored[id]) return;   // pergunta já pontuada antes (evita farmar pontos)
  const ops = document.querySelectorAll("#ops .op");
  ops.forEach((b,k) => { b.disabled = true; if (k === certo) b.classList.add("ok");
    else if (k === i) b.classList.add("no"); });
  const q = st.k === "boss" ? mod().boss[st.qi] : mod().aulas[st.ai].qs[st.qi];
  const fb = document.getElementById("fb");
  const ok = (i === certo);
  S.scored[id] = { i:i, ok:ok };
  if (ok){
    S.pts += 100 + Math.min(S.seq,5)*20; S.seq++;
    fb.className = "fb ok"; fb.innerHTML = `<b>✔ Acertou! +${100 + Math.min(S.seq-1,5)*20} pts</b>${q[3]||""}`;
  } else {
    S.seq = 0;
    fb.className = "fb no";
    fb.innerHTML = `<b>✘ Resposta: ${FM[certo]} — ${q[1][certo]}</b>${q[3]||""}`;
  }
  if (st.k === "chk"){
    const a = mod().aulas[st.ai];
    if (st.qi === a.qs.length - 1){
      const key = "m"+S.mi; const arr = S.aulas[key] || (S.aulas[key] = []);
      if (!arr.includes(a.n)) arr.push(a.n);
    }
  } else if (st.qi === mod().boss.length - 1){
    S.boss["m"+S.mi] = true;
  }
  setHud(); save();
  document.getElementById("nx").style.display = "inline-block";
}
function cardHtml(c){
  if (c.t === "p") return `<p>${c.h}</p>`;
  if (c.t === "h") return `<h3>${c.x}</h3>`;
  if (c.t === "ul") return `<ul>${c.it.map(i=>`<li>${i}</li>`).join("")}</ul>`;
  if (c.t === "ol") return `<ol>${c.it.map(i=>`<li>${i}</li>`).join("")}</ol>`;
  if (c.t === "bx"){
    const ti = c.ti || {con:"Conceito-chave", ana:"Analogia", dica:"Dica", aten:"Atenção"}[c.k];
    return `<div class="bx ${c.k}"><b class="ti">${ti}</b><p>${c.x}</p></div>`;
  }
  if (c.t === "cd") return codeHtml(c);
  if (c.t === "tb") return `<table class="tbl"><tr>${c.cab.map(x=>`<th>${x}</th>`).join("")}</tr>` +
    c.lin.map(r => `<tr>${r.map(x=>`<td>${x}</td>`).join("")}</tr>`).join("") + `</table>`;
  return "";
}
document.addEventListener("keydown", e => {
  if (!S.flow) return;
  const st = S.flow[S.step];
  if ((st.k === "chk" || st.k === "boss")){
    if (["1","2","3","4"].includes(e.key)){
      const b = document.querySelectorAll("#ops .op")[+e.key-1];
      if (b && !b.disabled) b.click();
    }
    if ((e.key === "ArrowRight" || e.key === " ") && document.getElementById("nx").style.display !== "none"){
      passo(1); e.preventDefault();
    }
    return;
  }
  if (st.k === "exs") return;
  if (e.key === "ArrowRight" || e.key === " ") { passo(1); e.preventDefault(); }
  if (e.key === "ArrowLeft") passo(-1);
});
updateNomeBtn();
irHome();
if (!S.nome) abrirModal();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    from conteudo import comuns as _c
    html = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False).replace("<", "\\u003c"))  # evita que </script> do conteúdo feche a tag script
    html = html.replace("__TITULO__", _c.META["titulo_doc"])
    html = html.replace("__KEY__", "aulaviva_" + _c.META["slug"])
    html = html.replace("__LBL__", _c.META.get("aula_label", "Aula"))
    out = os.path.join(_ROOT, "output", f"AulaViva_{comuns.META['slug']}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    na = sum(len(m["aulas"]) for m in DATA["mods"])
    nc = sum(len(a["cards"]) for m in DATA["mods"] for a in m["aulas"])
    nq = sum(len(a["qs"]) for m in DATA["mods"] for a in m["aulas"])
    nb = sum(len(m["boss"]) for m in DATA["mods"])
    print("OK:", out)
    print(f"módulos: {len(DATA['mods'])} | aulas interativas: {na} | cartas: {nc} | "
          f"checkpoints: {nq} | chefes: {nb}")
    print("tamanho:", round(os.path.getsize(out)/1024, 1), "KB")
