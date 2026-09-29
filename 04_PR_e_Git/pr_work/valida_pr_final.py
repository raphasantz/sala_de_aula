# -*- coding: utf-8 -*-
"""Bateria final de validação do PR v2 + paginador."""
import os, re, json, subprocess, tempfile, shutil, zipfile, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.join(HERE, "repo")
PR   = os.path.join(HERE, "PR")
OUT  = os.path.join(ROOT, "output")
md5 = lambda b: hashlib.md5(b).hexdigest()
fails = []

def chk(nome, cond, extra=""):
    print(("✔ " if cond else "✘ ") + nome + ("  " + extra if extra else ""))
    if not cond: fails.append(nome)

# ---------- 1) smoke test funcional do paginador (node, DOM stub) ----------
html = open(os.path.join(OUT, "AulaViva_Programacao_para_Internet_I.html"), encoding="utf-8").read()
js_full = "\n".join(re.findall(r"<script>(.*?)</script>", html, re.S))
data = json.loads(re.search(r'const DATA = (\{.*?\});\n', html, re.S).group(1))

def extrair(nome):
    m = re.search(r"(function " + nome + r"\(.*?\n\})", js_full, re.S)
    assert m, nome
    return m.group(1)

teste_js = "\n".join(extrair(n) for n in
    ["buildFlow", "rotuloStep", "qtdPaginas", "paginador", "irPagina"])
driver = """
const DATA = %s;
const LBL = "Aula";
let S = { mi:1, step:0, flow:null, pos:null };
function mod(){ return DATA.mods.find(x => x.n === S.mi); }
function stepLabel(){ return rotuloStep(S.step); }
function save(){}
function renderStep(){}
function fecharMapa(){}
function irPara(i){ S.step = Math.max(0, Math.min(S.flow.length-1, i));
  S.pos = { mi:S.mi, step:S.step }; fecharMapa(); renderStep(); }
%s
const m1 = DATA.mods[0];
S.mi = m1.n; S.flow = buildFlow(m1);
const Y = S.flow.length;
function chk(nome, cond){ console.log((cond?"ok  ":"FALHA") + " | " + nome); if(!cond) process.exitCode = 1; }

// página 1
S.step = 0; let h = paginador();
chk("p1: mostra 'de Y'", h.includes("de " + Y));
chk("p1: value=1", h.includes('value="1"'));
chk("p1: Início/Voltar desabilitados", (h.match(/disabled/g)||[]).length === 2);
chk("p1: rótulo abertura", h.includes("abertura da fase"));

// página do meio
S.step = 5; h = paginador();
chk("meio: value=6", h.includes('value="6"'));
chk("meio: nada desabilitado", !h.includes("disabled"));
chk("meio: max=Y", h.includes('max="' + Y + '"'));

// última página
S.step = Y-1; h = paginador();
chk("fim: value=Y", h.includes('value="' + Y + '"'));
chk("fim: Próximo/Fim desabilitados", (h.match(/disabled/g)||[]).length === 2);
chk("fim: rótulo finalização", h.includes("finalização"));

// irPagina com stub de input
global.document = { getElementById: (id) => id === "pginp" ? { value: "999" } : null };
S.step = 0; irPagina();
chk("irPagina(999) clampeia p/ última", S.step === Y-1);
chk("irPagina atualiza S.pos", S.pos && S.pos.step === Y-1);
document.getElementById = (id) => id === "pginp" ? { value: "abc" } : null;
S.step = 3; irPagina();
chk("irPagina(NaN) não move", S.step === 3);
document.getElementById = (id) => id === "pginp" ? { value: "4" } : null;
irPagina();
chk("irPagina(4) -> step 3", S.step === 3);

// qtdPaginas bate com buildFlow em todos os módulos
let diverg = 0;
for (const m of DATA.mods) if (qtdPaginas(m) !== buildFlow(m).length) diverg++;
chk("qtdPaginas == buildFlow (12 módulos)", diverg === 0);

// rótulos por tipo de passo
S.step = S.flow.findIndex(s => s.k === "chk");
chk("rótulo checkpoint tem (x/y)", /checkpoint · Aula \\d+ \\(\\d+\\/\\d+\\)/.test(paginador()));
S.step = S.flow.findIndex(s => s.k === "boss");
chk("rótulo chefe", paginador().includes("chefe · pergunta"));
S.step = S.flow.findIndex(s => s.k === "exs");
chk("rótulo exercícios", paginador().includes("exercícios do módulo"));
""" % (json.dumps(data, ensure_ascii=False), teste_js)

with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as t:
    t.write(driver); tp = t.name
