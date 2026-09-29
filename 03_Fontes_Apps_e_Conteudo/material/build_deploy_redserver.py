# -*- coding: utf-8 -*-
"""Gera a versão REDSERVER dos apps (sync via aulaviva/api.php + MySQL,
ZERO localStorage — shim de memória), alinhada à produção descrita no handover."""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUTD = os.path.join(ROOT, "redserver", "apps-nuvem")
os.makedirs(OUTD, exist_ok=True)

SHIM = """<script>
/* modo redserver: NADA de localStorage no aparelho — memória apenas */
(function(){
  var m = {};
  var shim = {
    getItem: function(k){ return (k in m) ? m[k] : null; },
    setItem: function(k, v){ m[k] = String(v); },
    removeItem: function(k){ delete m[k]; },
    clear: function(){ m = {}; },
    key: function(i){ return Object.keys(m)[i] || null; }
  };
  try { Object.defineProperty(window, "localStorage", { value: shim, configurable: true }); }
  catch(e){ try { window.localStorage = shim; } catch(e2){} }
})();
</script>
<script>"""

NUVEM = r"""
<script>
/* ========== sync redserver: api.php + cookie httpOnly (sem localStorage) ========== */
(function(){
  var DISC = "__DISC__";
  var API  = "../aulaviva/api.php";
  var elNuvem = null;
  function status(t){ if (!elNuvem) elNuvem = document.getElementById("nuvem");
    if (elNuvem) elNuvem.textContent = t; }
  function pill(){
    var d = document.querySelector("header .dir");
    if (d && !document.getElementById("nuvem")){
      var s = document.createElement("span"); s.id = "nuvem"; s.className = "pill ghost";
      s.textContent = "☁️ …"; d.prepend(s); elNuvem = s;
    }
    if (d && !document.getElementById("btArq")){
      var b = document.createElement("button"); b.className = "pill"; b.id = "btArq";
      b.textContent = "📎 Materiais"; b.onclick = abrirMateriais; d.prepend(b);
    }
  }
  pill(); setTimeout(pill, 600); setTimeout(pill, 1500);

  var pend = false, timer = null;
  function enviar(){
    timer = null; if (!pend) return; pend = false;
    fetch(API + "?disc=" + DISC + "&a=put", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome: S.nome || "", turma: S.turma || "", payload: {
        mi: S.mi, pts: S.pts, seq: S.seq, exok: S.exok, done: S.done, boss: S.boss,
        pos: S.pos, aulas: S.aulas, scored: S.scored, nome: S.nome, turma: S.turma } })
    }).then(function(r){ status(r.ok ? "☁️ salvo" : "☁️ offline"); })
      .catch(function(){ status("☁️ offline"); });
  }
  function marcar(){ pend = true; if (!timer) timer = setTimeout(enviar, 1200); }
  var _save0 = window.save;
  window.save = function(){ var r = _save0.apply(this, arguments); marcar(); return r; };

  function abrirMateriais(){
    S.flow = null; setHud();
    app.innerHTML = '<div class="cardp"><h2>📎 Materiais da turma</h2>' +
      '<p style="margin:6px 0 12px">Documentos enviados pela professora.</p>' +
      '<div id="listaArq"><p class="nota">carregando…</p></div>' +
      '<div class="nav"><button class="btn gh" onclick="irHome()">← Voltar à trilha</button></div></div>';
    fetch(API + "?disc=" + DISC + "&a=arq")
      .then(function(r){ return r.ok ? r.json() : []; })
      .then(function(xs){
        var el = document.getElementById("listaArq");
        if (!xs || !xs.length){ el.innerHTML = "<p class='nota'>Nenhum material enviado ainda.</p>"; return; }
        el.innerHTML = xs.map(function(x){
          var kb = x.tamanho ? Math.max(1, Math.round(x.tamanho/1024)) + " KB" : "";
          return '<div style="display:flex;justify-content:space-between;gap:10px;align-items:center;' +
            'background:#f4f8fc;border:1px solid #dfe8f2;border-radius:10px;padding:10px 12px;margin:8px 0">' +
            '<a href="' + x.url + '" target="_blank" download style="color:#1b5faa;font-weight:700;' +
            'text-decoration:none">⬇ ' + x.nome + '</a>' +
            '<span style="font-size:12px;color:#5b6b7c">' + kb + ' · ' +
            (x.atualizado || "").slice(0, 10) + '</span></div>';
        }).join("");
      })
      .catch(function(){ document.getElementById("listaArq").innerHTML =
        "<p class='nota'>Offline no momento.</p>"; });
  }

  fetch(API + "?disc=" + DISC + "&a=get")
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(j){
      if (j && j.payload && typeof j.payload.pts === "number"){
        Object.assign(S, j.payload); S.flow = null;
        if (typeof updateNomeBtn === "function") updateNomeBtn();
        if (typeof renderHome === "function") renderHome();
        status("☁️ sincronizado");
      } else { status("☁️ conectado"); }
    })
    .catch(function(){ status("☁️ offline"); });
})();
</script>
</body>"""

