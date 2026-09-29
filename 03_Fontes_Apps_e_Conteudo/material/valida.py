# -*- coding: utf-8 -*-
"""Valida todas as strings renderizáveis com o paraparser do reportlab."""
import os, sys, re
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from build_pdf import safe_para
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from conteudo import MODULOS, GLOSSARIO, comuns, avaliacoes

st = ParagraphStyle("t", fontName="Helvetica", fontSize=9, leading=12)
errors = []

def check(s, ctx):
    if not isinstance(s, str):
        return
    try:
        Paragraph(safe_para(s), st)
    except Exception as e:
        errors.append((ctx, str(e)[:180], s[:100]))

def walk(o, ctx="", skip_keys=("linhas", "resposta_codigo", "slides")):
    if isinstance(o, str):
        check(o, ctx)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in skip_keys:
                continue
            if k == "codigo" and isinstance(v, list):
                continue  # linhas de código puras (provas)
            walk(v, f"{ctx}.{k}", skip_keys)
    elif isinstance(o, (list, tuple)):
        for i, v in enumerate(o):
            walk(v, f"{ctx}[{i}]", skip_keys)

walk(comuns.APRESENTACAO, "APRES")
walk(comuns.COMO_USAR_ICONES, "ICONS")
walk(comuns.METODOLOGIA, "MET"); walk(comuns.RECURSOS, "REC")
walk(comuns.ATIVIDADES_EXTRACLASSE, "EXTRA")
walk(comuns.AVALIACOES_RESUMO, "AVRES")
walk(comuns.MAPA_MODULOS, "MAPA"); walk(comuns.EMENTA, "EMENTA")
walk(comuns.CURSO, "CURSO")
walk(comuns.BIBLIOGRAFIA_BASICA, "BIB"); walk(comuns.BIBLIOGRAFIA_COMPLEMENTAR, "BIB2")
walk(MODULOS, "MOD")
walk(GLOSSARIO, "GLOSS")
walk(avaliacoes.PROJETO_FINAL, "PF")
walk(avaliacoes.A1, "A1"); walk(avaliacoes.A2, "A2"); walk(avaliacoes.A3, "A3")

print(f"{len(errors)} erros de paraparser")
for ctx, err, frag in errors:
    print("---", ctx)
    print("   ", err)
    print("   texto:", repr(frag))
