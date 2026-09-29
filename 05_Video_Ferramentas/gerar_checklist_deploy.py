#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera 'Checklist_Deploy_PR_AulaViva_v2.pdf' — a página única que responde:
"so subir o pr ja resolve?" -> NAO. Merge = codigo no repo; deploy = 7 passos no servidor.
Sem emoji (reportlab/Helvetica), sem credenciais reais.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


def simpleSplit(texto, fonte, tamanho, largura):
    linhas = []
    for par in texto.split('\n'):
        palavras = par.split(' ')
        atual = ''
        for w in palavras:
            teste = (atual + ' ' + w).strip()
            if stringWidth(teste, fonte, tamanho) <= largura or not atual:
                atual = teste
            else:
                linhas.append(atual)
                atual = w
        linhas.append(atual)
    return linhas

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SAIDA = os.path.join(RAIZ, "output", "Checklist_Deploy_PR_AulaViva_v2.pdf")
SAIDA2 = os.path.join(RAIZ, "pr_work", "pr_docs", "Checklist_Deploy_PR_AulaViva_v2.pdf")  # canonico: make_repo copia p/ PR/extras/

AZUL = colors.HexColor("#123a6b")
OURO = colors.HexColor("#b8860b")
CINZA = colors.HexColor("#444444")
FUNDO = colors.HexColor("#f2f5fa")