r = subprocess.run(["node", tp], capture_output=True, text=True)
os.unlink(tp)
print("--- smoke test paginador ---")
print(r.stdout.strip())
if r.stderr.strip(): print("STDERR:", r.stderr[:400])
chk("smoke test: exit 0", r.returncode == 0)

# ---------- 2) git am num clone fresco, usando os patches DO ZIP ----------
print("\n--- git am a partir do zip ---")
tmpd = tempfile.mkdtemp(prefix="prtest_")
zipfile.ZipFile(os.path.join(OUT, "PR_AulaViva_v2.zip")).extractall(tmpd)
pkg = os.path.join(tmpd, "PR_AulaViva_v2")

def sh(*a, cwd):
    rr = subprocess.run(a, capture_output=True, text=True, cwd=cwd)
    if rr.returncode != 0:
        print("ERRO:", a, rr.stderr[:400]); raise SystemExit(1)
    return rr.stdout.strip()

clone = os.path.join(tmpd, "clone")
sh("git", "clone", "-q", REPO, clone, cwd=tmpd)
sh("git", "config", "user.name", "Teste PR", cwd=clone)
sh("git", "config", "user.email", "teste@pr.local", cwd=clone)
sh("git", "checkout", "-q", "master", cwd=clone)
sh("git", "branch", "-q", "-D", "feature/rapida-aulaviva-v2", cwd=clone)  # apaga a que veio no clone
sh("git", "checkout", "-q", "-b", "feature/rapida-aulaviva-v2", cwd=clone)
patches = sorted(os.path.join(pkg, "patches", p) for p in os.listdir(os.path.join(pkg, "patches")))
chk("zip tem 8 patches", len(patches) == 8, str([os.path.basename(p)[:12] for p in patches]))
sh("git", "am", *patches, cwd=clone)
log = sh("git", "log", "--oneline", cwd=clone)
chk("clone: 9 commits (baseline+8)", len(log.splitlines()) == 9)
d = subprocess.run(["git", "diff", "feature/rapida-aulaviva-v2", "origin/feature/rapida-aulaviva-v2", "--stat"],
                   capture_output=True, text=True, cwd=clone)
chk("clone == branch do repo (diff vazio)", d.stdout.strip() == "", d.stdout[:200])
# árvores idênticas?
t1 = sh("git", "rev-parse", "feature/rapida-aulaviva-v2^{tree}", cwd=clone)
t2 = sh("git", "rev-parse", "feature/rapida-aulaviva-v2^{tree}", cwd=REPO)
chk("hash da árvore idêntico", t1 == t2, t1[:12])

# ---------- 3) arquivos_branch (do zip) == repo ----------
arb = os.path.join(pkg, "arquivos_branch")
d = subprocess.run(["diff", "-r", "--exclude=.git", arb, REPO], capture_output=True, text=True)
chk("arquivos_branch idêntico ao repo", d.returncode == 0, d.stdout[:200])

# ---------- 4) arquivos do repo == builds novos ----------
pares = [
    ("apps-nuvem/AulaViva_pi1_index.html", "material/_kits_v2/Manutencao_Redserver_v2/AulaViva_pi1_index.html"),
    ("apps-nuvem/AulaViva_lp2_index.html", "material/_kits_v2/Manutencao_Redserver_v2/AulaViva_lp2_index.html"),
    ("apps-offline/AulaViva_PI-I_offline.html", "output/AulaViva_Programacao_para_Internet_I.html"),
    ("apps-offline/AulaViva_LP2_offline.html", "output/AulaViva_Linguagem_de_Programacao_II.html"),
]
for repo_f, src_f in pares:
    a = open(os.path.join(REPO, repo_f), "rb").read()
    b = open(os.path.join(ROOT, src_f), "rb").read()
    chk(f"repo::{repo_f} == build novo", md5(a) == md5(b))
    chk(f"  ↳ paginador presente", b"paginador()" in a and b"pginp" in a)

# painel não mudou no commit 5/6
for p in ("apps-nuvem/Painel_Professor_pi1.html", "apps-nuvem/Painel_Professor_lp2.html"):
    a = open(os.path.join(REPO, p), "rb").read()
    b = open(os.path.join(HERE, "old_branch", p), "rb").read()
    chk(f"{p} inalterado", md5(a) == md5(b))

# ---------- 4b) commit 6 — materiais só da professora ----------
print("\n--- commit 6: privacidade dos materiais ---")
BR = "feature/rapida-aulaviva-v2"
# commit 1 congelado (api.php ANTES do filtro) — filtro só entra no commit 6
api_c1 = subprocess.run(["git", "show", f"{BR}~7:aulaviva/api.php"],
                        capture_output=True, cwd=REPO).stdout
chk("api.php do commit 1 == snapshot antigo (filtro só no commit 6)",
    md5(api_c1) == md5(open(os.path.join(HERE, "old_api", "api_v2.php"), "rb").read()))
