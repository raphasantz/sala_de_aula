# -*- coding: utf-8 -*-
"""Gera o APP DE QUIZ offline (HTML único) — Programação para Internet I.
Modos: Solo (aluno) e Turma (projetor + equipes). Conteúdo:
  • 72 aulas × 3 questões (quizzes_aulas.py)
  • Testes rápidos dos 12 módulos (conteúdo da apostila)
  • Questões objetivas dos modelos de prova A1/A2/A3
Uso: python3 build_quiz_app.py
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
MODULOS_POR_NUM = _PKG.MODULOS_POR_NUM
QA = _PKG.quizzes
avaliacoes = _PKG.avaliacoes
comuns = _PKG.comuns

# ---------------------------------------------------------------------------
# MONTAGEM DOS DADOS
# ---------------------------------------------------------------------------
MODULO_DA_AULA = {}
for m in MODULOS:
    for a in m["aulas"]:
        MODULO_DA_AULA[a["num"]] = m["num"]
# aulas que não têm teoria própria (agrupadas) herdam o módulo da aula-âncora
for alias, base in QA.ALIASES.items():
    MODULO_DA_AULA.setdefault(alias, MODULO_DA_AULA.get(base, 12))

aulas = []
for n in range(1, max(QA.TITULOS_AULAS) + 1):
    base = QA.ALIASES.get(n, n)
    qs = QA.Q[base]
    titulo = QA.TITULOS_AULAS.get(n) or QA.TITULOS_AULAS.get(base, f"Aula {n}")
    aulas.append({
        "n": n,
        "mod": MODULO_DA_AULA.get(n, MODULOS[-1]["num"]),
        "t": titulo,
        "qs": [[q[0], q[1], q[2], q[3]] for q in qs],
    })

modulos = []
for m in MODULOS:
    modulos.append({
        "n": m["num"],
        "t": m["titulo"],
        "qs": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
               for q in m["teste_rapido"]],
    })

provas = []
provas.append({"id": "A1", "t": "Modelo A1 — Parte A (Web e HTML)",
               "qs": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
                      for q in avaliacoes.A1["teste"]["parte_a"]["questoes"]]})
provas.append({"id": "A2", "t": "Modelo A2 — conceituais",
               "qs": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
                      for q in avaliacoes.A2["teste"]["questoes"] if q["tipo"] == "objetiva"]})
provas.append({"id": "A3", "t": "Modelo A3 — conceituais",
               "qs": [[q["enunciado"], q["alt"], q["resposta"], q.get("comentario", "")]
                      for q in avaliacoes.A3["teste"]["questoes"] if q["tipo"] == "objetiva"]})

DATA = {"aulas": aulas, "modulos": modulos, "provas": provas}

HTML = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QuizWeb — __TITULO__</title>
<style>
  :root{
    --roxo:#46178f; --roxo2:#33106b; --fundo:#f2f2f9;
    --verm:#e21b3c; --azul:#1368ce; --amar:#ffa602; --verde:#26890c;
    --tinta:#201a35; --cinza:#6b6880; --branco:#fff;
  }
  *{box-sizing:border-box; margin:0; padding:0; -webkit-tap-highlight-color:transparent}
  body{font-family:"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;
       background:var(--fundo); color:var(--tinta); min-height:100vh}
  .wrap{max-width:1000px; margin:0 auto; padding:18px 16px 40px}
  header.topo{background:var(--roxo); color:#fff; padding:16px 0 14px; text-align:center;
              box-shadow:0 3px 0 var(--roxo2)}
  header.topo h1{font-size:26px; letter-spacing:.5px}
  header.topo p{font-size:12.5px; opacity:.85; margin-top:2px}
  .card{background:#fff; border-radius:14px; padding:18px; box-shadow:0 2px 10px rgba(30,20,80,.08);
        margin-top:16px}
  h2.sec{font-size:19px; color:var(--roxo); margin:22px 4px 10px}
  .grid-modos{display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:14px; margin-top:16px}
  .modo{border:none; border-radius:16px; padding:22px 18px; text-align:left; color:#fff; cursor:pointer;
        font-family:inherit; transition:transform .12s}
  .modo:hover{transform:translateY(-3px)}
  .modo h3{font-size:20px; margin-bottom:6px}
  .modo p{font-size:13px; opacity:.92; line-height:1.45}
  .modo.solo{background:linear-gradient(135deg,#7a2ff0,#46178f)}
  .modo.turma{background:linear-gradient(135deg,#e21b3c,#a3122b)}
  .modo.lista{background:linear-gradient(135deg,#1368ce,#0b4a94)}
  .linha{display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin:8px 0}
  .btn{border:none; border-radius:10px; padding:11px 20px; font-size:15px; font-weight:700;
       cursor:pointer; font-family:inherit; background:var(--roxo); color:#fff}
  .btn.secund{background:#e7e2f7; color:var(--roxo)}
  .btn.verde{background:var(--verde)}
  .btn.amarelo{background:var(--amar); color:#3a2700}
  .btn:disabled{opacity:.45; cursor:default}
  .item-lista{display:flex; justify-content:space-between; gap:10px; align-items:center;
              background:#fff; border:2px solid #eceaf6; border-radius:12px; padding:11px 14px;
              margin:7px 0; cursor:pointer; transition:border-color .12s}
  .item-lista:hover{border-color:var(--roxo)}
  .item-lista .tt{font-weight:700; font-size:14.5px}
  .item-lista .sub{font-size:12px; color:var(--cinza)}
  .badge{background:var(--roxo); color:#fff; font-size:11px; font-weight:700; border-radius:20px;
         padding:3px 10px; white-space:nowrap}
  .badge.rec{background:var(--verde)}
  /* ---- quiz ---- */
  .barra-topo{display:flex; justify-content:space-between; align-items:center; margin:14px 2px 10px;
              font-size:13.5px; font-weight:700; color:var(--cinza)}
  .timerbox{background:var(--roxo); color:#fff; border-radius:10px; padding:5px 14px; font-size:16px}
  .timerbar{height:8px; background:#e3e0f0; border-radius:6px; overflow:hidden; margin:6px 0 14px}
  .timerbar i{display:block; height:100%; background:var(--amar); width:100%; transition:width .25s linear}
  .pergunta{background:#fff; border-radius:16px; padding:22px 20px; font-size:21px; font-weight:700;
            line-height:1.35; box-shadow:0 2px 10px rgba(30,20,80,.08); min-height:96px}
  .opcoes{display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:14px}
  @media(max-width:720px){.opcoes{grid-template-columns:1fr}}
  .op{border:none; border-radius:12px; padding:16px 16px 16px 58px; position:relative; color:#fff;
      font-size:16.5px; font-weight:600; text-align:left; cursor:pointer; font-family:inherit;
      line-height:1.3; min-height:64px}
  .op .forma{position:absolute; left:16px; top:50%; transform:translateY(-50%); font-size:24px}
  .op.c0{background:var(--verm)} .op.c1{background:var(--azul)}
  .op.c2{background:var(--amar); color:#3a2700} .op.c3{background:var(--verde)}
  .op:disabled{cursor:default}
  .op.certa{outline:5px solid #0e5c00; outline-offset:-5px}
  .op.errada{outline:5px solid #7d0018; outline-offset:-5px; opacity:.85}
  .feedback{border-radius:14px; padding:16px 18px; margin-top:14px; color:#fff; font-size:15.5px}
  .feedback.ok{background:var(--verde)} .feedback.erro{background:var(--verm)}
  .feedback b{display:block; font-size:18px; margin-bottom:4px}
  .placar{display:flex; gap:16px; font-weight:800; font-size:15px; color:var(--roxo)}
  /* ---- turma ---- */
  .turma .pergunta{font-size:30px; padding:30px 26px}
  .turma .op{font-size:22px; min-height:84px; padding-left:66px}
  .turma .op .forma{font-size:30px}
  .times{display:flex; gap:10px; flex-wrap:wrap; margin-top:12px}
  .time{background:#fff; border:3px solid var(--roxo); color:var(--roxo); border-radius:12px;
        padding:8px 16px; font-weight:800; cursor:pointer; font-size:16px; font-family:inherit}
  .time span{background:var(--roxo); color:#fff; border-radius:16px; padding:1px 10px; margin-left:8px}
  .time.lead{background:var(--amar); border-color:#b57500; color:#3a2700}
  .time.lead span{background:#3a2700}
  input[type=text]{width:100%; border:2px solid #d9d4ee; border-radius:10px; padding:11px 13px;
                   font-size:15px; font-family:inherit}
  .nota{font-size:12.5px; color:var(--cinza); margin-top:8px; line-height:1.5}
  .podio{ text-align:center; padding:10px 0 4px }
  .podio .p1{font-size:34px}
  .rev{background:#fff; border-radius:10px; padding:10px 13px; margin:7px 0; font-size:13.5px;
       border-left:6px solid #ccc}
  .rev.ok{border-color:var(--verde)} .rev.erro{border-color:var(--verm)}
  .rev b{font-size:14px}
  footer{ text-align:center; font-size:11.5px; color:var(--cinza); padding:18px 0 8px }

/* ---------- responsivo ---------- */
@media (max-width:760px){
  header{padding:10px 12px; flex-wrap:wrap; gap:8px}
  header h1{font-size:16px}
  .wrap{padding:12px 10px 50px}
  .grid-modos{grid-template-columns:1fr}
  .opcoes{grid-template-columns:1fr}
  .op{font-size:14.5px; min-height:52px; padding:12px 12px 12px 48px}
  .op .forma{font-size:18px; left:12px}
  .pergunta{font-size:17px}
  .modo h3{font-size:17px}
  .modo p{font-size:13px}
  .timerbox{font-size:14px; padding:4px 10px}
  .times{gap:6px}
  .time{font-size:13.5px; padding:6px 10px}
  .btn{padding:10px 16px; font-size:14px}
  .item-lista{padding:10px 12px}
}
</style>
</head>
<body>
<header class="topo">
  <h1>🎯 QuizWeb · __TITULO__</h1>
  <p>Curso Técnico em Informática · Turma 2/2026 · funciona 100% offline</p>
</header>
<div class="wrap" id="app"></div>
<footer>Material da disciplina — quizzes por aula, testes rápidos de módulo e modelos de prova.
Sem internet, sem login, sem mensalidade. 🙂</footer>
<script>
const DATA = __DATA__;
const FORMAS = ["▲","◆","●","■"];
const K = "__KEY__";
const app = document.getElementById("app");
let st = null;          // estado da partida
let timerId = null;

function store(k, v){ try{ if(v===undefined) return localStorage.getItem(K+k);
  localStorage.setItem(K+k, v); }catch(e){ return null; } }
function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

/* ---------------- telas ---------------- */
function telaHome(){
  pararTimer();
  app.innerHTML = `
   <div class="grid-modos">
     <button class="modo solo" onclick="telaLista('aulas')">
       <h3>📘 Quiz por aula</h3>
       <p>${DATA.aulas.length} quizzes rápidos (3 questões cada). Ideal para revisar logo após cada aula.</p>
     </button>
     <button class="modo lista" onclick="telaLista('modulos')">
       <h3>⚡ Testes de módulo</h3>
       <p>Os 12 testes rápidos da apostila (5 questões cada) para fechar cada bloco.</p>
     </button>
     <button class="modo turma" onclick="telaLista('provas')">
       <h3>🏆 Desafios de prova</h3>
       <p>Questões objetivas dos modelos A1, A2 e A3 — treino para as avaliações.</p>
     </button>
   </div>
   <div class="card">
     <b>Como jogar</b>
     <p class="nota"><b>Modo Solo:</b> cada aluno joga no próprio celular/PC — cronômetro de 20 s,
     pontos por velocidade e sequência de acertos; explicação após cada questão.<br>
     <b>Modo Turma:</b> o professor projeta — cronômetro de 30 s, revela a resposta e marca
     pontos para as equipes (botões de +1). Sem necessidade de aparelho por aluno.<br>
     <b>Na tela de qualquer quiz há o botão “Modo Turma”.</b></p>
   </div>`;
}

function conjuntos(tipo){
  if (tipo === "aulas") return DATA.aulas.map(a => ({id:"a"+a.n, t:`Aula ${a.n} — ${a.t}`,
      sub:`Módulo ${a.mod}`, qs:a.qs}));
  if (tipo === "modulos") return DATA.modulos.map(m => ({id:"m"+m.n, t:`Módulo ${m.n} — ${m.t}`,
      sub:"Teste rápido", qs:m.qs}));
  return DATA.provas.map(p => ({id:"p"+p.id, t:p.t, sub:"Modelo de prova", qs:p.qs}));
}

function telaLista(tipo){
  pararTimer();
  const itens = conjuntos(tipo);
  const tit = {aulas:"Quiz por aula", modulos:"Testes rápidos de módulo", provas:"Desafios de prova"}[tipo];
  let html = `<h2 class="sec">${tit} <button class="btn secund" style="float:right" onclick="telaHome()">← Início</button></h2>`;
  if (tipo === "aulas"){
    let modAtual = 0;
    for (const it of itens){
      const mod = DATA.aulas.find(a => "a"+a.n === it.id).mod;
      if (mod !== modAtual){ modAtual = mod; html += `<h2 class="sec" style="font-size:15px;margin:16px 4px 6px">Módulo ${mod}</h2>`; }
      html += itemHtml(it);
    }
  } else {
    for (const it of itens) html += itemHtml(it);
  }
  app.innerHTML = html;
}
function itemHtml(it){
  const rec = store("rec_"+it.id);
  return `<div class="item-lista" onclick="iniciar('${it.id}', false)">
    <div><div class="tt">${esc(it.t)}</div><div class="sub">${it.qs.length} questões · ${esc(it.sub)}</div></div>
    <div class="badge ${rec? 'rec':''}">${rec ? "★ "+rec : "jogar"}</div></div>`;
}

function acharSet(id){
  for (const tipo of ["aulas","modulos","provas"])
    for (const c of conjuntos(tipo)) if (c.id === id) return c;
  return null;
}

/* ---------------- partida ---------------- */
function iniciar(id, turma){
  const set = acharSet(id);
  st = { set, i:0, pts:0, acertos:0, seq:0, resp:[], turma:!!turma,
         times: turma ? (st && st.times ? st.times : []) : [],
         tempo: turma ? 30 : 20, restante: turma ? 30 : 20, revelado:false, escolhido:-1 };
  if (turma && (!st.times || st.times.length === 0)) return telaTimes(id);
  rodar();
}

function telaTimes(id){
  pararTimer();
  app.innerHTML = `<h2 class="sec">Modo Turma — equipes</h2>
   <div class="card">
     <p style="font-size:15px;margin-bottom:10px"><b>${esc(acharSet(id).t)}</b></p>
     <p class="nota">Digite os nomes das equipes separados por vírgula (ou deixe vazio para jogar só com o cronômetro):</p>
     <div class="linha" style="margin-top:10px"><input type="text" id="inp-times" placeholder="Equipe A, Equipe B, Equipe C"></div>
     <div class="linha">
       <button class="btn" onclick="comecarTurma('${id}')">Começar ▶</button>
       <button class="btn secund" onclick="telaLista('aulas')">Voltar</button>
     </div>
   </div>`;
}
function comecarTurma(id){
  const v = document.getElementById("inp-times").value.trim();
  const nomes = v ? v.split(",").map(s => s.trim()).filter(Boolean).slice(0,6) : [];
  st = { set: acharSet(id), i:0, pts:0, acertos:0, seq:0, resp:[], turma:true,
         times: nomes.map(n => ({n, p:0})), tempo:30, restante:30, revelado:false, escolhido:-1 };
  rodar();
}

function rodar(){
  const q = st.set.qs[st.i];
  st.revelado = false; st.escolhido = -1; st.restante = st.tempo;
  let html = `<div class="barra-topo">
      <span>${esc(st.set.t)} · questão ${st.i+1}/${st.set.qs.length}</span>
      <span class="placar">${st.turma ? "" : `⭐ ${st.pts} pts` + (st.seq>=2?` · 🔥${st.seq}`:"")}</span>
      <span class="timerbox" id="tb">${st.restante}s</span>
    </div>
    <div class="timerbar"><i id="tbi"></i></div>
    <div class="${st.turma? 'turma':''}">
      <div class="pergunta">${esc(q[0])}</div>
      <div class="opcoes">
        ${q[1].map((a,k) => `<button class="op c${k}" id="op${k}" onclick="responder(${k})">
            <span class="forma">${FORMAS[k]}</span>${esc(a)}</button>`).join("")}
      </div>
    </div>
    <div id="fb"></div>
    <div class="linha" style="margin-top:14px">
      ${st.turma ? `<button class="btn amarelo" id="btnRev" onclick="revelar()">👁 Revelar resposta</button>` : ""}
      <button class="btn secund" id="btnNext" style="display:none" onclick="proxima()">Próxima ▶</button>
      <button class="btn secund" onclick="sair()">Sair</button>
      ${!st.turma ? `<button class="btn" onclick="iniciar('${st.set.id}', true)">📽 Modo Turma</button>` : ""}
    </div>
    ${st.turma && st.times.length ? `<div class="times" id="times">${st.times.map((t,k) =>
        `<button class="time" id="tm${k}" onclick="pontoTime(${k})">${esc(t.n)}<span>${t.p}</span></button>`).join("")}</div>
      <p class="nota">Após revelar, toque na equipe que acertou para dar +1 ponto.</p>` : ""}`;
  app.innerHTML = html;
  iniciarTimer();
}

function iniciarTimer(){
  pararTimer();
  const total = st.tempo;
  timerId = setInterval(() => {
    st.restante--;
    const tb = document.getElementById("tb"), tbi = document.getElementById("tbi");
    if (!tb) return pararTimer();
    tb.textContent = Math.max(0, st.restante) + "s";
    tbi.style.width = Math.max(0, 100 * st.restante / total) + "%";
    if (st.restante <= 0){ pararTimer(); if (!st.revelado) revelar(true); }
  }, 1000);
}
function pararTimer(){ if (timerId){ clearInterval(timerId); timerId = null; } }

function responder(k){
  if (st.revelado) return;
  st.escolhido = k;
  revelar(false, k);
}

function revelar(estourou, k){
  if (st.revelado) return;
  pararTimer();
  st.revelado = true;
  const q = st.set.qs[st.i];
  const certo = q[2];
  const escolha = (k === undefined) ? st.escolhido : k;
  for (let i = 0; i < 4; i++){
    const b = document.getElementById("op"+i);
    if (!b) continue;
    b.disabled = true;
    if (i === certo) b.classList.add("certa");
    else if (i === escolha) b.classList.add("errada");
  }
  let ganho = 0;
  if (!st.turma && escolha >= 0 && escolha === certo){
    ganho = 500 + Math.round(500 * Math.max(0, st.restante) / st.tempo) + Math.min(st.seq,5) * 100;
    st.seq++; st.pts += ganho; st.acertos++;
  } else if (!st.turma){ st.seq = 0; }
  st.resp.push({q: q[0], certo, escolha, ok: escolha === certo});
  const fb = document.getElementById("fb");
  if (st.turma){
    fb.innerHTML = `<div class="feedback ${estourou? 'erro':'ok'}">
      <b>${estourou ? "⏰ Tempo esgotado!" : "✅ Resposta: " + FORMAS[certo] + " — " + esc(q[1][certo])}</b>
      ${esc(q[3] || "")}</div>`;
  } else {
    fb.innerHTML = escolha === certo
      ? `<div class="feedback ok"><b>✔ Acertou! +${ganho} pts</b>${esc(q[3] || "")}</div>`
      : `<div class="feedback erro"><b>${estourou? "⏰ Tempo esgotado!" : "✘ Não foi dessa vez…" }
         Resposta: ${FORMAS[certo]} — ${esc(q[1][certo])}</b>${esc(q[3] || "")}</div>`;
  }
  document.getElementById("btnNext").style.display = "inline-block";
  const br = document.getElementById("btnRev"); if (br) br.style.display = "none";
  const pl = document.querySelector(".placar");
  if (pl && !st.turma) pl.innerHTML = `⭐ ${st.pts} pts` + (st.seq>=2?` · 🔥${st.seq}`:"");
}

function pontoTime(k){
  if (!st.revelado || !st.times.length) return;
  st.times[k].p++;
  const b = document.getElementById("tm"+k);
  if (b) b.querySelector("span").textContent = st.times[k].p;
}

function proxima(){
  st.i++;
  if (st.i >= st.set.qs.length) return fim();
  rodar();
}

function fim(){
  pararTimer();
  const total = st.set.qs.length;
  if (!st.turma){
    const rec = parseInt(store("rec_"+st.set.id) || "0", 10);
    if (st.pts > rec) store("rec_"+st.set.id, String(st.pts));
    let rev = st.resp.map((r, i) => `<div class="rev ${r.ok? 'ok':'erro'}">
        <b>${i+1}. ${r.ok? "✔":"✘"} ${esc(r.q)}</b><br>
        Resposta: ${esc(st.set.qs[i][1][st.set.qs[i][2]])}</div>`).join("");
    app.innerHTML = `<div class="card podio">
        <div class="p1">${st.acertos === total ? "🏆" : st.acertos >= total/2 ? "🎉" : "💪"}</div>
        <h2 style="color:var(--roxo);font-size:26px;margin:6px 0">${st.pts} pontos</h2>
        <p style="font-size:16px">${st.acertos} de ${total} acertos · ${esc(st.set.t)}</p>
        ${st.pts >= rec && st.pts > 0 ? '<p class="nota" style="color:var(--verde);font-weight:700">★ Novo recorde!</p>' : ""}
        <div class="linha" style="justify-content:center;margin-top:14px">
          <button class="btn" onclick="iniciar('${st.set.id}', false)">🔁 Jogar de novo</button>
          <button class="btn secund" onclick="telaLista('aulas')">Lista</button>
          <button class="btn secund" onclick="telaHome()">Início</button>
        </div></div>
        <h2 class="sec">Revisão das questões</h2>${rev}`;
  } else {
    const ordenados = [...st.times].sort((a,b) => b.p - a.p);
    const medalhas = ["🥇","🥈","","4º","5º","6º"];
    app.innerHTML = `<div class="card podio">
        <div class="p1">🏁</div><h2 style="color:var(--roxo);font-size:26px;margin:6px 0">Fim de jogo!</h2>
        <p style="font-size:15px">${esc(st.set.t)} · ${total} questões</p>
        ${ordenados.length ? ordenados.map((t,i) =>
            `<div class="rev ${i===0? 'ok':''}" style="font-size:17px"><b>${medalhas[i]} ${esc(t.n)} — ${t.p} pts</b></div>`).join("")
          : `<p class="nota">Sem equipes cadastradas — o placar foi acompanhado oralmente pelo professor. 😄</p>`}
        <div class="linha" style="justify-content:center;margin-top:14px">
          <button class="btn" onclick="iniciar('${st.set.id}', true)">🔁 Outra rodada</button>
          <button class="btn secund" onclick="telaHome()">Início</button>
        </div></div>`;
  }
}

function sair(){ pararTimer(); telaHome(); }

telaHome();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    from conteudo import comuns as _c
    html = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
    html = html.replace("__TITULO__", _c.META["titulo_doc"])
    html = html.replace("__KEY__", "quizweb_" + _c.META["slug"])
    out = os.path.join(_ROOT, "output", f"QuizWeb_{comuns.META['slug']}.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    nq = (sum(len(a["qs"]) for a in DATA["aulas"]) +
          sum(len(m["qs"]) for m in DATA["modulos"]) +
          sum(len(p["qs"]) for p in DATA["provas"]))
    print("OK:", out)
    print("aulas:", len(DATA["aulas"]), "| módulos:", len(DATA["modulos"]),
          "| provas:", len(DATA["provas"]), "| total de questões:", nq)
    print("tamanho:", round(os.path.getsize(out)/1024, 1), "KB")