def cab(c, y):
    c.setFillColor(AZUL)
    c.rect(0, y - 16 * mm, 210 * mm, 16 * mm, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(15 * mm, y - 9 * mm, "Deploy do AulaViva v2 - checklist do Rapha")
    c.setFont("Helvetica", 9.5)
    c.drawString(15 * mm, y - 13.5 * mm,
                 "Subir/mergear o PR NAO coloca nada no ar. O PR entrega o codigo; "
                 "o ar muda so depois da ETAPA 3.")
    return y - 22 * mm


def secao(c, y, titulo, cor=AZUL):
    c.setFillColor(cor)
    c.rect(13 * mm, y - 5.2 * mm, 184 * mm, 5.6 * mm, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(15 * mm, y - 3.9 * mm, titulo)
    return y - 9.6 * mm


def item(c, y, num, texto, negrito=False, cor=CINZA, recuo=20 * mm):
    c.setFillColor(OURO)
    c.setFont("Helvetica-Bold", 9)
    c.rect(14 * mm, y - 3.1 * mm, 3.4 * mm, 3.4 * mm, stroke=0, fill=1)
    c.setFillColor(cor)
    c.setFont("Helvetica-Bold" if negrito else "Helvetica", 9)
    c.drawString(recuo, y - 2.5 * mm, num)
    c.setFont("Helvetica-Bold" if negrito else "Helvetica", 9)
    fonte = 'Helvetica-Bold' if negrito else 'Helvetica'
    linhas = simpleSplit(texto, fonte, 9, 210 * mm - recuo - 14 * mm)
    for i, ln in enumerate(linhas):
        c.drawString(recuo + 8 * mm, y - 2.5 * mm - i * 3.95 * mm, ln)
    return y - 2.5 * mm - len(linhas) * 3.95 * mm - 0.9 * mm


def nota(c, y, titulo, linhas):
    alt = 5.6 * mm + len(linhas) * 4.0 * mm
    c.setFillColor(FUNDO)
    c.setStrokeColor(OURO)
    c.setLineWidth(0.7)
    c.rect(13 * mm, y - alt, 184 * mm, alt, stroke=1, fill=1)
    c.setFillColor(AZUL)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(16 * mm, y - 4.6 * mm, titulo)
    c.setFillColor(CINZA)
    c.setFont("Helvetica", 8.6)
    for i, ln in enumerate(linhas):
        c.drawString(16 * mm, y - 8.8 * mm - i * 4.0 * mm, ln)
    return y - alt - 4 * mm


def build():
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    c = canvas.Canvas(SAIDA, pagesize=A4)
    y = 297 * mm
    y = cab(c, y)

    y = secao(c, y, "ETAPA 1 - Levar a branch pro GitHub (5 min)")
    y = item(c, y, "1.", "Descompactar output/PR_AulaViva_v2.zip")
    y = item(c, y, "2.", "git checkout -b feature/rapida-aulaviva-v2  e  git am patches/*.patch (8 commits)")
    y = item(c, y, "3.", "Se o git am reclamar de conflito: git am --abort e usar a Opcao B "
                       "(copiar arquivos_branch/ por cima) - esta no LEIA-ME_PR.md")
    y = item(c, y, "4.", "git push -u origin feature/rapida-aulaviva-v2  ->  abrir o PR colando PR_DESCRICAO.md")

    y = secao(c, y, "ETAPA 2 - Merge (ainda nao mudou nada no ar)")
    y = item(c, y, "5.", "Revisar PR_completo.diff e mergear em master (nunca push direto em master)")
    y = item(c, y, "6.", "Copiar extras/DEPLOY_NOTES.md para redserver/DEPLOY_NOTES.md "
                       "(fica fora dos patches de proposito: tem usuario/IP do servidor)")
    y += 1.2 * mm

    y = secao(c, y, "ETAPA 3 - Deploy no redserver: e AQUI que o ar muda (o que o git NAO leva)", OURO)
    y = item(c, y, "7.", "Banco: mysql -u root -p loja_turma < aulaviva/migracao_contas_entregas.sql "
                       "(idempotente; migração do v1 e opcional, comentada no fim do SQL)", negrito=True)
    y = item(c, y, "8.", "Pastas: mkdir -p aulaviva/materiais/{pi1,lp2} aulaviva/entregas/{pi1,lp2} "
                       "+ chown -R www-data:www-data materiais entregas", negrito=True)
    y = item(c, y, "9.", "php-fpm (pool do vhost): env[LOJA_DB_PASS] e env[AULAVIVA_PROF_TOKEN] com TOKEN NOVO "
                       "(rotacionar o antigo, que circulou em docs) + restart do php-fpm", negrito=True)
    y = item(c, y, "10.", "scp: aulaviva/api.php (novo) + index.php da RAIZ do kit (porta de entrada: "
                        "302 para o app; ?d=lp2 leva a LP2)", negrito=True)
    y = item(c, y, "11.", "scp: os 4 HTML de apps-nuvem/ (2 apps + 2 paineis) e, para o pendrive, "
                        "os 2 de apps-offline/", negrito=True)
    y = item(c, y, "12.", "scp da pasta videoaulas/ para a raiz do kit (irma dos apps): 2 mp4 + 2 PDF "
                        "passo a passo + audio/ . Binario NUNCA vai no git.", negrito=True)
    y = item(c, y, "13.", "Conferir permissao de escrita do www-data em entregas/ e materiais/ "
                        "(upload sem 500) e md5 dos arquivos enviados")
    y = item(c, y, "14.", "Tunel: redserver/tunel/sobe-tunel.sh (cloudflared) no lugar do ngrok - "
                        "link em /root/url-tunel.txt; muda a cada subida")

    y = secao(c, y, "ETAPA 4 - Teste de aceite (10 min, checklist completo na PR_DESCRICAO.md)")
    y = item(c, y, "15.", "reg cria conta -> login -> get/put round-trip; put sem cookie da 401")
    y = item(c, y, "16.", "LP2: conta criada na LP2 nao aparece no painel da PI-I; titulo do app LP2 certo "
                        "(o sed de hotfix da v1 vira desnecessario)")
    y = item(c, y, "17.", "Alternativas com <head>/<title> aparecem como texto (nao somem mais)")
    y = item(c, y, "18.", "Entrega de arquivo -> aparece no painel -> download via dlent; .exe/.zip recusado")
    y = item(c, y, "19.", "Aluno comum nao ve Painel do Professor / Guia da Professora / Apostila do Professor; "
                        "a conta ADM (Juh) ve tudo")
    y = item(c, y, "20.", "Videoaula abre no cartao da trilha; paginador Pagina X de Y confere; "
                        "botao de resolucao dos exercicios da LP2 (Modulo 1) abre o gabarito")
    y = item(c, y, "21.", "Celular 640px e Modo Turma 641-900px sem quebrar; apagar residuos qa_* do banco")

    y = nota(c, y, "Duas coisas que o merge nao resolve sozinho", [
        "- Audio por modulo: o botao so aparece se existir videoaulas/audio/<disc>_mNN.mp3. A pasta esta VAZIA",
        "  hoje (PI-I 12 modulos + LP2 15 = 27 clips a gerar) - entao nenhum botao orfao aparece, e so esperar.",
        "- Aviso aos alunos: quem estiver com a aba do AulaViva v1 aberta recarrega uma vez (o put do v2 exige sessao).",
        "- Enquanto a v2 nao sobe: output/Hotfix_v1_tags_HTML.zip conserta o bug das alternativas na v1 em producao.",
    ])

    c.setFillColor(CINZA)
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(15 * mm, 9 * mm,
                 "Resumo em uma frase: PR = codigo versionado. Deploy (SQL + pastas + env + scp dos HTML/index.php/videoaulas) = aula funcionando.")
    print("Y FINAL (mm):", round(y / mm, 1))
    c.showPage()
    c.save()
    for p in (SAIDA, SAIDA2):
        os.makedirs(os.path.dirname(p), exist_ok=True)
    import shutil
    shutil.copyfile(SAIDA, SAIDA2)
    print("ok:", SAIDA, os.path.getsize(SAIDA), "bytes")
    print("copia:", SAIDA2)


if __name__ == "__main__":
    build()
