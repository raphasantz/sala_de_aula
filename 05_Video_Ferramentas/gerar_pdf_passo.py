# -*- coding: utf-8 -*-
"""Gera o Passo a Passo (PDF) das duas videoaulas — companheiro de papel do vídeo.
Uso: python3 video_tools/gerar_pdf_passo.py
Saída: videoaulas/Passo_a_Passo_*.pdf  (+ cópia em output/)"""
import os, shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
F = os.path.join(ROOT, "fonts")
for n, arq in (("R", "Inter-Regular.ttf"), ("B", "Inter-Bold.ttf"),
               ("S", "Inter-SemiBold.ttf"), ("M", "JetBrainsMono-Regular.ttf")):
    pdfmetrics.registerFont(TTFont("Inter" + n, os.path.join(F, arq)))

NAVY = HexColor("#12263a"); AMB = HexColor("#f2a33c"); MUT = HexColor("#6b7a8d")
GRN = HexColor("#1e7b34"); BG = HexColor("#f6f3ec")

tit = ParagraphStyle("t", fontName="InterB", fontSize=21, textColor=NAVY, leading=26)
sub = ParagraphStyle("s", fontName="InterR", fontSize=11, textColor=MUT, leading=15)
h2 = ParagraphStyle("h2", fontName="InterB", fontSize=13.5, textColor=NAVY,
                    leading=17, spaceBefore=10, spaceAfter=4)
bd = ParagraphStyle("bd", fontName="InterR", fontSize=10.5, textColor=HexColor("#1f2937"),
                    leading=15, leftIndent=10, bulletIndent=0, spaceAfter=2)
mono = ParagraphStyle("mo", fontName="InterM", fontSize=9.5, textColor=HexColor("#16202e"),
                      leading=14, leftIndent=16, spaceAfter=2,
                      backColor=HexColor("#eef2f6"), borderPadding=3)
nota = ParagraphStyle("nt", fontName="InterS", fontSize=10, textColor=GRN, leading=14,
                      spaceBefore=3, spaceAfter=6, leftIndent=10)

def cena(num, nome, passos, codigos=(), dica=None):
    out = [Paragraph(f"CENA {num} · {nome}", h2)]
    for p in passos:
        out.append(Paragraph(p, bd, bulletText="•"))
    for c in codigos:
        out.append(Paragraph(c.replace("&", "&amp;").replace("<", "&lt;"), mono))
    if dica:
        out.append(Paragraph("Dica: " + dica, nota))
    out.append(Spacer(1, 4))
    return out

def capa(disc, sub_t, dur):
    return [
        Paragraph(f"Passo a passo da videoaula<br/>{disc}", tit),
        Spacer(1, 4),
        Paragraph(f"{sub_t} · companheiro de papel do vídeo · duração ~{dur} · "
                  "Curso Técnico em Informática · Turma 2/2026 · Prof.ª Raquel", sub),
        HRFlowable(width="100%", thickness=2, color=AMB, spaceBefore=8, spaceAfter=10),
        Paragraph("Como usar: abra o vídeo na pasta <b>videoaulas/</b> (ou pelo botão "
                  "<b>Videoaula</b> na tela inicial do AulaViva) e siga esta folha do lado. "
                  "Cada cena do vídeo tem o seu bloco aqui, com os cliques na ordem. "
                  "Se travar em algum passo, volte no trecho do vídeo — e respire: errar faz parte.", sub),
        Spacer(1, 8),
    ]

PI1 = []
PI1 += capa("Programação para Internet I", "Loja Tech da Turma — PHP + MySQL no XAMPP", "13 min")
PI1 += cena(1, "Abertura e mapa do vídeo", [
    "O que vamos fazer: instalar VS Code e XAMPP, criar o banco <b>loja_turma</b> e colocar a loja no ar.",
    "No fim, uma compra de verdade: produto → carrinho → pagamento → pedido gravado no banco.",
    "Sem pressa: cada parada do mapa vira uma cena do vídeo."])
PI1 += cena(2, "Instalar o VS Code", [
    "Baixe SOMENTE do site oficial: code.visualstudio.com → botão azul <b>Download for Windows</b>.",
    "No instalador, marque: <b>Adicionar ao PATH</b> e <b>Registrar como editor suportado</b>.",
    "Avançar, avançar, concluir. Abra o VS Code: é o caderno onde a gente escreve o site."],
    dica="atalho útil: botão direito numa pasta → “Abrir com Code”.")
