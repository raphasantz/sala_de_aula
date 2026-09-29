# -*- coding: utf-8 -*-
"""Gera o APP-AULA interativo v2 (.html único, offline-capable).
Novidades v2: login (nome+senha) com nome único, perfis ADM(Juh)/USUÁRIO,
entrega de arquivos pelo aluno, histórico de respostas p/ correção,
retomada automática, nome completo no topo, botão casa, alternativas
com tags HTML renderizadas como texto (rich-escape).
Modos: offline (__API__ vazio → localStorage) | nuvem (__API__ → API + cookie).
Uso: python3 build_aula_app.py  (CONTEUDO_PKG define a disciplina)
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
        "n": m["num"], "ti": m["titulo"], "parte": ROMAN[m["parte_num"]],
        "parte_ti": m["parte_titulo"], "faixa": m["aulas_faixa"], "obj": m["objetivos"],
        "aulas": aulas,
        "exs": [{"ti": e["titulo"], "tp": e["tipo"], "en": e["enunciado"],
                 "ps": e.get("passos", []), "es": e.get("esperado", ""),
                 "rs": e.get("resolucao", [])} for e in m["exercicios"]],
        "boss": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
                 for q in m["teste_rapido"]],
    })

# ---------------------------------------------------------------------------
# MÍDIA DA TURMA (videoaula + áudios opcionais dos módulos)
# Os arquivos vivem na pasta videoaulas/, IRMÃ do app (apps-offline/ ou
# apps-nuvem/ → ../videoaulas/). O botão só aparece se o arquivo existir no
# kit em tempo de build — nada de botão que leva a lugar nenhum.
# ---------------------------------------------------------------------------
_SLUG = comuns.META["slug"]
_CHAVE = "pi1" if _SLUG.startswith("Programacao") else "lp2"
_MEDIA_DIR = os.path.join(_ROOT, "videoaulas")
_VID = f"Videoaula_{_SLUG}.mp4"
DATA["media"] = {"vid": None, "aud": {}}
_TITULO_MEDIA = ("Programação para Internet I" if _CHAVE == "pi1"
                 else "Linguagem de Programação II")
if os.path.exists(os.path.join(_MEDIA_DIR, _VID)):
    DATA["media"]["vid"] = {"url": f"../videoaulas/{_VID}",
                            "nome": _TITULO_MEDIA}
for _m in DATA["mods"]:
    _fa = os.path.join(_MEDIA_DIR, "audio", f"{_CHAVE}_m{_m['n']:02d}.mp3")
    if os.path.exists(_fa):
        DATA["media"]["aud"][f"m{_m['n']}"] = f"../videoaulas/audio/{_CHAVE}_m{_m['n']:02d}.mp3"

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
 header{background:var(--navy);color:#fff;padding:10px 16px;display:flex;gap:10px;
   align-items:center;justify-content:space-between;position:sticky;top:0;z-index:9;
   box-shadow:0 2px 0 #081b33;flex-wrap:wrap}
 header h1{font-size:18px;cursor:pointer}
 header .dir{display:flex;gap:7px;align-items:center;flex-wrap:wrap}
 .pill{background:var(--amber);color:#3a2700;border:none;border-radius:20px;padding:6px 13px;
   font-weight:800;font-size:12px;cursor:pointer;font-family:inherit;text-decoration:none;display:inline-block}
 .pill.ghost{background:transparent;color:#cfe1f5;border:2px solid #2a527f}
 .wrap{max-width:960px;margin:0 auto;padding:16px 14px 60px}
 body.turma .wrap{max-width:1200px}
 body.turma{font-size:1.22rem}
 body.turma .cardp{padding:34px 30px}
 body.turma .cardp p,body.turma .cardp li{font-size:1.35rem;line-height:1.55}
 body.turma .cardp h3{font-size:1.6rem}
 body.turma .perg{font-size:1.7rem !important}
 body.turma .op{font-size:1.35rem !important;min-height:74px}
 body.turma pre{font-size:1.05rem !important}
 body.turma .resbox ol{font-size:1.25rem}
 body.turma .gab{font-size:1.2rem}
 body.turma .resbtn,body.turma .abtn{font-size:1.05rem}
 body.turma .videocard h3{font-size:1.4rem}
 .bar{height:10px;background:#dfe8f2;border-radius:8px;overflow:hidden;margin:10px 0 16px}
 .bar i{display:block;height:100%;background:linear-gradient(90deg,var(--amber),#ffcf4d);width:0;transition:width .3s}
 .cardp{background:var(--card);border-radius:18px;padding:24px 22px;
   box-shadow:0 3px 14px rgba(13,43,78,.09);animation:pop .25s ease}
 @keyframes pop{from{transform:translateY(8px);opacity:.4}to{transform:none;opacity:1}}
 .kick{font-size:12px;font-weight:800;letter-spacing:.6px;color:var(--amberd);text-transform:uppercase}
 .cardp h2{color:var(--navy);font-size:23px;margin:4px 0 12px}
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
 .pager{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:0 0 14px;
   background:var(--card);border:1px solid #d7e2ee;border-left:5px solid var(--azul);
   border-radius:12px;padding:9px 11px;box-shadow:0 3px 10px rgba(13,43,78,.07)}
 .pgb{background:var(--sky);color:var(--azul);border:none;border-radius:9px;padding:8px 12px;
   font-weight:800;font-size:13px;cursor:pointer;font-family:inherit}
 .pgb:hover:not(:disabled){background:var(--azul);color:#fff}
 .pgb:disabled{opacity:.35;cursor:default}
 .pgb.amb{background:var(--amber);color:#3a2700}
 .pgb.amb:hover{background:#d97706;color:#fff}
 .pglab{font-weight:800;color:var(--navy);font-size:13px}
 .pginp{width:66px;padding:8px 6px;border:2px solid #b9c8d8;border-radius:9px;
   font-weight:800;text-align:center;font-size:14.5px;font-family:inherit;color:var(--navy)}
 .pginp:focus{outline:none;border-color:var(--azul)}
 .pgwhere{flex-basis:100%;color:var(--soft);font-size:12px;font-weight:700;margin-top:2px}
 body.turma .pgb{padding:10px 15px;font-size:15px}
 body.turma .pginp{width:80px;font-size:16px}
 body.turma .pglab{font-size:15px}
 body.turma .pgwhere{font-size:13.5px}
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
 .hud{display:flex;gap:14px;font-weight:800;color:#fff;font-size:15px;align-items:center}
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
 #modal{position:fixed;inset:0;background:rgba(8,20,38,.62);display:flex;align-items:center;
   justify-content:center;z-index:20}
 .mbox{background:#fff;border-radius:18px;padding:24px 22px;max-width:460px;width:94%;
   box-shadow:0 12px 44px rgba(0,0,0,.4);animation:pop .25s ease;max-height:92vh;overflow:auto}
 .mbox h3{color:var(--navy);margin-bottom:4px;font-size:20px}
 .mbox input{width:100%;border:2px solid #d9d4ee;border-radius:10px;padding:11px 13px;
   font-size:15.5px;margin:7px 0;font-family:inherit}
 .mbox input:focus{outline:3px solid #ffd57e;border-color:var(--amber)}
 .tabs{display:flex;gap:8px;margin:8px 0}
 .tabs button{flex:1;border:none;border-radius:10px;padding:10px;font-weight:800;cursor:pointer;
   font-family:inherit;background:#e3ecf7;color:var(--navy);font-size:14px}
 .tabs button.on{background:var(--amber);color:#3a2700}
 .item-arq{display:flex;justify-content:space-between;gap:10px;align-items:center;
   background:#f4f8fc;border:1px solid #dfe8f2;border-radius:10px;padding:10px 12px;margin:8px 0}
 .item-arq a{color:var(--azul);font-weight:700;text-decoration:none}
 .err{background:#fbeae8;border-left:5px solid var(--verm);border-radius:8px;
   padding:8px 12px;font-size:13.5px;color:#8c2418;margin:8px 0}
 .videocard{display:flex;gap:16px;align-items:center;background:linear-gradient(135deg,#143a66,#0d2b4e);
   border-radius:18px;padding:16px 18px;margin:16px 0 6px;cursor:pointer;border:3px solid var(--amber);
   color:#fff;transition:transform .15s}
 .videocard:hover{transform:translateY(-3px)}
 .videocard .play{flex:0 0 58px;height:58px;border-radius:50%;background:var(--amber);color:#3a2700;
   display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900}
 .videocard h3{font-size:17.5px;margin:0 0 3px}
 .videocard .sub{font-size:12.5px;color:#cfe1f5}
 .abtn{border:2px solid #bcd9bd;border-radius:12px;background:#e8f2e6;color:#1e5c33;
   padding:9px 14px;font-weight:800;font-family:inherit;font-size:14px;cursor:pointer;margin:12px 0 2px}
 .abtn:hover{background:#dcebd9}
 .resbtn{border:2px solid #c9dcf2;border-radius:10px;background:#eef4fb;color:#143a66;
   padding:7px 12px;font-weight:800;font-family:inherit;font-size:13px;cursor:pointer;margin-top:9px}
 .resbtn:hover{background:#e0ecfa}
 .resbox{display:none;margin-top:10px;border:2px solid #c9dcf2;border-radius:12px;
   background:#f7fafd;padding:12px 14px}
 .resbox.on{display:block}
 .resbox h4{color:#143a66;font-size:14.5px;margin:10px 0 4px}
 .resbox h4:first-child{margin-top:2px}
 .resbox pre{background:#16202e;color:#e8edf2;border-radius:10px;padding:12px 14px;font-size:13px;
   line-height:1.6;overflow-x:auto;font-family:Consolas,"JetBrains Mono",monospace;margin:6px 0;
   white-space:pre}
 .resbox pre.arv{background:#fdf9ef;color:#5b4a21;border:2px dashed #e4cf9a}
 .resbox ol{margin:6px 0 6px 22px;font-size:14px;color:#374151}
 .resbox ol li{margin:5px 0}
 .gab{background:#eaf6e6;border:2px solid #bcd9bd;border-radius:10px;padding:10px 12px;
   font-size:14px;color:#1e5c33;margin-top:12px}
 .mplayer video{width:100%;border-radius:12px;background:#000}
 .mplayer audio{width:100%}
 @media (max-width:760px){
   header{padding:8px 10px}
   header h1{font-size:15px}
   .pill{padding:5px 9px;font-size:11px}
   .wrap{padding:12px 10px 60px}
   .cardp{padding:16px 14px}
   .cardp h2{font-size:19px}
   .cardp p,.cardp li{font-size:14.5px}
   .perg{font-size:17px}
   .op{font-size:14.5px;min-height:52px;padding:10px 12px 10px 46px}
   .op .fm{font-size:17px;left:12px}
   .codewrap pre{font-size:10.5px}
   .modgrid{grid-template-columns:1fr}
   .mbox{padding:18px 14px}
   .btn{padding:10px 16px;font-size:14px}
   .pager{gap:4px;padding:7px 8px}
   .pgb{padding:7px 8px;font-size:11.5px}
   .pginp{width:52px;padding:7px 3px;font-size:13px}
   .pglab{font-size:11.5px}
   table{display:block;overflow-x:auto}
 }
</style>
</head>
<body>
<header>
  <h1 onclick="irHome()">🎓 AulaViva · __TITULO__</h1>
  <div class="dir">
    <span class="hud" id="hud"></span>
    <span class="pill ghost" id="nuvem" style="display:none">☁️ …</span>
    <button class="pill" id="btArq" style="display:none" onclick="abrirMateriais()">📎 Materiais</button>
    <button class="pill" id="btEnt" style="display:none" onclick="abrirEntregas()">📤 Entregar</button>
    <button class="pill ghost" id="btMapa" style="display:none" onclick="abrirMapa()">🎯 Ir para</button>
    <button class="pill ghost" id="btAluno" onclick="editarConta()">👤 Entrar</button>
    <button class="pill ghost" id="btPainel" style="display:none" onclick="abrirPainel()">👩‍ Painel</button>
    <button class="pill ghost" id="btTurma" onclick="toggleTurma()">📽 Modo Turma</button>
    <button class="pill" onclick="irHome()">🗺 Trilha</button>
  </div>
</header>
<div class="wrap" id="app"></div>
<div id="modal" style="display:none"><div class="mbox" id="mbox"></div></div>
<script>
const DATA = __DATA__;
const API  = "__API__";            // vazio = modo offline
const DISC = "__DISC__";
const LBL  = "__LBL__";
const CLOUD = API !== "";
const FM = ["▲","◆","●","■"];
const app = document.getElementById("app");
const hud = document.getElementById("hud");
let S = { mi:0, step:0, flow:null, pts:0, seq:0, exok:{}, done:{}, boss:{},
          pos:null, aulas:{}, scored:{}, hist:[], nome:"", turma:"" };
const LS = "aulaviva_" + DISC;
if (!CLOUD){ try{ const sv = localStorage.getItem(LS); if (sv) Object.assign(S, JSON.parse(sv)); }catch(e){} }
S.flow = null;

/* ---------- utilidades ---------- */
function rich(s){                      // texto com marcação segura (tags HTML viram texto)
  s = String(s)
    .replace(/&(?!amp;|lt;|gt;|quot;|apos;|nbsp;|#\d+;|#x[0-9a-fA-F]+;)/g, "&amp;")
    .replace(/<(?!\/?(?:b|i|u|br|sub|super|strike)(?:\s[^>]*)?\s*\/?>)/g, "&lt;");
  return s;
}
function esc(s){                       // escape total (para blocos de código <pre>)
  return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}

/* ---------- mídia da turma: videoaula + áudios opcionais ---------- */
function videoCardHtml(){
  const md = DATA.media || {};
  if (!md.vid) return "";
  return `<div class="videocard" onclick="abrirVideo()" role="button" tabindex="0"
    onkeydown="if(event.key==='Enter')abrirVideo()">
    <span class="play">▶</span>
    <div><h3>🎬 Videoaula — ${md.vid.nome}</h3>
    <div class="sub">Assista e acompanhe no seu computador: instalação, banco e projeto
    passo a passo, bem devagar.</div></div></div>`;
}
function abrirVideo(){
  const md = DATA.media || {}; if (!md.vid) return;
  playerModal("🎬 Videoaula — " + md.vid.nome,
    `<video controls preload="metadata" src="${md.vid.url}" onerror="mediaFalhou(this)"></video>
     <p class="nota">O arquivo fica na pasta <b>videoaulas/</b>, ao lado deste app.
     Dá para pausar, voltar e assistir de novo quantas vezes quiser.</p>`);
}
function audioModHtml(m){
  const md = DATA.media || {};
  const u = md.aud && md.aud["m" + m.n];
  if (!u) return "";
  return `<button class="abtn" onclick="abrirAudio('${u}')">🔊 Ouvir o resumo deste módulo (opcional)</button>
    <p class="nota" style="margin-top:4px">Prefere ler? Tudo bem — o áudio é só para quem quiser ouvir.</p>`;
}
function abrirAudio(u){
  playerModal("🔊 Áudio do módulo",
    `<audio controls preload="metadata" src="${u}" onerror="mediaFalhou(this)"></audio>
     <p class="nota">Toque no ▶ para ouvir a aula narrada. Pode fechar quando quiser —
     nada é obrigado.</p>`);
}
function playerModal(tit, inner){
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>${tit}</h3><div class="mplayer">${inner}</div>
    <div class="nav" style="justify-content:flex-end;margin-top:12px">
    <button class="btn gh" onclick="fecharMedia()">Fechar ✖</button></div>`;
  document.getElementById("modal").style.display = "flex";
}
function fecharMedia(){
  document.getElementById("modal").style.display = "none";
  document.getElementById("mbox").innerHTML = "";
}
function mediaFalhou(el){
  if (el.parentNode.querySelector(".err")) return;
  const p = document.createElement("p");
  p.className = "err";
  p.textContent = "Arquivo de mídia não encontrado ao lado do app (pasta videoaulas/). " +
                  "Use o kit atualizado da professora ou abra o arquivo diretamente na pasta.";
  el.parentNode.appendChild(p);
}

/* ---------- resolução passo a passo dos exercícios ---------- */
function resHtml(e){
  let h = "";
  (e.rs || []).forEach(b => {
    if (b.t === "code" || b.t === "pseudo" || b.t === "tree"){
      const tit = b.tit || (b.t === "tree" ? "📁 Estrutura de pastas"
                          : b.t === "pseudo" ? "🧠 Pseudocódigo" : "💻 Código no VB6");
      h += `<h4>${tit}</h4><pre class="${b.t === "tree" ? "arv" : ""}">${esc(b.x)}</pre>`;
    } else if (b.t === "passos"){
      h += `<h4>${b.tit || "🪜 Passo a passo"}</h4><ol>` +
           b.x.map(p => `<li>${rich(p)}</li>`).join("") + `</ol>`;
    } else {
      h += `<p class="nota">${rich(b.x)}</p>`;
    }
  });
  if (e.es) h += `<div class="gab"><b>✅ Gabarito (resposta esperada):</b> ${rich(e.es)}</div>`;
  if (!h) h = `<p class="nota">Resolução em preparação — a professora vai mostrar em aula.</p>`;
  return h;
}
function verRes(i){
  const el = document.getElementById("res" + i);
  if (!el) return;
  el.classList.toggle("on");
  const bt = document.getElementById("resbt" + i);
  if (bt) bt.textContent = el.classList.contains("on")
    ? "🙈 Esconder resolução" : "👀 Ver resolução passo a passo";
}
function save(){
  if (CLOUD){ marcarNuvem(); return; }
  try{ localStorage.setItem(LS, JSON.stringify(payloadS())); }catch(e){}
}
function payloadS(){ return { mi:S.mi, pts:S.pts, seq:S.seq, exok:S.exok, done:S.done,
  boss:S.boss, pos:S.pos, aulas:S.aulas, scored:S.scored, hist:S.hist,
  nome:S.nome, turma:S.turma }; }
function primeiroNome(){ return (S.nome || "").split(" ")[0] || ""; }
function ehADM(){ return /juh/i.test((S.nome || "").trim()); }
function visivelMaterial(x){   // material só da professora (Painel/Guia/Apostila do Professor)
  return ehADM() || !/professor|painel/i.test((x && x.nome) || "");
}
function setHud(){ hud.innerHTML = S.flow || S.nome ? `⭐ ${S.pts}` + (S.seq>=2?` 🔥${S.seq}`:"") : "";
  document.getElementById("btMapa").style.display = S.flow ? "" : "none"; }
function updateChrome(){
  const ba = document.getElementById("btAluno");
  ba.textContent = S.nome ? "👤 " + S.nome : "👤 Entrar";   // nome COMPLETO
  document.getElementById("btArq").style.display = (CLOUD && S.nome) ? "" : "none";
  document.getElementById("btEnt").style.display = (CLOUD && S.nome) ? "" : "none";
  document.getElementById("btPainel").style.display = (CLOUD && ehADM()) ? "" : "none";
  document.getElementById("nuvem").style.display = CLOUD ? "" : "none";
}
function abrirPainel(){ location.href = "__PAINEL__"; }
function toggleTurma(){ document.body.classList.toggle("turma");
  document.getElementById("btTurma").textContent =
    document.body.classList.contains("turma") ? "👤 Modo Aluno" : "📽 Modo Turma"; }

/* ---------- nuvem ---------- */
let pend = false, timerN = null;
function statusNuvem(t){ const el = document.getElementById("nuvem"); if (el) el.textContent = t; }
function marcarNuvem(){ pend = true; if (!timerN) timerN = setTimeout(enviarNuvem, 1200); }
function enviarNuvem(){ timerN = null; if (!pend) return; pend = false;
  api("put", payloadS()).then(() => statusNuvem("☁️ salvo")).catch(() => statusNuvem("☁️ offline")); }
function api(rota, corpo, extra){
  const q = API + "?disc=" + DISC + "&a=" + rota + (extra || "");
  if (corpo !== undefined)
    return fetch(q, { method:"POST", headers:{ "Content-Type":"application/json" },
                      body: JSON.stringify(corpo) }).then(r => {
        if (!r.ok) return r.json().then(j => { throw j; });
        return r.json(); });
  return fetch(q).then(r => { if (!r.ok) return r.json().then(j => { throw j; }); return r.json(); });
}

/* ---------- autenticação ---------- */
let abaAuth = "entrar";
let preNome = "", preTurma = "";   // lembra o nome digitado ao trocar de aba (entrar ⇄ criar)
function modalAuth(msg){
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>👤 ${CLOUD ? "Entrar ou criar conta" : "Identifique-se"}</h3>
   <p class="nota">${CLOUD ? "Seu progresso fica guardado no servidor da escola, protegido por senha."
     : "Modo offline: o progresso fica só neste navegador."}</p>
   ${CLOUD ? `<div class="tabs">
     <button id="tbE" class="${abaAuth==="entrar"?"on":""}" onclick="abaAuth='entrar';modalAuth()">Já tenho conta</button>
     <button id="tbC" class="${abaAuth==="criar"?"on":""}" onclick="abaAuth='criar';modalAuth()">Criar conta</button>
   </div>` : ""}
   <label style="font-size:13px;font-weight:700;color:var(--navy)">Nome completo *</label>
   <input id="inNome" maxlength="40" placeholder="Seu nome completo"
     value="${preNome.replace(/"/g,"&quot;")}"
     oninput="if(this.dataset.t) checkNome(this.value)">
   <label style="font-size:13px;font-weight:700;color:var(--navy)">Turma (opcional)</label>
   <input id="inTurma" maxlength="20" placeholder="ex.: 2/2026"
     value="${preTurma.replace(/"/g,"&quot;")}">
   ${CLOUD ? `<label style="font-size:13px;font-weight:700;color:var(--navy)">Senha *
     <span style="font-weight:400">(crie uma só sua)</span></label>
   <input id="inSenha" type="password" maxlength="30" placeholder="senha">
   <input id="inSenha2" type="password" maxlength="30" placeholder="repita a senha"
     style="display:${abaAuth==="criar"?"block":"none"}">
   <div id="chkNome" class="nota"></div>` : ""}
   <div id="authErr" class="err" style="display:none"></div>
   <div class="nav">
     <button class="btn amb" onclick="submitAuth()">${CLOUD ? (abaAuth==="criar" ? "Criar e jogar ✔" : "Entrar ▶") : "Salvar e jogar ✔"}</button>
   </div>
   ${msg ? `<div class="err">${msg}</div>` : ""}`;
  if (CLOUD && abaAuth === "criar") document.getElementById("inNome").dataset.t = "1";
  document.getElementById("modal").style.display = "flex";
  setTimeout(() => document.getElementById("inNome").focus(), 60);
}
function checkNome(v){
  const el = document.getElementById("chkNome");
  v = v.trim(); if (v.length < 3){ el.textContent = ""; return; }
  api("check", undefined, "&nome=" + encodeURIComponent(v))
    .then(j => { el.innerHTML = j.existe
        ? "<span style='color:#c0392b;font-weight:700'>✗ Este nome já existe — use “Já tenho conta”.</span>"
        : "<span style='color:#1e7b34;font-weight:700'>✔ Nome disponível.</span>"; })
    .catch(() => { el.textContent = ""; });
}
function submitAuth(){
  const nome = document.getElementById("inNome").value.trim();
  const turma = document.getElementById("inTurma").value.trim();
  const err = document.getElementById("authErr");
  err.style.display = "none";
  if (nome.length < 3){ err.textContent = "Digite seu nome completo."; err.style.display = "block"; return; }
  if (!CLOUD){ S.nome = nome; S.turma = turma; save(); finishBoot(); return; }
  const senha = document.getElementById("inSenha").value;
  if (senha.length < 4){ err.textContent = "A senha precisa de pelo menos 4 caracteres."; err.style.display = "block"; return; }
  if (abaAuth === "criar"){
    const s2 = document.getElementById("inSenha2").value;
    if (s2 !== senha){ err.textContent = "As senhas não conferem."; err.style.display = "block"; return; }
    api("reg", { nome, turma, senha })
      .then(j => { S.nome = nome; S.turma = turma;
                   if (j && j.payload) Object.assign(S, j.payload);
                   finishBoot(); })
      .catch(j => { err.textContent = (j && j.erro === "nome")
          ? "Este nome já está cadastrado. Use a aba “Já tenho conta”." : "Falha ao criar conta.";
        err.style.display = "block"; });
  } else {
    api("login", { nome, senha })
      .then(j => { S.nome = j.nome || nome; S.turma = j.turma || turma;
                   if (j.payload) Object.assign(S, j.payload);
                   finishBoot(); })
      .catch(() => {   // primeira vez? um clique leva pra criar conta sem perder o nome digitado
        preNome = nome; preTurma = turma;
        err.textContent = "Nome ou senha incorretos. Se é sua primeira vez aqui, crie sua conta em 10 segundos:";
        err.style.display = "block";
        const b = document.createElement("button");
        b.className = "btn gh"; b.style.marginTop = "8px";
        b.textContent = "🆕 É minha primeira vez — criar conta";
        b.onclick = () => { abaAuth = "criar"; modalAuth(); };
        err.appendChild(b); });
  }
}
function editarConta(){
  if (!S.nome) return modalAuth();
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>👤 ${S.nome}</h3>
    <p class="nota">Turma: ${S.turma || "—"} · ⭐ ${S.pts} pts · ${ehADM() ? "perfil ADM" : "perfil aluno"}</p>
    <div class="nav" style="flex-direction:column;align-items:stretch">
      <button class="btn gh" onclick="fecharModal(); abrirMinhas()">📤 Minhas entregas</button>
      <button class="btn gh" onclick="fecharModal(); abrirMateriais()">📎 Materiais da turma</button>
      ${CLOUD ? `<button class="btn gh" onclick="trocarConta()">🔄 Trocar de conta / sair</button>` : ""}
    </div>`;
  document.getElementById("modal").style.display = "flex";
}
function trocarConta(){
  fecharModal();
  preNome = ""; preTurma = "";
  api("logout", {}).catch(()=>{});
  S = { mi:0, step:0, flow:null, pts:0, seq:0, exok:{}, done:{}, boss:{},
        pos:null, aulas:{}, scored:{}, hist:[], nome:"", turma:"" };
  updateChrome(); setHud(); modalAuth();
}
function fecharModal(){ document.getElementById("modal").style.display = "none"; }

/* ---------- boot ---------- */
function finishBoot(){
  document.getElementById("modal").style.display = "none";
  updateChrome(); setHud();
  if (CLOUD){
    statusNuvem("☁️ …");
    api("get").then(j => {
      if (j && j.payload && typeof j.payload.pts === "number" && !S.pts){
        Object.assign(S, j.payload);
      }
      statusNuvem("☁️ sincronizado");
      retomar();
    }).catch(() => { statusNuvem("☁️ offline"); retomar(); });
  } else retomar();
}
function retomar(){
  updateChrome(); setHud();
  if (S.pos){ abrirMod(S.pos.mi, S.pos.step); }   // volta DIRETO de onde parou
  else irHome();
}
function boot(){
  updateChrome();
  if (CLOUD){
    api("get").then(j => {
      if (j && j.nome){ S.nome = j.nome; S.turma = j.turma || "";
        if (j.payload) Object.assign(S, j.payload);
        finishBoot(); }
      else modalAuth();
    }).catch(() => { statusNuvem("☁️ offline"); modalAuth(); });
  } else {
    if (S.nome) finishBoot(); else modalAuth();
  }
}

/* ---------- entregas de arquivos do aluno ---------- */
function abrirEntregas(){
  if (!S.nome) return modalAuth();
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>📤 Entregar atividade</h3>
    <p class="nota">Anexe seu arquivo (txt, doc, docx, pdf) — ele fica ligado ao seu nome para
    a professora corrigir depois.</p>
    <input type="file" id="inFile" accept=".txt,.doc,.docx,.pdf,.odt">
    <div id="entErr" class="err" style="display:none"></div>
    <div class="nav"><button class="btn amb" onclick="enviarEntrega()">Enviar ✔</button>
    <button class="btn gh" onclick="abrirMinhas()">Minhas entregas</button></div>
    <div id="entSt" class="nota"></div>`;
  document.getElementById("modal").style.display = "flex";
}
function enviarEntrega(){
  const f = document.getElementById("inFile").files[0];
  const err = document.getElementById("entErr");
  err.style.display = "none";
  if (!f){ err.textContent = "Escolha um arquivo antes."; err.style.display = "block"; return; }
  if (f.size > 12 * 1024 * 1024){ err.textContent = "Arquivo maior que 12 MB."; err.style.display = "block"; return; }
  document.getElementById("entSt").textContent = "Enviando " + f.name + " …";
  const r = new FileReader();
  r.onload = () => {
    api("entrega", { nome: f.name, base64: String(r.result).split(",")[1], tipo: f.type })
      .then(() => { document.getElementById("entSt").textContent = "✔ Entregue com sucesso!"; abrirMinhas(); })
      .catch(() => { err.textContent = "Falha no envio — tente de novo."; err.style.display = "block"; });
  };
  r.readAsDataURL(f);
}
function abrirMinhas(){
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>📤 Minhas entregas</h3><div id="minhasLista" class="nota">carregando…</div>
    <div class="nav"><button class="btn gh" onclick="fecharModal()">Fechar</button></div>`;
  document.getElementById("modal").style.display = "flex";
  api("minhas").then(xs => {
    document.getElementById("minhasLista").innerHTML = (xs && xs.length)
      ? xs.map(x => `<div class="item-arq"><span>📄 ${x.nome}</span>
          <span class="nota">${(x.atualizado||"").slice(0,10)}</span></div>`).join("")
      : "<p class='nota'>Nenhuma entrega ainda.</p>";
  }).catch(() => { document.getElementById("minhasLista").innerHTML =
      "<p class='nota'>Offline no momento.</p>"; });
}

/* ---------- materiais ---------- */
function abrirMateriais(){
  S.flow = null; setHud(); updateChrome();
  app.innerHTML = `<div class="cardp"><h2>📎 Materiais da turma</h2>
    <p style="margin:6px 0 12px">Documentos enviados pela professora: apostilas, listas, slides.</p>
    <div id="listaArq"><p class="nota">carregando…</p></div>
    <div class="nav"><button class="btn gh" onclick="irHome()">← Voltar à trilha</button></div></div>`;
  api("arq").then(xs => {
    const el = document.getElementById("listaArq");
    if (xs) xs = xs.filter(visivelMaterial);  // a partir do login, some o que é só da professora
    if (!xs || !xs.length){ el.innerHTML = "<p class='nota'>Nenhum material enviado ainda.</p>"; return; }
    el.innerHTML = xs.map(x => `<div class="item-arq"><a href="${x.url}" target="_blank" download>⬇ ${x.nome}</a>
      <span class="nota">${x.tamanho ? Math.max(1, Math.round(x.tamanho/1024)) + " KB" : ""} ·
      ${(x.atualizado||"").slice(0,10)}</span></div>`).join("");
  }).catch(() => { document.getElementById("listaArq").innerHTML =
      "<p class='nota'>Offline no momento.</p>"; });
}

/* ---------- trilha / fluxo ---------- */
function irHome(){ S.flow = null; setHud(); updateChrome(); renderHome(); }
function renderHome(){
  let h = S.nome
    ? `<h2 style="color:var(--navy);margin:6px 0 4px">Olá, ${S.nome}! 👋</h2>
       <div class="kick">Trilha do semestre${S.turma ? " · Turma " + S.turma : ""} · seus pontos: ⭐ ${S.pts}</div>`
    : `<h2 style="color:var(--navy);margin:6px 0 4px">Trilha do semestre</h2>`;
  h += `<p class="nota">Cada módulo é uma fase: cartas de aula com checkpoints ✅, exercícios 🛠 e o
   <b>chefe do módulo</b> ⚡. ${CLOUD ? "Seu progresso vive na nuvem da escola." :
   "Seu progresso fica neste navegador."}</p>
   ${videoCardHtml()}
   <div class="modgrid" style="margin-top:14px">`;
  for (const m of DATA.mods){
    const d = (S.aulas["m"+m.n] || []).length;
    const tot = m.aulas.length;
    const st = S.done["m"+m.n] ? "🏆" : d > 0 ? "⭐" : "📘";
    h += `<div class="modcard" onclick="abrirMod(${m.n})">
      <span class="st">${st}</span>
      <div class="kick">Módulo ${m.n} · Parte ${m.parte}</div>
      <h3>${m.ti}</h3>
      <div class="sub">${m.faixa} · ${tot} aulas interativas · ${qtdPaginas(m)} páginas</div>
      <div class="prog">${d}/${tot} aulas concluídas</div>
      <div class="mini"><i style="width:${tot? Math.round(100*d/tot):0}%"></i></div>
    </div>`;
  }
  app.innerHTML = h + "</div>";
}
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
  const alvo = (step !== undefined) ? step : ((S.pos && S.pos.mi === n) ? S.pos.step : 0);
  S.step = Math.max(0, Math.min(S.flow.length - 1, alvo));
  S.pos = { mi:n, step:S.step };
  save(); setHud(); updateChrome(); renderStep();
}
function mod(){ return DATA.mods.find(x => x.n === S.mi); }
function continuar(){ if (S.pos) abrirMod(S.pos.mi, S.pos.step); }
function chkId(st){ return "m"+S.mi + (st.k === "boss" ? ":b"+st.qi : ":a"+st.ai+":q"+st.qi); }
function pct(){ return Math.round(100 * S.step / (S.flow.length - 1)); }
function qtdPaginas(m){                       // total de páginas de um módulo
  let n = 3 + m.boss.length;                  // abertura + exercícios + finalização + chefe
  m.aulas.forEach(a => { n += a.cards.length + a.qs.length; });
  return n;
}
function paginador(){                         // barra: início/voltar/nº/próximo/fim
  if (!S.flow) return "";
  const y = S.flow.length, x = S.step + 1;
  return `<div class="pager" role="navigation" aria-label="Páginas do módulo">
    <button class="pgb" onclick="irPara(0)" title="Ir para a página 1" ${x<=1?"disabled":""}>⏮ Início</button>
    <button class="pgb" onclick="passo(-1)" title="Página anterior" ${x<=1?"disabled":""}>◀ Voltar</button>
    <span class="pglab"><label for="pginp">Página</label></span>
    <input id="pginp" class="pginp" type="number" min="1" max="${y}" value="${x}" step="1"
      inputmode="numeric" aria-label="Número da página desejada"
      onkeydown="if(event.key==='Enter'){irPagina();event.preventDefault();}">
    <span class="pglab">de ${y}</span>
    <button class="pgb amb" onclick="irPagina()" title="Ir para a página digitada">Ir</button>
    <button class="pgb" onclick="passo(1)" title="Próxima página" ${x>=y?"disabled":""}>Próximo ▶</button>
    <button class="pgb" onclick="irPara(S.flow.length-1)" title="Ir para a última página" ${x>=y?"disabled":""}>⏭ Fim</button>
    <span class="pgwhere">📖 ${stepLabel()}</span>
  </div>`;
}
function irPagina(){                          // salto pelo número digitado
  const el = document.getElementById("pginp"); if (!el) return;
  const v = parseInt(el.value, 10); if (isNaN(v)) return;
  irPara(Math.max(1, Math.min(S.flow.length, v)) - 1);
}
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
function stepLabel(){ return rotuloStep(S.step); }
function topo(tit, kick){
  return `<div class="bar"><i style="width:${pct()}%"></i></div>` + paginador() +
    `<div class="kick">${kick}</div><div class="cardp"><h2>${tit}</h2>`;
}
function navBtns(volt, rotulo){
  const volta = (volt && S.step > 0)
    ? `<button class="btn gh" onclick="passo(-1)">← Voltar: ${rotuloStep(S.step-1)}</button>` : "";
  return `</div><div class="nav">${volta}
    <button class="btn" onclick="passo(1)">${rotulo||"Continuar →"}</button></div>`;
}
function passo(d){ S.step = Math.max(0, Math.min(S.flow.length-1, S.step+d));
  S.pos = { mi:S.mi, step:S.step }; save(); renderStep(); }
function chip(i, txt){ return `<button class="btn gh" style="margin:3px 5px 3px 0;padding:8px 13px;
  font-size:13px" onclick="irPara(${i})">${txt}</button>`; }
function irPara(i){ S.step = Math.max(0, Math.min(S.flow.length-1, i));
  S.pos = { mi:S.mi, step:S.step }; save(); fecharMapa(); renderStep(); }
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
  const mb = document.getElementById("mbox");
  mb.innerHTML = `<h3>🎯 Ir diretamente para… <span class="kick" style="text-transform:none">página ${S.step+1} de ${S.flow.length}</span></h3>
    <div style="max-height:55vh;overflow:auto;padding:4px 0">${h}</div>
    <div class="nav"><button class="btn gh" onclick="fecharMapa()">Fechar</button>
      <button class="btn gh" onclick="irPara(0)">⏮ Início</button>
      <button class="btn gh" onclick="irPara(S.flow.length-1)">⏭ Fim</button></div>`;
  document.getElementById("modal").style.display = "flex";
}
function fecharMapa(){ document.getElementById("modal").style.display = "none"; }

function renderStep(){
  const st = S.flow[S.step];
  const m = mod();
  window.scrollTo(0,0);
  if (st.k === "intro"){
    app.innerHTML = topo(`Módulo ${m.n} — ${m.ti}`, `Parte ${m.parte} · ${m.faixa}`) +
      `<p><b>${m.parte_ti}.</b> Nesta fase você vai viver ${m.aulas.length} aulas interativas.</p>
       <h3>🎯 Objetivos da fase</h3><ul>` +
      m.obj.map(o => `<li>${rich(o)}</li>`).join("") + `</ul>
       <p class="nota">Cada <b>carta</b> traz um pedaço da aula; no fim, <b>checkpoints</b> que valem
       pontos (⭐) e sequência (🔥). Setas do teclado também avançam.</p>` +
      audioModHtml(m) +
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
    app.innerHTML = `<div class="bar"><i style="width:${pct()}%"></i></div>` + paginador() + `
      <div class="kick">${tit} · pergunta ${st.qi+1}/${isBoss? m.boss.length : m.aulas[st.ai].qs.length}${prev? " · já respondida ✔":""}</div>
      <div class="cardp"><div class="perg">${rich(q[0])}</div>
      <div id="ops">` + q[1].map((a,i) =>
        `<button class="op c${i}${prev ? (i===q[2]?" ok":(i===prev.i?" no":"")) : ""}" ${prev?"disabled":""}
          onclick="resp(${i},${q[2]},this)"><span class="fm">${FM[i]}</span>${rich(a)}</button>`).join("") +
      `</div><div id="fb">${prev ? (prev.ok
          ? `<div class="fb ok"><b>✔ Você já respondeu esta pergunta.</b>${rich(q[3]||"")}</div>`
          : `<div class="fb no"><b>✘ Já respondida — correta: ${FM[q[2]]} — ${rich(q[1][q[2]])}</b>${rich(q[3]||"")}</div>`) : ""}</div></div>
      <div class="nav">${S.step > 0 ? `<button class="btn gh" onclick="passo(-1)">← Voltar: ${rotuloStep(S.step-1)}</button>` : ""}
        <button class="btn" id="nx" style="display:${prev?"inline-block":"none"}" onclick="passo(1)">
        ${proximoRotulo(st)} ▶</button></div>`;
    return;
  }
  if (st.k === "exs"){
    const key = "m"+m.n;
    if (!S.exok[key]) S.exok[key] = [];
    app.innerHTML = topo(`Exercícios do Módulo ${m.n} 🛠`, "Marque ao concluir no laboratório") +
      `<p class="nota">Resolva no ambiente da disciplina e marque cada item ao terminar —
       seu “visto” fica salvo${CLOUD ? " no servidor" : ""}.</p>
       <p class="nota" style="background:#eef4fb;border:2px solid #c9dcf2;border-radius:10px;
       padding:9px 12px;color:#143a66">📽 <b>Sem laboratório hoje?</b> Cada exercício tem o botão
       <b>👀 Ver resolução passo a passo</b>: é a demonstração completinha na tela, para a turma
       acompanhar no projetor (ou estudar em casa).</p>` +
      m.exs.map((e,i) => `<div class="exitem"><label>
        <input type="checkbox" ${S.exok[key].includes(i)?"checked":""} onchange="markEx(${i},this.checked)">
        <span><b>${rich(e.ti)}</b> <span class="kick">[${e.tp}]</span><div class="en">${rich(e.en)}</div></span>
      </label>
      <div style="padding:0 15px 13px 47px">
        <button class="resbtn" id="resbt${i}" onclick="verRes(${i})">👀 Ver resolução passo a passo</button>
        <div class="resbox" id="res${i}">${resHtml(e)}</div>
      </div></div>`).join("") +
      navBtns(true, "Encarar o chefe ⚡");
    return;
  }
  if (st.k === "fim"){
    S.done["m"+m.n] = m.aulas.length;
    S.aulas["m"+m.n] = m.aulas.map(a => a.n);
    S.pos = null; save();
    const nx = DATA.mods.find(x => x.n === m.n+1);
    app.innerHTML = paginador() + `<div class="cardp fimbox"><div class="em">🏆</div>
      <h2 style="color:var(--navy)">Módulo ${m.n} concluído${S.nome ? ", " + primeiroNome() : ""}! 🎉</h2>
      <p><b>${m.ti}</b> · Parte ${m.parte}</p>
      <p class="nota">Pontos: ⭐ ${S.pts} · Exercícios marcados: ${(S.exok["m"+m.n]||[]).length}/${m.exs.length}.</p>
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
  if (S.scored[id]) return;
  const ops = document.querySelectorAll("#ops .op");
  ops.forEach((b,k) => { b.disabled = true; if (k === certo) b.classList.add("ok");
    else if (k === i) b.classList.add("no"); });
  const q = st.k === "boss" ? mod().boss[st.qi] : mod().aulas[st.ai].qs[st.qi];
  const fb = document.getElementById("fb");
  const ok = (i === certo);
  S.scored[id] = { i:i, ok:ok };
  S.hist = S.hist || [];
  S.hist.push({ t: st.k, mod: S.mi, aula: st.k === "boss" ? "chefe" : mod().aulas[st.ai].n,
                q: st.qi+1, perg: q[0].replace(/<[^>]+>/g,"").slice(0,90),
                esc: i, ok: ok, ts: new Date().toISOString().slice(0,16).replace("T"," ") });
  if (S.hist.length > 600) S.hist = S.hist.slice(-600);
  if (ok){
    S.pts += 100 + Math.min(S.seq,5)*20; S.seq++;
    fb.className = "fb ok"; fb.innerHTML = `<b>✔ Acertou! +${100 + Math.min(S.seq-1,5)*20} pts</b>${rich(q[3]||"")}`;
  } else {
    S.seq = 0;
    fb.className = "fb no";
    fb.innerHTML = `<b>✘ Resposta: ${FM[certo]} — ${rich(q[1][certo])}</b>${rich(q[3]||"")}`;
  }
  if (st.k === "chk"){
    const a = mod().aulas[st.ai];
    if (st.qi === a.qs.length-1){
      const key = "m"+S.mi; const arr = S.aulas[key] || (S.aulas[key] = []);
      if (!arr.includes(a.n)) arr.push(a.n);
    }
  } else if (st.qi === mod().boss.length-1){
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
/* ---------- realce de código ---------- */
const KW = /(echo|print|if|else|elseif|endif|for|endforeach|foreach|while|do|switch|case|break|default|function|return|true|false|null|exit|die|include|require|include_once|require_once|define|as|new|isset|empty)\b/;
function hiLine(line, lg){
  if (lg === "html") return hiHtml(line);
  if (lg === "vb") return hiVb(line);
  if (lg === "sql") return hiSql(line);
  if (lg === "shell" || lg === "texto"){
    const i = line.indexOf("#");
    if (lg === "shell" && i >= 0) return [["", line.slice(0,i)], ["c", line.slice(i)]];
    return [["", line]];
  }
  const ci = line.indexOf("//");
  let code = line, com = null;
  if (ci >= 0){ code = line.slice(0, ci); com = line.slice(ci); }
  const out = [];
  const re = /("[^"]*"|'[^']*')|(<\?php\b|<\?=|\?>)|(<\/?[A-Za-z][^>]*>)|(\$[A-Za-z_]\w*)|\b([A-Za-z_]\w*)(?=\s*\()/g;
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
  const res = []; const r2 = new RegExp(KW.source, "g"); let last = 0, m;
  while ((m = r2.exec(txt))){
    if (m.index > last) res.push(["", txt.slice(last, m.index)]);
    res.push(["k", m[0]]); last = r2.lastIndex;
  }
  if (last < txt.length) res.push(["", txt.slice(last)]);
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
function hiHtml(line){
  const res=[]; let re=/(<\/?[A-Za-z][^>]*>)|("[^"]*")/g, last=0, m;
  while ((m=re.exec(line))){
    if (m.index>last) res.push(["", line.slice(last,m.index)]);
    res.push(m[1] ? ["t", m[1]] : ["s", m[2]]); last=re.lastIndex;
  }
  if (last<line.length) res.push(["", line.slice(last)]);
  return res;
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
document.addEventListener("keydown", e => {
  if (!S.flow || document.getElementById("modal").style.display === "flex") return;
  // com o cursor num campo (ex.: página desejada), as setas/teclas são do campo
  if (e.target && (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA" || e.target.isContentEditable)) return;
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
boot();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    slug = comuns.META["slug"]
    html = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False).replace("<", "\\u003c"))
    html = html.replace("__TITULO__", comuns.META["titulo_doc"])
    html = html.replace("__LBL__", comuns.META.get("aula_label", "Aula"))
    # FIX: slug começa maiúsculo ("Linguagem_...") — comparar em minúsculas,
    # senão LP2 virava "pi1" e sincronizava na disciplina errada.
    disc = "lp2" if "linguagem" in slug.lower() else "pi1"
    # base com placeholders (deploy builders injetam API/PAINEL)
    base_dir = os.path.join(_HERE, "_base"); os.makedirs(base_dir, exist_ok=True)
    with open(os.path.join(base_dir, f"AulaViva_{slug}.BASE.html"), "w", encoding="utf-8") as f:
        f.write(html.replace("__DISC__", disc))
    # versão OFFLINE (sem API): mantém comportamento local
    off = (html.replace('"__API__"', '""')
               .replace("__DISC__", disc)
               .replace('"__PAINEL__"', '"prof.html"'))  # botão fica oculto offline
    out = os.path.join(_ROOT, "output", f"AulaViva_{slug}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(off)
    na = sum(len(m["aulas"]) for m in DATA["mods"])
    nc = sum(len(a["cards"]) for m in DATA["mods"] for a in m["aulas"])
    nq = sum(len(a["qs"]) for m in DATA["mods"] for a in m["aulas"])
    print("OK:", out, "| aulas:", na, "| cartas:", nc, "| checkpoints:", nq)