PROF = r"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Painel do Professor — AulaViva __LABEL__ (redserver)</title>
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
<header><h1>👩‍🏫 Painel do Professor — AulaViva __LABEL__ · redserver</h1></header>
<div class="wrap">
  <div class="card">
    <p style="margin:0 0 10px"><b>Token do professor</b> (variável AULAVIVA_PROF_TOKEN no servidor):</p>
    <input id="tok" type="password" placeholder="cole o PROF_TOKEN">
    <button onclick="carregar()">Ver turma</button>
    <button class="gh" onclick="csv()">Exportar CSV</button>
  </div>
  <div class="card" style="margin-top:14px" id="resultado"></div>
  <div class="card" style="margin:14px 0">
    <p style="margin:0 0 10px"><b>📎 Enviar material para a turma</b></p>
    <input type="file" id="farq" style="width:auto;max-width:70vw">
    <button onclick="enviarArq()">Enviar</button>
    <div id="stArq" class="nota"></div>
    <div id="listaProf" style="margin-top:10px"></div>
  </div>
</div>
<script>
const DISC = "__DISC__";
const API = "../aulaviva/api.php";
let LINHAS = [];
async function carregar(){
  const tok = document.getElementById("tok").value.trim();
  const r = await fetch(API + "?disc=" + DISC + "&a=lista&token=" + encodeURIComponent(tok));
  const el = document.getElementById("resultado");
  if (!r.ok){ el.innerHTML = "<p class='nota'>Falha: " + r.status + " (token?)</p>"; return; }
  LINHAS = await r.json();
  if (!LINHAS.length){ el.innerHTML = "<p class='nota'>Nenhum aluno sincronizado ainda.</p>"; return; }
  let h = "<table><tr><th>#</th><th>Aluno</th><th>Turma</th><th>Pontos</th><th>Módulos</th>" +
          "<th>Aulas</th><th>Última sync</th></tr>";
  LINHAS.forEach((x, i) => {
    const p = x.payload || {};
    h += "<tr><td>" + (i+1) + "</td><td><b>" + (x.nome || "(sem nome)") + "</b></td><td>" +
      (x.turma || "-") + "</td><td class='ok'>" + (p.pts || 0) + "</td><td>" +
      Object.keys(p.done || {}).length + "</td><td>" + Object.keys(p.aulas || {}).length +
      "</td><td>" + (x.updated_at || "").replace("T", " ").slice(0, 16) + "</td></tr>";
  });
  el.innerHTML = h + "</table>";
  listarProf();
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
async function enviarArq(){
  const tok = document.getElementById("tok").value.trim();
  const f = document.getElementById("farq").files[0];
  const st = document.getElementById("stArq");
  if (!f || !tok){ st.textContent = "Escolha o arquivo e informe o token."; return; }
  const b64 = await new Promise(res => { const r = new FileReader();
    r.onload = () => res(r.result.split(",")[1]); r.readAsDataURL(f); });
  st.textContent = "Enviando " + f.name + " …";
  const r = await fetch(API + "?disc=" + DISC + "&a=arqup", {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token: tok, nome: f.name, base64: b64, tipo: f.type }) });
  st.textContent = r.ok ? "✔ Disponível para a turma!" : "Falha: HTTP " + r.status;
  listarProf();
}
async function listarProf(){
  const tok = document.getElementById("tok").value.trim();
  if (!tok) return;
  const r = await fetch(API + "?disc=" + DISC + "&a=arq");
  if (!r.ok) return;
  const xs = await r.json();
  document.getElementById("listaProf").innerHTML = xs.length
    ? "<b>Disponíveis:</b> " + xs.map(x => x.nome).join(" · ")
    : "<span class='nota'>Nenhum material enviado ainda.</span>";
}
</script>
</body>
</html>
"""

SQL = """-- Tabela de progresso do AulaViva (MySQL do redserver) — execute 1x
CREATE TABLE IF NOT EXISTS aulaviva_alunos (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  disc VARCHAR(8) NOT NULL,
  code CHAR(16) NOT NULL,
  nome VARCHAR(80) DEFAULT '',
  turma VARCHAR(40) DEFAULT '',
  payload JSON,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_disc_code (disc, code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

NOTES = """# Deploy no redserver (regra de ouro do handover)

Fonte de verdade: **/root/_drop/kit_sala/** → scp → **/mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/**
Confira `md5sum` local × remoto antes de dar por pronto. Teste SEMPRE pela URL do ngrok.

## Arquivos desta pasta de manutenção
| Origem (aqui) | Destino no servidor |
|---|---|
| aulaviva/api.php | Kit_Sala_de_Aula/aulaviva/api.php |
| aulaviva/aulaviva_alunos.sql | executar 1× no MySQL (sudo mysql loja_turma) |
| apps-nuvem/AulaViva_PI-I_index.html | Kit_Sala_de_Aula/apps-nuvem/… |
| apps-nuvem/AulaViva_LP2_index.html | idem |
| apps-nuvem/Painel_Professor_PI-I.html | idem |
| apps-nuvem/Painel_Professor_LP2.html | idem |

## Comandos modelo
    scp aulaviva/api.php rednerd@100.84.203.66:/tmp/
    ssh rednerd@100.84.203.66 'sudo cp /tmp/api.php /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php && sudo chown www-data:www-data /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php'
    md5sum aulaviva/api.php   # e compare com o remoto

## Antes do primeiro uso
1. Rode `aulaviva_alunos.sql` no MySQL (tabela aulaviva_alunos);
2. Crie `aulaviva/materiais/pi1/` e `aulaviva/materiais/lp2/` (chown www-data);
3. Defina no php-fpm (pool do vhost pcs-replica):
   `env[LOJA_DB_PASS] = <senha do loja_app>` e `env[AULAVIVA_PROF_TOKEN] = <token novo>`;
4. **ROTACIONE** a senha antiga e o token antigo (o doc de handover circulou com eles em claro).

## Regras que eu (manutenção) respeito
- Nada de localStorage nos apps (shim de memória injetado);
- Erros de banco → error_log, mensagem genérica pro browser;
- Pedido de loja: transação + SELECT … FOR UPDATE (não reverter);
- Não tocar em outros vhosts (8081/8082, mesanerd, calistenia, siad…);
- Resíduos de teste (linhas qa_*) sempre apagados após QA.
"""

def build():
    for disc, label, src in [
        ("pi1", "Programação para Internet I", "AulaViva_Programacao_para_Internet_I.html"),
        ("lp2", "Linguagem de Programação II", "AulaViva_Linguagem_de_Programacao_II.html"),
    ]:
        html = io.open(os.path.join(ROOT, "output", src), encoding="utf-8").read()
        # shim ANTES do script principal do app
        html = html.replace("<script>\nconst DATA =", SHIM.replace("<script>", "", 1) if False else SHIM + "\nconst DATA =", 1) \
            if False else html
        idx = html.find("<script>")
        html = html[:idx] + SHIM + html[idx + len("<script>"):]
        html = html.replace("</body>", NUVEM.replace("__DISC__", disc), 1)
        io.open(os.path.join(OUTD, f"AulaViva_{disc}_index.html"), "w", encoding="utf-8").write(html)
        io.open(os.path.join(OUTD, f"Painel_Professor_{disc}.html"), "w", encoding="utf-8").write(
            PROF.replace("__DISC__", disc).replace("__LABEL__", label))
        print("app redserver ok:", disc)
    io.open(os.path.join(ROOT, "redserver", "aulaviva", "aulaviva_alunos.sql"), "w",
            encoding="utf-8").write(SQL)
    io.open(os.path.join(ROOT, "redserver", "DEPLOY_NOTES.md"), "w",
            encoding="utf-8").write(NOTES)
    print("sql + notes ok")

if __name__ == "__main__":
    build()