PI1 += cena(3, "Instalar o XAMPP", [
    "Baixe do site oficial: apachefriends.org → versão para Windows.",
    "Instale aceitando tudo padrão (Apache + MySQL + PHP vêm juntos).",
    "XAMPP = a caixa que transforma o seu PC em servidor de testes (localhost)."])
PI1 += cena(4, "Ligar Apache e MySQL e testar", [
    "Abra o Painel de Controle do XAMPP → <b>Start</b> em Apache e em MySQL.",
    "No navegador: http://localhost → apareceu a página do XAMPP? Servidor no ar.",
    "http://localhost/phpmyadmin → é a portaria do banco de dados."],
    dica="se a porta 80 estiver ocupada, feche Skype/Teams/IIS e tente de novo.")
PI1 += cena(5, "Criar o banco loja_turma", [
    "phpMyAdmin → Nova base de dados → nome <b>loja_turma</b> → criar.",
    "Aba SQL → cole o script <b>loja_turma.sql</b> (pasta banco/ do kit) → Executar.",
    "Conferir: tabelas produtos, clientes, pedidos aparecem na lista à esquerda."],
    codigos=("loja_turma: produtos | clientes | pedidos",))
PI1 += cena(6, "Copiar o site para a htdocs", [
    "Copie a pasta <b>site/</b> do projeto para C:\\xampp\\htdocs\\loja (pasta inteira).",
    "Confira o includes/conexao.php: servidor localhost, banco loja_turma, usuário loja_app.",
    "Navegador: http://localhost/loja → a vitrine abre com os produtos do banco."])
PI1 += cena(7, "A loja no navegador: compra de verdade", [
    "Percorra: vitrine → ficha do produto → carrinho → pagamento (pix/cartão/boleto).",
    "Finalize o pedido: aparece o protocolo → o pedido EXISTE no banco (confira no phpMyAdmin).",
    "Teste também cadastro e contato: os formulários gravam e avisam por e-mail de mentira."])
PI1 += cena(8, "Por dentro do código", [
    "conexao.php: abre a ligação com o MySQL (PDO) — uma vez só, reaproveitada em tudo.",
    "produtos.php: SELECT ... ORDER BY + <b>foreach</b> desenhando os cards da vitrine.",
    "produto.php: lê o id pela URL (?id=) com consulta preparada — sem susto de injeção."],
    codigos=("$stmt = $pdo->prepare(\"SELECT * FROM produtos WHERE id = ?\");",))
PI1 += cena(9, "Transação e segurança: os dois segredos", [
    "processar_pedido.php usa <b>transação</b>: BEGIN → grava pedido → grava itens → COMMIT.",
    "Se algo falhar no meio: ROLLBACK — o banco nunca fica pela metade.",
    "O SELECT ... FOR UPDATE segura o estoque enquanto a compra acontece (sem venda furada).",
    "htmlspecialchars() nas saídas e consultas preparadas nas entradas: dupla de proteção."],
    codigos=("BEGIN;  INSERT pedidos;  INSERT itens;  COMMIT;   -- ou ROLLBACK",))
PI1 += cena(10, "Recapitulando e missão da turma", [
    "Checklist: VS Code ✓ XAMPP ✓ banco loja_turma ✓ site na htdocs ✓ compra gravada ✓.",
    "Missão: trocar o nome da loja, um produto e uma cor do CSS — e mostrar pra turma.",
    "Dúvida? Reassista a cena correspondente: o vídeo fica na pasta videoaulas/ e no app."])

LP2 = []
LP2 += capa("Linguagem de Programação II", "VB6 na prática — do zero ao primeiro programa", "11 min")
LP2 += cena(1, "Abertura e mapa do vídeo", [
    "Vamos: deixar o VB6 pronto, criar as pastas do semestre e fazer o primeiro programa.",
    "O programa vai: cumprimentar com nome e data, dizer par/ímpar e imprimir tabuada.",
    "É exatamente o exercício do Módulo 1 — assistindo, você já entende a resolução."])
LP2 += cena(2, "Instalar / abrir o VB6", [
    "Instalador: botão direito em setup.exe → Propriedades → aba Compatibilidade.",
    "Marque: modo de compatibilidade (Windows 7/XP) E executar como administrador.",
    "Dois cliques no setup → assistente padrão → <b>reinicie o PC</b>.",
    "Se o PC já tem VB6: Menu Iniciar → digite “Visual Basic 6” → abrir."])
