# -*- coding: utf-8 -*-
"""Monta o repositório local do PR (master v1 + branch v2), patches e docs.
Rodar a partir de /home/user/pr_work (caminhos relativos)."""
import os, shutil, subprocess, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.join(HERE, "repo")
PR   = os.path.join(HERE, "PR")
KIT  = os.path.join(ROOT, "material", "_kits_v2", "Manutencao_Redserver_v2")
V1   = os.path.join(HERE, "v1red", "redserver")
KITFULL = os.path.join(HERE, "kitv1full")

def sh(*args, **kw):
    r = subprocess.run(args, capture_output=True, text=True, cwd=kw.get("cwd", REPO))
    if r.returncode != 0:
        print("ERRO:", args, r.stderr[:500]); raise SystemExit(1)
    return r.stdout.strip()

# ---------- limpa ----------
for d in (REPO, PR):
    if os.path.exists(d): shutil.rmtree(d)
os.makedirs(REPO); os.makedirs(os.path.join(PR, "patches"))

# ---------- master: baseline v1 (só os arquivos que o PR toca) ----------
def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)

base = {
    "apps-nuvem/AulaViva_pi1_index.html":   f"{V1}/apps-nuvem/AulaViva_pi1_index.html",
    "apps-nuvem/AulaViva_lp2_index.html":   f"{V1}/apps-nuvem/AulaViva_lp2_index.html",
    "apps-nuvem/Painel_Professor_pi1.html": f"{V1}/apps-nuvem/Painel_Professor_pi1.html",
    "apps-nuvem/Painel_Professor_lp2.html": f"{V1}/apps-nuvem/Painel_Professor_lp2.html",
    "aulaviva/api.php":                     f"{V1}/aulaviva/api.php",
    "aulaviva/aulaviva_alunos.sql":         f"{V1}/aulaviva/aulaviva_alunos.sql",
    "apps-offline/AulaViva_PI-I_offline.html": f"{HERE}/v1off/AulaViva_Programacao_para_Internet_I.html",
    "apps-offline/AulaViva_LP2_offline.html":  f"{HERE}/v1off/AulaViva_Linguagem_de_Programacao_II.html",
    "redserver/DEPLOY_NOTES.md":               f"{HERE}/v1red/DEPLOY_NOTES.md",
}
for dst, src in base.items():
    cp(src, os.path.join(REPO, dst))

sh("git", "init", "-b", "master")
sh("git", "config", "user.name", "Agente Kit-Sala (Qwen)")
sh("git", "config", "user.email", "agente@kit-sala-de-aula.local")
sh("git", "add", "-A")
sh("git", "commit", "-m", "baseline: estado v1 em produção (apps-nuvem, aulaviva, apps-offline)",
   "-m", "Snapshot dos arquivos atualmente no repositório/servidor que este PR substitui. (Baseline local do agente — no repo real estes arquivos já existem na master.)")

# ---------- branch da tarefa ----------
BR = "feature/rapida-aulaviva-v2"
sh("git", "checkout", "-b", BR)

# commit 1 — backend (conteúdo congelado ANTES do commit 6 — filtro de materiais)
cp(f"{HERE}/old_api/api_v2.php",          f"{REPO}/aulaviva/api.php")
cp(f"{ROOT}/redserver/aulaviva_v2.sql",  f"{REPO}/aulaviva/migracao_contas_entregas.sql")
cp(f"{HERE}/LEIA-ME_MIGRACAO.md",        f"{REPO}/aulaviva/LEIA-ME_MIGRACAO.md")
sh("git", "add", "-A")
sh("git", "commit", "-F", f"{HERE}/msg1.txt")

# commit 2 — apps nuvem (versão da branch ANTES do paginador — ver commit 5)
cp(f"{HERE}/old_branch/apps-nuvem/AulaViva_pi1_index.html", f"{REPO}/apps-nuvem/AulaViva_pi1_index.html")
cp(f"{HERE}/old_branch/apps-nuvem/AulaViva_lp2_index.html", f"{REPO}/apps-nuvem/AulaViva_lp2_index.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg2.txt")

# commit 3 — painéis (idênticos aos da branch anterior — commit 6 não toca neles)
cp(f"{HERE}/old_branch/apps-nuvem/Painel_Professor_pi1.html", f"{REPO}/apps-nuvem/Painel_Professor_pi1.html")
cp(f"{HERE}/old_branch/apps-nuvem/Painel_Professor_lp2.html", f"{REPO}/apps-nuvem/Painel_Professor_lp2.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg3.txt")

# commit 4 — offline (versão da branch ANTES do paginador — ver commit 5)
cp(f"{HERE}/old_branch/apps-offline/AulaViva_PI-I_offline.html", f"{REPO}/apps-offline/AulaViva_PI-I_offline.html")
cp(f"{HERE}/old_branch/apps-offline/AulaViva_LP2_offline.html", f"{REPO}/apps-offline/AulaViva_LP2_offline.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg4.txt")