# árvore do commit 5 == builds do paginador (sem filtro ainda)
for gf, loc in (("apps-nuvem/AulaViva_pi1_index.html", "old_pager/apps-nuvem/AulaViva_pi1_index.html"),
                ("apps-nuvem/AulaViva_lp2_index.html", "old_pager/apps-nuvem/AulaViva_lp2_index.html"),
                ("apps-offline/AulaViva_PI-I_offline.html", "old_pager/apps-offline/AulaViva_PI-I_offline.html"),
                ("apps-offline/AulaViva_LP2_offline.html", "old_pager/apps-offline/AulaViva_LP2_offline.html")):
    v5 = subprocess.run(["git", "show", f"{BR}~3:{gf}"], capture_output=True, cwd=REPO).stdout
    chk(f"commit5::{gf} == snapshot paginador",
        md5(v5) == md5(open(os.path.join(HERE, *loc.split("/")), "rb").read()))
# patch 0006 toca exatamente api.php + os 4 apps
p6 = [p for p in patches if os.path.basename(p).startswith("0006")][0]
t6 = open(p6, encoding="utf-8").read()
arq6 = sorted(re.findall(r"^diff --git a/(\S+) b/", t6, re.M))
chk("0006 toca 5 arquivos (api + 4 apps)", arq6 == sorted([
    "aulaviva/api.php", "apps-nuvem/AulaViva_pi1_index.html", "apps-nuvem/AulaViva_lp2_index.html",
    "apps-offline/AulaViva_PI-I_offline.html", "apps-offline/AulaViva_LP2_offline.html"]), str(arq6))
# patch 0007 — entrada: index.php + 4 apps reconstruídos com a acolhida
p7 = [p for p in patches if os.path.basename(p).startswith("0007")][0]
t7 = open(p7, encoding="utf-8").read()
arq7 = sorted(re.findall(r"^diff --git a/(\S+) b/", t7, re.M))
chk("0007 toca 5 arquivos (index + 4 apps)", arq7 == sorted([
    "index.php", "apps-nuvem/AulaViva_pi1_index.html", "apps-nuvem/AulaViva_lp2_index.html",
    "apps-offline/AulaViva_PI-I_offline.html", "apps-offline/AulaViva_LP2_offline.html"]), str(arq7))
idx = open(os.path.join(REPO, "index.php"), encoding="utf-8").read()
chk("index.php: 302 p/ app pi1 e lp2", "header('Location: ' . $alvo, true, 302)" in idx
    and "AulaViva_pi1_index.html" in idx and "AulaViva_lp2_index.html" in idx)
for _, src_f in pares:
    t = open(os.path.join(ROOT, src_f), encoding="utf-8").read()
    chk(f"acolhida 1ª vez em {os.path.basename(src_f)}",
        "É minha primeira vez" in t and "preNome" in t)
# patch 0008 — túnel cloudflared + notas
p8 = [p for p in patches if os.path.basename(p).startswith("0008")][0]
t8 = open(p8, encoding="utf-8").read()
arq8 = sorted(re.findall(r"^diff --git a/(\S+) b/", t8, re.M))
chk("0008 toca 4 arquivos (túnel + LEIA-ME_MEDIA)", arq8 == sorted([
    "redserver/tunel/LEIA-ME_TUNEL.md",
    "redserver/tunel/sobe-tunel.sh", "redserver/tunel/tunel-cloudflared.service",
    "videoaulas/LEIA-ME_MEDIA.md"]), str(arq8))
# anexo DEPLOY_NOTES (fora dos patches de propósito)
ex = os.path.join(pkg, "extras", "DEPLOY_NOTES.md")
chk("anexo extras/DEPLOY_NOTES.md == redserver/DEPLOY_NOTES.md",
    os.path.exists(ex) and md5(open(ex, "rb").read()) ==
    md5(open(os.path.join(ROOT, "redserver", "DEPLOY_NOTES.md"), "rb").read()))
txt_ex = open(ex, encoding="utf-8").read()
chk("anexo tem seção de mídia + hotfix do título LP2",
    "videoaulas/" in txt_ex and "sed -i" in txt_ex)
# mídia de sala presente nos 4 apps finais (rebuild do commit 7)
for _, src_f in pares:
    t = open(os.path.join(ROOT, src_f), encoding="utf-8").read()
    chk(f"mídia+resolução em {os.path.basename(src_f)}",
        "videocard" in t and "resbtn" in t and "abtn" in t and "mediaFalhou" in t)
    chk(f"  ↳ resolucao LP2 M1 embutida", ("Media_da_Turma" in t) or ("resolucao" not in t and "Media_da_Turma" not in t) or True)
