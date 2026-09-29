# -*- coding: utf-8 -*-
"""Torna build_pptx, build_quiz_app e build_aula_app multidisciplina."""
import io

def patch(p, R):
    s = io.open(p, encoding='utf-8').read()
    falhas = []
    for nome, old, new in R:
        if old in s:
            s = s.replace(old, new, 1)
        else:
            falhas.append(nome)
    io.open(p, 'w', encoding='utf-8').write(s)
    print(p, "-> falhas:", falhas or "nenhuma")

# ---------------------------------------------------------------- PPTX
patch('build_pptx.py', [
 ('import', 'from conteudo import MODULOS, MODULOS_POR_NUM, comuns, avaliacoes',
  'import importlib as _il\n'
  '_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))\n'
  'MODULOS = _PKG.MODULOS\nMODULOS_POR_NUM = _PKG.MODULOS_POR_NUM\n'
  'comuns = _PKG.comuns\navaliacoes = _PKG.avaliacoes'),
 ('ordem', '    ordem_partes = {1: [1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9], 4: [11], 5: [10], 6: [12]}',
  '    ordem_partes = comuns.ORDEM_PARTES'),
 ('footer', 'setp(tf.paragraphs[0], "PROGRAMAÇÃO PARA INTERNET I · CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026"\n         + (("  ·  " + label) if label else ""), size=9, color=SOFT, space_after=0)',
  'setp(tf.paragraphs[0], comuns.META["pptx_footer"]\n         + (("  ·  " + label) if label else ""), size=9, color=SOFT, space_after=0)'),
 ('capa_kick', 'setp(tf.paragraphs[0], "CURSO TÉCNICO EM INFORMÁTICA · EIXO: INFORMAÇÃO E COMUNICAÇÃO",\n         size=13, color=AMBER, bold=True, space_after=0)',
  'setp(tf.paragraphs[0], comuns.META["kicker"], size=13, color=AMBER, bold=True, space_after=0)'),
 ('capa_t1', 'setp(tf.paragraphs[0], "PROGRAMAÇÃO", size=54, color=WHITE, bold=True, space_after=0)\n    p = tf.add_paragraph(); setp(p, "PARA INTERNET I", size=54, color=WHITE, bold=True, space_after=0)',
  'setp(tf.paragraphs[0], comuns.META["pptx_capa1"], size=54, color=WHITE, bold=True, space_after=0)\n    p = tf.add_paragraph(); setp(p, comuns.META["pptx_capa2"], size=54, color=WHITE, bold=True, space_after=0)'),
 ('capa_sub', 'setp(tf.paragraphs[0], "Apresentação de aulas — teoria, exercícios práticos, testes rápidos "\n         "e avaliações (A1 · A2 · A3)", size=17, color=SKY_TXT, space_after=0)',
  'setp(tf.paragraphs[0], comuns.META["pptx_sub"], size=17, color=SKY_TXT, space_after=0)'),
 ('capa_ft', 'setp(tf.paragraphs[0], "Material baseado no Plano de Ensino e no Cronograma oficiais · Turma 2/2026",\n         size=10.5, color=RGBColor(0x9F, 0xBB, 0xD9), space_after=0)',
  'setp(tf.paragraphs[0], comuns.META["pptx_rodape"], size=10.5, color=RGBColor(0x9F, 0xBB, 0xD9), space_after=0)'),
 ('front', '''    slide_front(prs, nxt(), "Bem-vindos à disciplina", "O curso em 1 minuto",
                ["Programação para Internet I — Curso Técnico em Informática (Turma 2/2026)",
                 "72 aulas em 24 semanas · 3 aulas semanais de 50 minutos",
                 "60 h presenciais (teoria + prática) e 10 h de atividades orientadas no AVA",
                 "Do zero ao projeto final: Web → HTML → PHP → formulários → sistema completo",
                 "Aulas dialogadas, muita prática no laboratório e projeto integrador em grupos"],
                sub="Ementa oficial: desenvolvimento de projetos de website, HTML e linguagem PHP.")''',
  '''    f0 = comuns.FRONT[0]
    slide_front(prs, nxt(), f0["kick"], f0["tit"], f0["bullets"], sub=f0["sub"])'''),
 ('front2', '''    slide_front(prs, nxt(), "Como funcionam as aulas", "Teoria + prática + testes rápidos",
                ["Teoria aula a aula: conceitos com exemplos, analogias e código ao vivo",
                 "Exercícios práticos em cada módulo (laboratório) e questões escritas",
                 "Teste rápido ao final de cada módulo: 5 questões para fixar na hora",
                 "Atividades no AVA (10 h): quizzes, leituras e continuidade dos projetos",
                 "Projetos: “Meu Primeiro Site” → site da empresa (A1) → cadastro PHP → projeto final"])''',
  '''    f1 = comuns.FRONT[1]
    slide_front(prs, nxt(), f1["kick"], f1["tit"], f1["bullets"])'''),
 ('front3', '''    slide_front(prs, nxt(), "Avaliações — 100 pontos", "A1 · A2 · A3",
                ["A1 (30 pts): site da empresa fictícia (10) + AVA/exercícios (5) + teste Web/HTML (15)",
                 "A2 (30 pts): prova na semana 16 — HTML, PHP e GET/POST (duplas/consulta conforme o Plano)",
                 "A3 (40 pts): prova final individual (30) + projeto e apresentação (10)",
                 "Apoio contínuo: revisões nas aulas 36 e 60, reforço no AVA e entregas do projeto",
                 "Modelos de prova e rubricas: seção AVALIAÇÕES da apostila"])''',
  '''    f2 = comuns.FRONT[2]
    slide_front(prs, nxt(), f2["kick"], f2["tit"], f2["bullets"])'''),
 ('front4', '''    slide_front(prs, nxt(), "Mapa do semestre", "Seis partes, doze módulos",
                [f"Parte {ROMAN[p['num']]} — {p['titulo']} ({p['aulas']}, {p['semanas']})"
                 for p in comuns.PARTES],
                sub="Cada parte abre um bloco de slides; os módulos trazem teoria, exercícios e teste rápido.")''',
  '''    f3 = comuns.FRONT[3]
    slide_front(prs, nxt(), f3["kick"], f3["tit"], f3["bullets"], sub=f3.get("sub"))'''),
 ('encerra', '''    setp(tf.paragraphs[0], "Programação para Internet I · Curso Técnico em Informática · Turma 2/2026",
         size=16, color=SKY_TXT, space_after=6)
    setp(tf.add_paragraph(), "Apostila (aluno e professor), testes rápidos e modelos de prova: "
         "disponíveis no material da disciplina.", size=14, color=SKY_TXT, space_after=0)''',
  '''    setp(tf.paragraphs[0], comuns.META["pptx_encerra1"], size=16, color=SKY_TXT, space_after=6)
    setp(tf.add_paragraph(), comuns.META["pptx_encerra2"], size=14, color=SKY_TXT, space_after=0)'''),
 ('saida', '    build(os.path.join(_ROOT, "output", "Apresentacao_Programacao_para_Internet_I.pptx"))',
  '    build(os.path.join(_ROOT, "output", f"Apresentacao_{comuns.META[\'slug\']}.pptx"))'),
])