# commit 5 — paginador (página X de Y + Início/Voltar/Próximo/Fim + salto por número)
cp(f"{HERE}/old_pager/apps-nuvem/AulaViva_pi1_index.html", f"{REPO}/apps-nuvem/AulaViva_pi1_index.html")
cp(f"{HERE}/old_pager/apps-nuvem/AulaViva_lp2_index.html", f"{REPO}/apps-nuvem/AulaViva_lp2_index.html")
cp(f"{HERE}/old_pager/apps-offline/AulaViva_PI-I_offline.html", f"{REPO}/apps-offline/AulaViva_PI-I_offline.html")
cp(f"{HERE}/old_pager/apps-offline/AulaViva_LP2_offline.html", f"{REPO}/apps-offline/AulaViva_LP2_offline.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg5.txt")

# commit 6 — privacidade: material só da professora some da lista do aluno
cp(f"{ROOT}/redserver/api_v2.php", f"{REPO}/aulaviva/api.php")
cp(f"{HERE}/old_preauth/AulaViva_pi1_index.html", f"{REPO}/apps-nuvem/AulaViva_pi1_index.html")
cp(f"{HERE}/old_preauth/AulaViva_lp2_index.html", f"{REPO}/apps-nuvem/AulaViva_lp2_index.html")
cp(f"{HERE}/old_preauth/off_pi1.html", f"{REPO}/apps-offline/AulaViva_PI-I_offline.html")
cp(f"{HERE}/old_preauth/off_lp2.html", f"{REPO}/apps-offline/AulaViva_LP2_offline.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg6.txt")

# commit 7 — entrada: raiz do kit → app (login nome+senha) + acolhida na 1ª vez
cp(f"{HERE}/extra/index.php", f"{REPO}/index.php")
cp(f"{KIT}/AulaViva_pi1_index.html", f"{REPO}/apps-nuvem/AulaViva_pi1_index.html")
cp(f"{KIT}/AulaViva_lp2_index.html", f"{REPO}/apps-nuvem/AulaViva_lp2_index.html")
cp(f"{ROOT}/output/AulaViva_Programacao_para_Internet_I.html", f"{REPO}/apps-offline/AulaViva_PI-I_offline.html")
cp(f"{ROOT}/output/AulaViva_Linguagem_de_Programacao_II.html", f"{REPO}/apps-offline/AulaViva_LP2_offline.html")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg7.txt")

# commit 8 — túnel cloudflared sem tela de aviso + notas de deploy
cp(f"{ROOT}/redserver/tunel/sobe-tunel.sh",             f"{REPO}/redserver/tunel/sobe-tunel.sh")
cp(f"{ROOT}/redserver/tunel/tunel-cloudflared.service", f"{REPO}/redserver/tunel/tunel-cloudflared.service")
cp(f"{ROOT}/redserver/tunel/LEIA-ME_TUNEL.md",          f"{REPO}/redserver/tunel/LEIA-ME_TUNEL.md")
cp(f"{ROOT}/videoaulas/LEIA-ME_MEDIA.md",               f"{REPO}/videoaulas/LEIA-ME_MEDIA.md")
sh("git", "add", "-A"); sh("git", "commit", "-F", f"{HERE}/msg8.txt")

# ---------- patches + diff ----------
sh("git", "format-patch", "master", "-o", os.path.join(PR, "patches"))
diff = subprocess.run(["git", "diff", "master", BR, "--stat"], capture_output=True, text=True, cwd=REPO).stdout
open(os.path.join(PR, "PR_completo.diff"), "w", encoding="utf-8").write(
    subprocess.run(["git", "diff", "master", BR], capture_output=True, text=True, cwd=REPO).stdout)

# ---------- anexo: DEPLOY_NOTES novo (fora dos patches: o master real tem usuário/IP
# ---------- do servidor e eles vazariam pelas linhas de contexto do diff) ----------
os.makedirs(os.path.join(PR, "extras"), exist_ok=True)
cp(f"{ROOT}/redserver/DEPLOY_NOTES.md", os.path.join(PR, "extras", "DEPLOY_NOTES.md"))
# checklist imprimível de deploy (1 página) — gerado por video_tools/gerar_checklist_deploy.py
cp(os.path.join(HERE, "pr_docs", "Checklist_Deploy_PR_AulaViva_v2.pdf"),
   os.path.join(PR, "extras", "Checklist_Deploy_PR_AulaViva_v2.pdf"))

# ---------- docs do PR (versão canônica em pr_docs/, sobrevive ao rmtree) ----------
for doc in ("PR_DESCRICAO.md", "LEIA-ME_PR.md"):
    cp(os.path.join(HERE, "pr_docs", doc), os.path.join(PR, doc))

# ---------- árvore final da branch (fallback manual) ----------
arb = os.path.join(PR, "arquivos_branch")
for rootd, _, files in os.walk(REPO):
    if ".git" in rootd: continue
    for f in files:
        fp = os.path.join(rootd, f)
        cp(fp, os.path.join(arb, os.path.relpath(fp, REPO)))

print("LOG:")
print(sh("git", "log", "--oneline", "--decorate"))
print("\nDIFFSTAT:"); print(diff)
print("PATCHES:", sorted(os.listdir(os.path.join(PR, "patches"))))
