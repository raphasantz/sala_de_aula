# -*- coding: utf-8 -*-
"""Guia em PDF, em língua de gente: o link da turma com Cloudflared (sem precisar
saber usar a Cloudflare). Uso: python3 video_tools/gerar_guia_tunel.py"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
                                Table, TableStyle)
from reportlab.lib.styles import ParagraphStyle

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
F = os.path.join(ROOT, "fonts")
for n, arq in (("R", "Inter-Regular.ttf"), ("B", "Inter-Bold.ttf"),
               ("S", "Inter-SemiBold.ttf"), ("M", "JetBrainsMono-Regular.ttf")):
    pdfmetrics.registerFont(TTFont("Inter" + n, os.path.join(F, arq)))

NAVY = HexColor("#12263a"); AMB = HexColor("#f2a33c"); MUT = HexColor("#6b7a8d")
GRN = HexColor("#1e7b34"); RED = HexColor("#c0392b")

tit = ParagraphStyle("t", fontName="InterB", fontSize=23, textColor=NAVY, leading=28)
sub = ParagraphStyle("s", fontName="InterR", fontSize=11.5, textColor=MUT, leading=16)
h2 = ParagraphStyle("h2", fontName="InterB", fontSize=14, textColor=NAVY, leading=18,
                    spaceBefore=12, spaceAfter=4)
bd = ParagraphStyle("bd", fontName="InterR", fontSize=11.5, textColor=HexColor("#1f2937"),
                    leading=16.5, leftIndent=6, spaceAfter=4)
mono = ParagraphStyle("mo", fontName="InterM", fontSize=10.5, textColor=HexColor("#16202e"),
                      leading=15, leftIndent=10, spaceAfter=6,
                      backColor=HexColor("#eef2f6"), borderPadding=4)
ok = ParagraphStyle("ok", fontName="InterS", fontSize=11, textColor=GRN, leading=15,
                    spaceAfter=4, leftIndent=6)

doc = SimpleDocTemplate(os.path.join(ROOT, "output", "Guia_Do_Link_Sem_Misterio_Cloudflared.pdf"),
                        pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                        topMargin=16 * mm, bottomMargin=16 * mm,
                        title="Guia do link sem mistério (Cloudflared)")
E = []
E.append(Paragraph("O link da turma, sem mistério e sem painel", tit))
E.append(Spacer(1, 3))
E.append(Paragraph("Cloudflared para quem tem conta na Cloudflare e não sabe (e não precisa!) usar · "
                   "Kit Sala de Aula · Turma 2/2026", sub))
E.append(HRFlowable(width="100%", thickness=2, color=AMB, spaceBefore=8, spaceAfter=12))

E.append(Paragraph("A boa notícia primeiro", h2))
E.append(Paragraph("Para o link da turma funcionar, <b>você não abre o site da Cloudflare, "
                   "não entra em painel nenhum e não configura nada</b>. A conta que você já "
                   "tem é útil só para um opcional de luxo (um link fixo), explicado no final. "
                   "Quem faz o serviço é um programinha no servidor, o <b>cloudflared</b>: ele "
                   "abre a porta entre o servidor da escola e a Internet e devolve um link prontinho.", bd))

E.append(Paragraph("O passo a passo (3 movimentos)", h2))
E.append(Paragraph("1. No servidor da escola, rodar UM comando (pode pedir ao Rapha):", bd))
E.append(Paragraph("sudo bash redserver/tunel/sobe-tunel.sh", mono))
E.append(Paragraph("2. O comando imprime o link na tela (e guarda uma cópia em "
                   "<font name='InterM'>/root/url-tunel.txt</font>). O link parece assim:", bd))
E.append(Paragraph("https://nome-sortido.trycloudflare.com/KiT_Sala_de_Aula/", mono))
E.append(Paragraph("3. Copiar o link, colar no grupo da turma e testar no seu celular "
                   "com o 4G (fora do wi-fi da escola).", bd))
E.append(Paragraph("Se caiu DIRETO na tela de nome + senha do aluno: está perfeito. "
                   "É exatamente isso que queríamos — sem nenhuma tela de aviso no meio "
                   "(era isso que o ngrok fazia).", ok))

E.append(Paragraph("Perguntas que você ia me fazer", h2))
E.append(Paragraph("<b>• O link muda?</b> No plano grátis, sim: a cada reinício do túnel ele "
                   "sorteia um nome novo (o final /KiT_Sala_de_Aula/ é sempre o mesmo). "
                   "Se o servidor reiniciar, rode o comando de novo e mande o link novo no grupo. "
                   "Leva 10 segundos.", bd))
E.append(Paragraph("<b>• E a minha conta da Cloudflare?</b> Só entra em cena se um dia você "
                   "quiser um link fixo, do tipo aula.seudominio.com.br, que nunca muda. "
                   "Aí sim se usa a conta (num comando chamado “tunnel login”, com o Rapha do lado). "
                   "Enquanto isso: não precisa de nada dela.", bd))
E.append(Paragraph("<b>• Posso deixar ligado para sempre?</b> Pode: existe um modo “serviço” "
                   "(systemd) que religa sozinho junto com o servidor. Está tudo escrito no "
                   "LEIA-ME_TUNEL.md que vai no pacote, em língua de gente também.", bd))
E.append(Paragraph("<b>• E o ngrok antigo?</b> Só desligue DEPOIS de testar o link novo no 4G. "
                   "Um de cada vez, sem pressa.", bd))

E.append(Paragraph("Checklist da Juh", h2))
chk = [["☐", "Comando rodado no servidor, link impresso/salvo"],
       ["☐", "Link aberto no celular (4G): caiu direto no login nome + senha"],
       ["☐", "Vídeo da videoaula abriu pelo cartão de videoaula dentro do app"],
       ["☐", "Link colado no grupo da turma"],
       ["☐", "ngrok desligado só depois do teste ok"]]
t = Table(chk, colWidths=[10 * mm, 150 * mm])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "InterB"),
    ("FONTNAME", (1, 0), (1, -1), "InterR"),
    ("FONTSIZE", (0, 0), (-1, -1), 11.5),
    ("TEXTCOLOR", (0, 0), (0, -1), NAVY),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
]))
E.append(t)
E.append(Spacer(1, 10))
E.append(Paragraph("Qualquer tela estranha: print e me manda. A gente resolve junto, como sempre.", bd))
doc.build(E)
print("OK: output/Guia_Do_Link_Sem_Misterio_Cloudflared.pdf")