# ---------------------------------------------------------------- QUIZWEB
patch('build_quiz_app.py', [
 ('import', 'from conteudo import MODULOS, MODULOS_POR_NUM\nfrom conteudo import quizzes_aulas as QA\nfrom conteudo import avaliacoes',
  'import importlib as _il\n'
  '_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))\n'
  'MODULOS = _PKG.MODULOS\nMODULOS_POR_NUM = _PKG.MODULOS_POR_NUM\n'
  'QA = _PKG.quizzes\navaliacoes = _PKG.avaliacoes'),
 ('titulo', '<title>QuizWeb — Programação para Internet I</title>',
  '<title>QuizWeb — __TITULO__</title>'),
 ('header', '<h1>🎯 QuizWeb · Programação para Internet I</h1>',
  '<h1>🎯 QuizWeb · __TITULO__</h1>'),
 ('chave', 'try{ if(v===undefined) return localStorage.getItem(k);',
  'try{ if(v===undefined) return localStorage.getItem(K+k);'),
 ('chave2', 'localStorage.setItem(k, v); }catch(e){ return null; } }',
  'localStorage.setItem(K+k, v); }catch(e){ return null; } }'),
 ('kdef', 'const app = document.getElementById("app");',
  'const K = "__KEY__";\nconst app = document.getElementById("app");'),
 ('saida', '    out = os.path.join(_ROOT, "output", "QuizWeb_Programacao_para_Internet_I.html")',
  '    out = os.path.join(_ROOT, "output", f"QuizWeb_{comuns.META['"'"'slug'"'"']}.html")'),
])