LP2 += cena(3, "Pastas do semestre", [
    "Documentos → nova pasta <b>LP2</b>; dentro dela: S01, S02, S03, S04 e PROJETO.",
    "A aula de hoje mora em S01; o trabalho final morará em PROJETO.",
    "Regra da turma: todo projeto salvo tem endereço fixo. Sempre."],
    codigos=("Documentos\\LP2\\S01 .. S04 + PROJETO",))
LP2 += cena(4, "Conhecendo a tela do VB6", [
    "Formulário = palco (o que o usuário vê). Caixa de ferramentas = peças.",
    "Propriedades = ajuste fino ((Name) é o nome do código; Caption é o texto visível).",
    "Janela do projeto = arquivos; janela de código = cozinha (dois cliques na peça)."])
LP2 += cena(5, "Projeto ola.vbp e o Form_Load", [
    "Novo Projeto → <b>Standard EXE</b> → OK.",
    "SALVE ANTES DE CODAR: Form1.frm e <b>ola.vbp</b> dentro de LP2\\S01.",
    "Dois cliques no form → digite o Form_Load → F5 para rodar."],
    codigos=("Private Sub Form_Load()",
             "    Print \"Olá, eu sou a Prof.ª Raquel!\"",
             "    Print \"Hoje é \" & Date",
             "End Sub"))
LP2 += cena(6, "Errar faz parte", [
    "Quebre de propósito (tire uma aspa) → F5 → o VB6 destaca a linha: leia sem medo.",
    "Private Sub abre, End Sub fecha. Texto entre aspas; número sem aspas.",
    "Ctrl+S toda hora, na sua pasta. Corrija uma coisa de cada vez."])
LP2 += cena(7, "Exercício 1 no papel: a média", [
    "soma ← 0; laço para i de 1 até 3 (leia nota, some) → REPETIÇÃO.",
    "media ← soma / 3 → SEQUÊNCIA; se/senao-se/senao → SELEÇÃO.",
    "Teste na lousa: 6, 8, 7 → soma 21 → média 7 → APROVADO."],
    codigos=("para i de 1 ate 3 faca  leia(nota); soma <- soma + nota  fim-para",))
LP2 += cena(8, "Botão Par ou Ímpar (If + Mod)", [
    "Toolbox → CommandButton → desenhe; (Name) btnParImpar, Caption “Par ou Ímpar?”.",
    "Dois cliques → código abaixo → F5 → teste 7 (ímpar) e 10 (par).",
    "Val() converte o texto do InputBox em número; Mod é o resto da divisão."],
    codigos=("Private Sub btnParImpar_Click()",
             "    Dim n As Integer",
             "    n = Val(InputBox(\"Digite um número inteiro:\"))",
             "    If n Mod 2 = 0 Then",
             "        Print n & \" é PAR\"",
             "    Else",
             "        Print n & \" é ÍMPAR\"",
             "    End If",
             "End Sub"))
LP2 += cena(9, "Botão Tabuada (For...Next)", [
    "Segundo botão: (Name) btnTabuada, Caption “Tabuada 1 a 10”.",
    "For i = 1 To 10 repete o Print dez vezes; o & cola os pedaços da linha.",
    "F5 → digite 7 → aparecem as dez linhas, até 7 x 10 = 70."],
    codigos=("Private Sub btnTabuada_Click()",
             "    Dim n As Integer, i As Integer",
             "    n = Val(InputBox(\"Tabuada de qual número?\"))",
             "    For i = 1 To 10",
             "        Print n & \" x \" & i & \" = \" & n * i",
             "    Next i",
             "End Sub"))
LP2 += cena(10, "Checklist final e próximos passos", [
    "Pastas ✓ · ola.vbp em S01 ✓ · Form_Load ✓ · btnParImpar ✓ · btnTabuada ✓ · F5 + Ctrl+S ✓.",
    "Exercícios 1, 2 e 3 do Módulo 1: feitos e entendidos.",
    "Continue no AulaViva (Módulo 2) e reassista este vídeo quantas vezes quiser."])

def build(nome, fluxo):
    for destino in (os.path.join(ROOT, "videoaulas", nome),
                    os.path.join(ROOT, "output", nome)):
        doc = SimpleDocTemplate(destino, pagesize=A4,
                                leftMargin=18 * mm, rightMargin=18 * mm,
                                topMargin=16 * mm, bottomMargin=16 * mm,
                                title=nome.replace(".pdf", ""))
        doc.build(fluxo)
    print("OK:", nome)

build("Passo_a_Passo_Videoaula_PI-I_Loja_Tech.pdf", PI1)
build("Passo_a_Passo_Videoaula_LP2_VB6.pdf", LP2)
