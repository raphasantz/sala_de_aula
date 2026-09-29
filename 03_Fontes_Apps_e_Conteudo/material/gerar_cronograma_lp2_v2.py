# -*- coding: utf-8 -*-
"""Cronograma LP2 v2 — nas DATAS REAIS da professora (58 linhas).
Atividades = texto verbatim do Cronograma_Preenchido_LP2 (96 etapas),
encaixadas em ordem nos encontros presenciais; sábados = texto exato dela."""
import datetime as dt
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gerar_cronogramas import build_docx, build_pdf, LP2_ATIV

D = lambda d, m, y=2026: dt.date(y, m, d)

# (data, texto-do-sábado ou None para encontro presencial)
DATAS = [
    (D(2,10),  None), (D(2,10),  None),
    (D(7,10),  None), (D(7,10),  None),
    (D(9,10),  None), (D(9,10),  None),
    (D(21,10), None), (D(21,10), None),
    (D(23,10), None), (D(23,10), None),
    (D(28,10), None), (D(28,10), None),
    (D(30,10), None), (D(30,10), None),
    (D(4,11),  None), (D(4,11),  None),
    (D(6,11),  None), (D(6,11),  None),
    (D(11,11), None), (D(11,11), None),
    (D(13,11), None), (D(13,11), None),
    (D(14,11), "Sabado Letivo - conteudo e atividade"),
    (D(18,11), None), (D(18,11), None),
    (D(25,11), None), (D(25,11), None),
    (D(27,11), None), (D(27,11), None),
    (D(28,11), "sabado letivo - conteudo e atividade"),
    (D(2,12),  None), (D(2,12),  None),
    (D(4,12),  None), (D(4,12),  None),
    (D(5,12),  "sabado letivo - atividade e conteudo"),
    (D(9,12),  None), (D(9,12),  None),
    (D(11,12), None), (D(11,12), None),
    (D(16,12), None), (D(16,12), None),
    (D(18,12), None), (D(18,12), None),
    (D(3,2,2027), None), (D(3,2,2027), None),
    (D(5,2,2027), None), (D(5,2,2027), None),
    (D(6,2,2027), "sabado letivo - atividade e conteudo"),
    (D(13,2,2027), "sabado letivo - atividade e conteudo"),
    (D(17,2,2027), None), (D(17,2,2027), None),
    (D(19,2,2027), None), (D(19,2,2027), None),
    (D(20,2,2027), "sabado letivo - atividade e conteudo"),
    (D(26,2,2027), None), (D(26,2,2027), None),
    (D(3,3,2027), None), (D(3,3,2027), None),
]

presenciais = sum(1 for _, s in DATAS if s is None)
assert presenciais <= len(LP2_ATIV), (presenciais, len(LP2_ATIV))

LINHAS = []
i = 0
np = 0
A = len(LP2_ATIV)
for d, sab in DATAS:
    if sab:
        LINHAS.append((d, sab))
        continue
    rest_linhas = presenciais - np
    rest_ativ = A - i
    take = 2 if rest_ativ > rest_linhas else 1
    LINHAS.append((d, "  •  ".join(LP2_ATIV[i:i+take])))
    i += take
    np += 1
assert i == A, (i, A)

OBS = ("Replanejado conforme calendário real informado pela docente: encontros de "
       "quarta (2 aulas) e sexta (2 aulas) + sábados letivos com conteúdo/atividade no portal. "
       "Sem aula em: 12 e 13/10, 02/11, 20/11/2026; 08–10/02/2027 (recesso); férias de janeiro/2027. "
       "Carga complementar: 14 h não presenciais distribuídas nos sábados letivos e tarefas do AVA.")
PER = "2026/02 — replanejado conforme calendário real (02/10/2026 a 03/03/2027)"

build_docx("Linguagem de Programação II", [d for d, _ in LINHAS],
           [a for _, a in LINHAS], "Cronograma_Preenchido_LP2.docx", OBS, PER)
build_pdf("Linguagem de Programação II", [d for d, _ in LINHAS],
          [a for _, a in LINHAS], "Cronograma_Preenchido_LP2.pdf", OBS, PER)
print(f"LP2 v2: {len(LINHAS)} linhas ({presenciais} presenciais + {len(LINHAS)-presenciais} sábados) · "
      f"{DATAS[0][0].strftime('%d/%m/%Y')} → {DATAS[-1][0].strftime('%d/%m/%Y')} · "
      f"{A} atividades encaixadas")
