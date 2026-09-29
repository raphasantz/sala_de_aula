# -*- coding: utf-8 -*-
"""Cronograma PI-I v2 — nas DATAS REAIS enviadas pela professora (46 linhas).
Atividades = conteúdo das 72 aulas oficiais, agrupado por encontro real.
Sábados letivos marcados = postagem da matéria no portal (AVA)."""
import datetime as dt
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gerar_cronogramas import build_docx, build_pdf   # reaproveita o layout do modelo

D = lambda d, m, y=2026: dt.date(y, m, d)

SAB = "sabado letivo - postar a materia no portal"
# cada item: (data, índices das atividades do arquivo original OU 'SAB')
MAPA = [
    (D(3,10),  [0, 1]),
    (D(5,10),  [2, 3]),
    (D(6,10),  [4]),
    (D(6,10),  [5]),
    (D(10,10), SAB),
    (D(19,10), [6, 7]),
    (D(20,10), [8]),
    (D(20,10), [9, 10]),
    (D(24,10), SAB),
    (D(26,10), [11]),
    (D(27,10), [12, 13]),
    (D(27,10), [14]),
    (D(31,10), SAB),
    (D(3,11),  [15, 16]),
    (D(3,11),  [17]),
    (D(7,11),  SAB),
    (D(9,11),  [18, 19]),
    (D(10,11), [20]),
    (D(10,11), [21, 22]),
    (D(16,11), [23]),
    (D(17,11), [24, 25]),
    (D(17,11), [26, 27]),
    (D(23,11), [28, 29]),
    (D(24,11), [30, 31]),
    (D(24,11), [32, 33]),
    (D(30,11), [34, 35]),
    (D(1,12),  [36, 37]),
    (D(1,12),  [38, 39]),
    (D(7,12),  [40, 41]),
    (D(8,12),  [42, 43]),
    (D(8,12),  [44, 45]),
    (D(14,12), [46, 47]),
    (D(15,12), [48, 49]),
    (D(15,12), [50, 51]),
    (D(1,2,2027),  [52, 53]),
    (D(2,2,2027),  [54, 55]),
    (D(2,2,2027),  [56, 57]),
    (D(15,2,2027), [58, 59]),
    (D(16,2,2027), [60, 61]),
    (D(16,2,2027), [62, 63]),
    (D(22,2,2027), [64, 65]),
    (D(23,2,2027), [66, 67]),
    (D(23,2,2027), [68]),
    (D(1,3,2027),  [69]),
    (D(2,3,2027),  [70]),
    (D(2,3,2027),  [71]),
]
from gerar_cronogramas import PI1_TEMAS
LINHAS = []
for d, at in MAPA:
    if at == SAB:
        LINHAS.append((d, SAB))
    else:
        LINHAS.append((d, "  •  ".join(PI1_TEMAS[i] for i in at)))


OBS = ("Replanejado conforme calendário real informado pela docente: encontros de "
       "segunda (1 aula), terça (2 aulas) e sábados letivos de postagem no portal (AVA). "
       "Sem aula em: 12/10, 02/11, 20/11/2026; 08–10/02/2027 (recesso); férias de janeiro/2027. "
       "Carga complementar: 10 h não presenciais distribuídas nas postagens de sábado e tarefas do AVA.")

PER = "2026/02 — replanejado conforme calendário real (03/10/2026 a 02/03/2027)"
build_docx("Programação para Internet I", [d for d, _ in LINHAS],
           [a for _, a in LINHAS], "Cronograma_Preenchido_PI-I.docx", OBS, PER)
build_pdf("Programação para Internet I", [d for d, _ in LINHAS],
          [a for _, a in LINHAS], "Cronograma_Preenchido_PI-I.pdf", OBS, PER)
print("PI-I v2: 46 linhas ·", LINHAS[0][0].strftime("%d/%m/%Y"), "→", LINHAS[-1][0].strftime("%d/%m/%Y"))