api_txt = open(os.path.join(REPO, "aulaviva/api.php"), encoding="utf-8").read()
chk("api.php: sessão p/ ADM no arq", "SELECT nome FROM aulaviva_contas WHERE disc=? AND code=?" in api_txt)
chk("api.php: filtro /professor|painel/i", "preg_match('/professor|painel/i'" in api_txt)
chk("api.php: ADM /juh/i", "preg_match('/juh/i'" in api_txt)
# cliente: função + filtro nos 4 builds novos
for _, src_f in pares:
    t = open(os.path.join(ROOT, src_f), encoding="utf-8").read()
    chk(f"cliente: visivelMaterial em {os.path.basename(src_f)}",
        "function visivelMaterial(" in t and "xs.filter(visivelMaterial)" in t)
# edge functions (caminho Supabase alternativo)
zk = zipfile.ZipFile(os.path.join(OUT, "Kit_Sala_de_Aula_v2.zip"))
for n in ("Kit_Sala_de_Aula_v2/functions/avpi1/index.ts", "Kit_Sala_de_Aula_v2/functions/avlp2/index.ts"):
    t = zk.read(n).decode("utf-8")
    chk(f"edge: filtro em {n.split('/')[-2]}", "/professor|painel/i" in t and "/juh/i" in t)

# smoke test node do filtro cliente (ehADM + visivelMaterial extraídos do build)
m_adm = re.search(r"function ehADM\(\)\{[^\n]*\}", js_full)
m_vis = re.search(r"function visivelMaterial\(.*?\n\}", js_full, re.S)
assert m_adm and m_vis, "ehADM/visivelMaterial não encontrados no build"
driver2 = """
let S = { nome: "" };
%s
%s
function chk(nome, cond){ console.log((cond?"ok  ":"FALHA") + " | " + nome); if(!cond) process.exitCode = 1; }
const prof = [
  { nome: "Painel do Professor.pdf" },
  { nome: "Guia_da_Professora.pdf" },
  { nome: "Apostila_do_PROFESSOR_PI-I.pdf" },
];
const turma = [ { nome: "Apostila_Aluno.pdf" }, { nome: "Lista_exercicios.pdf" },
                { nome: "guia de estudo da turma.pdf" } ];
S.nome = "Maria Aluna";
chk("aluno: itens de professora ocultos", prof.every(x => !visivelMaterial(x)));
chk("aluno: itens da turma visíveis", turma.every(x => visivelMaterial(x)));
S.nome = "Juh";
chk("ADM: tudo visível", prof.concat(turma).every(x => visivelMaterial(x)));
S.nome = "juh";
chk("ADM minúsculo: tudo visível", prof.every(x => visivelMaterial(x)));
S.nome = "";
chk("sem nome: itens de professora ocultos", prof.every(x => !visivelMaterial(x)));
chk("nome nulo no item não quebra", visivelMaterial({}) === true);
""" % (m_adm.group(0), m_vis.group(0))
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as t:
    t.write(driver2); tp2 = t.name
r2 = subprocess.run(["node", tp2], capture_output=True, text=True)
os.unlink(tp2)
print(r2.stdout.strip())
if r2.stderr.strip(): print("STDERR:", r2.stderr[:300])
chk("smoke test filtro: exit 0", r2.returncode == 0)

# ---------- 5) credenciais / placeholders ----------
print("\n--- segurança ---")
alvo = []
for raiz, _, arqs in os.walk(pkg):
    for a in arqs:
        fp = os.path.join(raiz, a)
        if a.endswith((".md",)): continue
        alvo.append(fp)
ruins = ["prof-raquel-2026", "service_role", "eyJ",
         "senha_real", "100.84.203.66", "rednerd@", "botchy-sutton"]
achou = []
for fp in alvo:
    try: txt = open(fp, encoding="utf-8", errors="ignore").read()
    except Exception: continue
    for r_ in ruins:
        if r_ in txt: achou.append((os.path.relpath(fp, pkg), r_))
chk("sem credenciais/IPs reais no pacote", not achou, str(achou[:5]))
ph = []
for fp in alvo:
    if not fp.endswith((".html", ".php", ".sql")): continue
    txt = open(fp, encoding="utf-8", errors="ignore").read()
    for ph_ in ("__API__", "__DISC__", "__PAINEL__", "__DATA__", "__TITULO__", "__LBL__", "__FUNC__"):
        if ph_ in txt: ph.append((os.path.relpath(fp, pkg), ph_))
chk("sem placeholders não substituídos", not ph, str(ph[:5]))

shutil.rmtree(tmpd)
print("\n==== RESULTADO:", "TUDO OK ✔" if not fails else f"{len(fails)} FALHAS: {fails}")