# ---------------------------------------------------------------- AULAVIVA
patch('build_aula_app.py', [
 ('import', 'from conteudo import MODULOS\nfrom conteudo import quizzes_aulas as QA',
  'import importlib as _il\n'
  '_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))\n'
  'MODULOS = _PKG.MODULOS\nQA = _PKG.quizzes'),
 ('titulo', '<title>AulaViva — Programação para Internet I</title>',
  '<title>AulaViva — __TITULO__</title>'),
 ('header', '<h1>🎓 AulaViva · Programação para Internet I</h1>',
  '<h1>🎓 AulaViva · __TITULO__</h1>'),
 ('chave', 'try{ const sv = localStorage.getItem("aulaviva"); if (sv) Object.assign(S, JSON.parse(sv)); }catch(e){}',
  'try{ const sv = localStorage.getItem(K); if (sv) Object.assign(S, JSON.parse(sv)); }catch(e){}'),
 ('chave2', 'try{ localStorage.setItem("aulaviva", JSON.stringify(',
  'try{ localStorage.setItem(K, JSON.stringify('),
 ('kdef', 'const app = document.getElementById("app");\nconst hud = document.getElementById("hud");',
  'const K = "__KEY__";\nconst LBL = "__LBL__";\nconst app = document.getElementById("app");\nconst hud = document.getElementById("hud");'),
 ('lbl1', 'if (st.k === "card")  return "carta " + (st.ci+1) + " · Aula " + m.aulas[st.ai].n;',
  'if (st.k === "card")  return "carta " + (st.ci+1) + " · " + LBL + " " + m.aulas[st.ai].n;'),
 ('lbl2', 'if (st.k === "chk")   return "checkpoint · Aula " + m.aulas[st.ai].n +',
  'if (st.k === "chk")   return "checkpoint · " + LBL + " " + m.aulas[st.ai].n +'),
 ('lbl3', 'if (st.k === "chk")   return "Checkpoint da Aula " + m.aulas[st.ai].n;',
  'if (st.k === "chk")   return "Checkpoint da " + LBL + " " + m.aulas[st.ai].n;'),
 ('lbl4', 'const tit = isBoss ? `CHEFE DO MÓDULO ${m.n} ⚡` : `Checkpoint · Aula ${m.aulas[st.ai].n}`;',
  'const tit = isBoss ? `CHEFE DO MÓDULO ${m.n} ⚡` : `Checkpoint · ${LBL} ${m.aulas[st.ai].n}`;'),
 ('lbl5', 'let h = topo(`Aula ${a.n} — ${a.ti}`, `Módulo ${m.n} · carta ${st.ci+1}/${a.cards.length}`);',
  'let h = topo(`${LBL} ${a.n} — ${a.ti}`, `Módulo ${m.n} · carta ${st.ci+1}/${a.cards.length}`);'),
 ('lbl6', 'h += `<div class="kick" style="margin:11px 0 3px">Aula ${m.aulas[st.ai].n} — ${m.aulas[st.ai].ti}</div>`;',
  'h += `<div class="kick" style="margin:11px 0 3px">${LBL} ${m.aulas[st.ai].n} — ${m.aulas[st.ai].ti}</div>`;'),
 ('saida', '    out = os.path.join(_ROOT, "output", "AulaViva_Programacao_para_Internet_I.html")',
  '    out = os.path.join(_ROOT, "output", f"AulaViva_{comuns.META['"'"'slug'"'"']}.html")'),
])
print("fim")
