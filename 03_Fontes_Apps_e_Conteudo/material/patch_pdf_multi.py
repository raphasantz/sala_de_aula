# -*- coding: utf-8 -*-
"""Aplica patches de multidisciplina no build_pdf.py (com diagnóstico por item)."""
import io

p = 'build_pdf.py'
s = io.open(p, encoding='utf-8').read()

R = [
 ('import',
  'from conteudo import (MODULOS, MODULOS_POR_NUM, GLOSSARIO, comuns, avaliacoes)',
  'import importlib as _il\n'
  '_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))\n'
  'MODULOS = _PKG.MODULOS\n'
  'MODULOS_POR_NUM = _PKG.MODULOS_POR_NUM\n'
  'GLOSSARIO = _PKG.GLOSSARIO\n'
  'comuns = _PKG.comuns\n'
  'avaliacoes = _PKG.avaliacoes'),
 ('ordem',
  '    ordem_partes = {1: [1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9], 4: [11], 5: [10], 6: [12]}',
  '    ordem_partes = comuns.ORDEM_PARTES'),
 ('notas',
  'story += part_divider(parte, mods_info, note=notas.get(parte["num"]))',
  'story += part_divider(parte, mods_info, note=comuns.NOTAS_PARTES.get(parte["num"]))'),
 ('kicker',
  'Paragraph("CURSO TÉCNICO EM INFORMÁTICA · EIXO: INFORMAÇÃO E COMUNICAÇÃO",',
  'Paragraph(comuns.META["kicker"],'),
 ('titulo_capa',
  'Paragraph("PROGRAMAÇÃO<br/>PARA INTERNET I", S["cap"]),',
  'Paragraph(comuns.META["titulo_capa"], S["cap"]),'),
 ('sub_capa',
  'Paragraph("Apostila completa da disciplina — teoria aula a aula, exercícios "\n                  "práticos, testes rápidos e avaliações (A1 · A2 · A3)", S["cap2"]),',
  'Paragraph(comuns.META["sub_capa"], S["cap2"]),'),
 ('header',
  'c.drawString(ML, PAGE_H - 0.95 * cm, "PROGRAMAÇÃO PARA INTERNET I — APOSTILA COMPLETA")',
  'c.drawString(ML, PAGE_H - 0.95 * cm, comuns.META["header"])'),
 ('rodape',
  'c.drawCentredString(PAGE_W / 2 + 1.2 * cm, MB - 0.95 * cm, "(S) = proposta pedagógica")',
  'c.drawCentredString(PAGE_W / 2 + 1.2 * cm, MB - 0.95 * cm, comuns.META.get("rodape", "(S) = proposta pedagógica"))'),
 ('fecho',
  'Paragraph("Programação para Internet I · Curso Técnico em Informática · Turma 2/2026 — "\n                                "material elaborado a partir do Plano de Ensino e Cronograma oficiais. "\n                                "Itens marcados com (S) são propostas pedagógicas de organização.",',
  'Paragraph(comuns.META["fecho"],'),
 ('saida',
  '    build(False, os.path.join(_ROOT, "output", "Apostila_Programacao_para_Internet_I_ALUNO.pdf"))\n    build(True, os.path.join(_ROOT, "output", "Apostila_Programacao_para_Internet_I_PROFESSOR.pdf"))',
  '    suf = comuns.META["slug"]\n    build(False, os.path.join(_ROOT, "output", f"Apostila_{suf}_ALUNO.pdf"))\n    build(True, os.path.join(_ROOT, "output", f"Apostila_{suf}_PROFESSOR.pdf"))'),
 ('doctitle',
  'title="Programação para Internet I — Apostila Completa ("',
  'title=comuns.META["titulo_doc"] + " — Apostila Completa ("'),
]

falhas = []
for nome, old, new in R:
    if old in s:
        s = s.replace(old, new, 1)
    else:
        falhas.append(nome)
io.open(p, 'w', encoding='utf-8').write(s)
print("aplicados:", [n for n, _, _ in R if n not in falhas])
print("FALHAS:", falhas)
