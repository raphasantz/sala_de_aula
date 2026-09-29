# -*- coding: utf-8 -*-
"""Tutorial Ilustrado da Loja — PDF + site-guia (mesmo conteúdo, duas mídias)."""
import base64, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image, Table,
                                TableStyle, KeepTogether, PageBreak)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MOCK = os.path.join(HERE, "mockups_loja")
F = "/home/user/fonts/"
ALT = "/opt/arena-python/lib/python3.11/site-packages/reportlab/fonts/"
def reg(name, path, alt):
    try: pdfmetrics.registerFont(TTFont(name, path))
    except Exception: pdfmetrics.registerFont(TTFont(name, alt))
reg("Inter", F + "Inter-Regular.ttf", ALT + "Vera.ttf")
reg("Inter-Bd", F + "Inter-Bold.ttf", ALT + "VeraBd.ttf")
reg("Inter-Bk", F + "Inter-Black.ttf", ALT + "VeraBd.ttf")
reg("Mono", F + "JetBrainsMono-Regular.ttf", ALT + "Vera.ttf")
reg("Mono-Bd", F + "JetBrainsMono-Bold.ttf", ALT + "VeraBd.ttf")

NAVY=HexColor("#0D2B4E"); AZUL=HexColor("#1B5FAA"); AMB=HexColor("#F59E0B")
AMBBG=HexColor("#FEF4E2"); SKY=HexColor("#E9F1FA"); INK=HexColor("#1F2937")
SOFT=HexColor("#5B6B7C"); LINE=HexColor("#C9D8E8"); VERDE=HexColor("#1E7B34")
VERDBG=HexColor("#E8F4EA"); REDBG=HexColor("#FBEAE8"); RED=HexColor("#C0392B")
CODEBG=HexColor("#0F2237")

S = {}
S["h1"]  = ParagraphStyle("h1", fontName="Inter-Bk", fontSize=24, leading=29, textColor=NAVY)
S["sub"] = ParagraphStyle("sub", fontName="Inter", fontSize=11, leading=16, textColor=SOFT)
S["step"]= ParagraphStyle("step", fontName="Inter-Bk", fontSize=16, leading=21, textColor=white)
S["h3"]  = ParagraphStyle("h3", fontName="Inter-Bd", fontSize=12.5, leading=17, textColor=NAVY,
                          spaceBefore=8, spaceAfter=4)
S["p"]   = ParagraphStyle("p", fontName="Inter", fontSize=10.2, leading=15.5, textColor=INK,
                          alignment=4, spaceAfter=5)
S["li"]  = ParagraphStyle("li", parent=S["p"], alignment=0, leftIndent=14, spaceAfter=3)
S["boxt"]= ParagraphStyle("boxt", fontName="Inter-Bd", fontSize=9.5, leading=13, textColor=HexColor("#9A6206"))
S["boxg"]= ParagraphStyle("boxg", fontName="Inter-Bd", fontSize=9.5, leading=13, textColor=VERDE)
S["boxr"]= ParagraphStyle("boxr", fontName="Inter-Bd", fontSize=9.5, leading=13, textColor=RED)
S["box"] = ParagraphStyle("box", fontName="Inter", fontSize=9.6, leading=14.2, textColor=INK)
S["code"]= ParagraphStyle("code", fontName="Mono", fontSize=8.6, leading=12.6,
                          textColor=HexColor("#DCE9F7"))
S["codet"]= ParagraphStyle("codet", fontName="Mono-Bd", fontSize=8.4, leading=11,
                           textColor=HexColor("#BBD4EE"))
S["cap"] = ParagraphStyle("cap", fontName="Inter", fontSize=8.6, leading=12, textColor=SOFT,
                          alignment=1)

def P(t, s): return Paragraph(t, S[s])
def box(kind, title, body):
    bg, tst = (AMBBG, S["boxt"]) if kind == "tente" else \
              (VERDBG, S["boxg"]) if kind == "ok" else (REDBG, S["boxr"])
    lbl = {"tente": "TENTE VOCÊ", "ok": "CHECK", "erro": "ERRO COMUM"}[kind]
    t = Table([[ [P(lbl, "boxt" if kind=="tente" else "boxg" if kind=="ok" else "boxr"),
                  P(body, "box")] ]], colWidths=[A4[0]-3.2*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),bg),
        ("LINEBEFORE",(0,0),(0,-1),3.2, AMB if kind=="tente" else VERDE if kind=="ok" else RED),
        ("LEFTPADDING",(0,0),(-1,-1),11),("RIGHTPADDING",(0,0),(-1,-1),11),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
        ("ROUNDEDCORNERS",[8,8,8,8])]))
    return t
def code(titulo, linhas):
    rows = [[P(titulo, "codet")]] + [[P(l.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;") or "&nbsp;", "code")] for l in linhas]
    t = Table(rows, colWidths=[A4[0]-3.2*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),CODEBG),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),8),
        ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),1.5),
        ("TOPPADDING",(0,0),(0,0),7),("BOTTOMPADDING",(0,-1),(-1,-1),8),
        ("ROUNDEDCORNERS",[8,8,8,8])]))
    return t
def img(nome, leg):
    from PIL import Image as PILImage
    p = os.path.join(MOCK, nome)
    w, h = PILImage.open(p).size
    tw = A4[0]-3.2*cm
    im = Image(p, width=tw, height=tw*h/w)
    return [im, Spacer(1, 3), P(leg, "cap"), Spacer(1, 8)]
def step_header(n, titulo):
    t = Table([[P(f"PASSO {n}", "codet"), P(titulo, "step")]],
              colWidths=[2.2*cm, A4[0]-5.4*cm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),
        ("LEFTPADDING",(0,0),(0,0),10),("LEFTPADDING",(1,0),(1,0),0),
        ("RIGHTPADDING",(0,0),(-1,-1),12),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ROUNDEDCORNERS",[8,8,8,8])]))
    return [Spacer(1, 10), t, Spacer(1, 8)]

# ============================================================ CONTEÚDO
STEPS = []
STEPS.append(("0", "O que vamos construir (visão geral)", None, [
    ("p", "Neste tutorial você coloca no ar, passo a passo, a <b>Loja Tech da Turma</b>: um site "
           "completo em <b>HTML + CSS + PHP</b> rodando no <b>XAMPP</b>, com banco <b>MySQL</b> e um "
           "<b>gerencial em VB6</b> que compartilha o mesmo banco. Cada passo tem um “print” "
           "ilustrado, um bloco <b>🛠 TENTE VOCÊ</b> e um <b>⚠ ERRO COMUM</b>."),
    ("p", "<b>Mapa das páginas:</b> index.php (vitrine) › produtos.php (catálogo com filtro) › "
           "produto.php?id=N (detalhe + foto) › pagamentos.php (Pix/cartão/boleto simulados) › "
           "processar_pedido.php (grava venda e baixa estoque) › contato.php (contato + localização) › "
           "cadastro.php (clientes)."),
], [("code", ("Estrutura de pastas (o que você copia para o XAMPP)", [
    "C:\\xampp\\htdocs\\loja\\",
    "├── index.php  produtos.php  produto.php",
    "├── pagamentos.php  processar_pedido.php",
    "├── contato.php  cadastro.php  processar_*.php",
    "├── includes\\  (conexao, cabecalho, rodape)",
    "├── css\\estilo.css",
    "└── imagens\\  (logo, banner, produtos, mapa, ícones)"])),
    ("box", ("ok", "Pré-requisitos: VS Code + XAMPP instalados (veja o Checklist_Downloads.pdf) "
                   "e o ZIP Projeto_Loja_Tech_da_Turma extraído."))]),
)
STEPS.append(("1", "Copiar o site para a casa do XAMPP", "mock_vscode.png", [
    ("p", "O XAMPP só executa PHP dentro da pasta <b>htdocs</b>. Copie a pasta <b>site</b> do ZIP para "
           "<b>C:\\xampp\\htdocs\\loja</b> (pode arrastar pelo Explorador de Arquivos). Abra a pasta no "
           "VS Code (Arquivo › Abrir Pasta) para acompanhar os arquivos."),
], [("box", ("tente", "Abra o VS Code em C:\\xampp\\htdocs\\loja e confira na barra lateral as 7 páginas "
                      ".php, a pasta includes/, css/ e imagens/ — igualzinho ao print.")),
    ("box", ("erro", "Deixar as páginas fora da htdocs ou com nome .html: arquivo .html NÃO executa PHP "
                     "(esse era o bug do “site sem fundo e sem imagem”)."))]),
)
STEPS.append(("2", "Ligar os servidores (Apache + MySQL)", "mock_xampp.png", [
    ("p", "Abra o <b>Painel de Controle do XAMPP</b> e clique em <b>Start</b> nas linhas "
           "<b>Apache</b> e <b>MySQL</b>. As duas precisam ficar <b>verdes</b>, com portas 80/443 e 3306."),
], [("box", ("tente", "Com os dois verdes, abra no navegador: http://localhost — o painel do XAMPP "
                      "confirma que o Apache está vivo.")),
    ("box", ("erro", "Apache não inicia (vermelho): porta 80 ocupada (Skype/IIS). Feche o programa ou "
                     "mude a porta em Config › httpd.conf."))]),
)
STEPS.append(("3", "Importar o banco loja_turma", "mock_phpmyadmin.png", [
    ("p", "No navegador: <b>http://localhost/phpmyadmin</b> › aba <b>Importar</b> › escolha o arquivo "
           "<b>banco/loja_turma.sql</b> do ZIP › <b>Executar</b>. Pronto: banco, 4 tabelas, dados de "
           "exemplo e a view de estoque baixo criados de uma vez."),
], [("code", ("Alternativa pelo terminal (cmd)", [
    "cd C:\\xampp\\mysql\\bin",
    "mysql -u root < C:\\caminho\\banco\\loja_turma.sql"])),
    ("box", ("tente", "Clique na tabela produtos › aba Explorar: devem aparecer 8 produtos com foto, "
                      "preço, estoque e descrição.")),
    ("box", ("erro", "Esquecer de importar e o site abrir com “Falha na conexão”: o PHP não acha o "
                     "banco loja_turma."))]),
)
STEPS.append(("4", "Abrir a vitrine e entender o fluxo", "mock_browser_home.png", [
    ("p", "Acesse <b>http://localhost/loja/index.php</b>. A vitrine NÃO está escrita no HTML: o PHP "
           "consulta <b>SELECT … FROM produtos WHERE destaque=1</b> e monta cada card na hora. Fluxo: "
           "navegador pede › Apache passa ao PHP › PHP consulta o MySQL › HTML volta pronto."),
], [("box", ("tente", "No phpMyAdmin, mude o preço do Mouse para 99,90 e atualize a página: o card muda "
                      "sozinho. Isso é conteúdo dinâmico!")),
    ("box", ("ok", "Se apareceu o banner, o logo e os 4 cards com preço verde: seu ambiente está 100%."))]),
)
STEPS.append(("5", "Detalhe do produto e pagamento", "mock_browser_produto.png", [
    ("p", "Clique num produto: a URL fica <b>produto.php?id=1</b> — o id viaja por <b>GET</b> e o PHP "
           "busca a ficha completa (foto, descrição, estoque). Em “Ir para o pagamento”, escolha Pix, "
           "Cartão ou Boleto e confirme: o PHP grava a <b>venda</b> e <b>baixa o estoque</b>."),
], [("code", ("O que acontece no banco a cada pedido", [
    "INSERT INTO vendas (produto_id, qtd, total) VALUES (1, 2, 179.80);",
    "UPDATE produtos SET estoque = estoque - 2 WHERE id = 1;"])),
    ("box", ("tente", "Confira no phpMyAdmin: linha nova em vendas e estoque diminuído em produtos. "
                      "Depois abra o gerencial VB6 e veja o mesmo número!")),
    ("box", ("erro", "Pedir quantidade maior que o estoque: o site avisa “Estoque insuficiente” — "
                     "validação no servidor funcionando."))]),
)
STEPS.append(("6", "Testar no celular (mesmo Wi-Fi)", None, [
    ("p", "O celular não entende “localhost” (que é o PC). Descubra o IP do PC: <b>Win+R › cmd › "
           "ipconfig</b> (IPv4, ex.: 192.168.0.15). No celular, no <b>mesmo Wi-Fi</b>, abra "
           "<b>http://192.168.0.15/loja/index.php</b>. O layout se ajusta sozinho à tela."),
], [("box", ("tente", "Compre um produto pelo celular e veja o estoque cair no PC: o banco é um só "
                      "para todos os aparelhos.")),
    ("box", ("erro", "Celular em 4G ou em outro Wi-Fi: não alcança o PC. Tem que ser a mesma rede."))]),
)
STEPS.append(("7", "Backup e o desastre didático", "mock_terminal.png", [
    ("p", "Backup é cópia de segurança. No cmd: <b>mysqldump -u root loja_turma &gt; arquivo.sql</b>. "
           "Restaurar: <b>mysql -u root loja_turma &lt; arquivo.sql</b>. Professor(a): faça o desastre "
           "didático — DELETE FROM produtos; sem WHERE — e deixe a turma recuperar. Ninguém mais esquece."),
], [("code", ("Backup e recuperação (cmd em C:\\xampp\\mysql\\bin)", [
    "mysqldump -u root loja_turma > C:\\lp2\\backups\\loja_aula.sql",
    "mysql -u root -e \"CREATE DATABASE loja_teste;\"",
    "mysql -u root loja_teste < C:\\lp2\\backups\\loja_aula.sql",
    "mysql -u root loja_teste -e \"SELECT COUNT(*) FROM produtos;\""])),
    ("box", ("ok", "Validação pós-restauro: 4 tabelas e 8 produtos conferidos ANTES de confiar."))]),
)
STEPS.append(("8", "O gerencial VB6 no mesmo banco", "mock_vb6.png", [
    ("p", "No VB6: crie um projeto <b>Standard EXE</b>, marque em Projeto › Referências a "
           "<b>Microsoft ActiveX Data Objects 2.8</b>, importe <b>mdlConexao.bas</b> e "
           "<b>mdlRelatorios.bas</b> e monte o formulário seguindo o arquivo "
           "<b>frmGerencial_codigo.txt</b>. O botão Atualizar lista mostra os mesmos produtos do site."),
], [("box", ("tente", "Cadastre um produto pelo VB6 e atualize o site: ele aparece na vitrine. "
                      "Depois imprima o Relatório (ou “Microsoft Print to PDF”).")),
    ("box", ("erro", "“Data source name not found”: falta o driver MySQL ODBC instalado no Windows."))]),
)
STEPS.append(("9", "Missão do aluno: a SUA loja", None, [
    ("p", "Com o modelo dominado, cada aluno/dupla cria a <b>própria loja</b> (petshop, lanchonete, "
           "boutique, oficina…) repetindo a estrutura: 4+ páginas, 1 tabela nova com seed próprio, "
           "formulário com validação, página de detalhe com “pagamento”, e backup executado."),
], [("box", ("ok", "Rubrica sugerida (10 pts): site sem erros 2 · formulários validados 2 · consulta SQL "
                   "exibindo dados 2 · tabela própria com seed 1,5 · pedido baixando estoque 1,5 · backup "
                   "comprovado 1.")),
    ("box", ("tente", "Troque o CSS de cores (2 linhas no estilo.css) para a identidade da sua loja: "
                      "mesma estrutura, cara nova."))]),
)

STEPS = [(t[0], t[1], t[2], t[3] + (list(t[4]) if len(t) > 4 else [])) for t in STEPS]

# ============================================================ PDF
doc = SimpleDocTemplate(os.path.join(ROOT, "output", "Tutorial_Loja_Ilustrado.pdf"),
    pagesize=A4, leftMargin=1.6*cm, rightMargin=1.6*cm, topMargin=1.5*cm, bottomMargin=1.5*cm,
    title="Tutorial Ilustrado — Loja Tech da Turma", author="Turma 2/2026")
st = []
capa = Table([[ [P("TUTORIAL ILUSTRADO", "codet"),
                 P("Loja Tech da Turma — site + banco + gerencial, passo a passo", "h1"),
                 Spacer(1, 6),
                 P("Programação para Internet I + Linguagem de Programação II · Turma 2/2026 · "
                   "VS Code + XAMPP + MySQL + VB6 · com prints ilustrados, “tente você” e erros comuns", "sub")] ]],
             colWidths=[A4[0]-3.2*cm])
capa.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),NAVY),
    ("LEFTPADDING",(0,0),(-1,-1),16),("RIGHTPADDING",(0,0),(-1,-1),16),
    ("TOPPADDING",(0,0),(-1,-1),18),("BOTTOMPADDING",(0,0),(-1,-1),18),
    ("ROUNDEDCORNERS",[10,10,10,10])]))
st.append(capa); st.append(Spacer(1, 10))
for n, titulo, imgname, blocos in STEPS:
    bloco = step_header(n, titulo)
    for kind, payload in blocos:
        if kind == "p": bloco.append(P(payload, "p"))
        elif kind == "code": bloco.append(code(*payload)); bloco.append(Spacer(1, 6))
        elif kind == "box": bloco.append(box(payload[0], "", payload[1])); bloco.append(Spacer(1, 4))
    if imgname:
        bloco.extend(img(imgname, f"Figura do passo {n}: " + titulo))
    st.append(KeepTogether(bloco[:3]))
    st.extend(bloco[3:])
doc.build(st)
print("PDF ok")

# ============================================================ SITE-GUIA
CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,Arial,sans-serif;background:#eef3f9;color:#1f2937;
 background-image:radial-gradient(circle at 1px 1px,rgba(27,95,170,.10) 1px,transparent 0);
 background-size:26px 26px}
header{background:linear-gradient(90deg,#0d2b4e,#14406f);color:#fff;padding:26px 18px;text-align:center}
header h1{font-size:26px} header p{color:#c9dcf2;margin-top:6px;font-size:14px}
nav{position:sticky;top:0;background:#0d2b4e;display:flex;flex-wrap:wrap;gap:4px;justify-content:center;padding:8px}
nav a{color:#fff;text-decoration:none;font-size:12.5px;font-weight:700;padding:6px 10px;border-radius:14px}
nav a:hover{background:#f59e0b;color:#0d2b4e}
main{max-width:900px;margin:0 auto;padding:20px 14px 60px}
section{background:#fff;border-radius:16px;padding:20px;margin:18px 0;box-shadow:0 3px 14px rgba(13,43,78,.10)}
section h2{color:#0d2b4e;font-size:20px;border-left:6px solid #f59e0b;padding-left:10px;margin-bottom:10px}
section p{line-height:1.65;margin:8px 0;font-size:15px;text-align:justify}
img{width:100%;border-radius:12px;border:1px solid #dfe8f2;margin:10px 0}
figcaption{font-size:12.5px;color:#5b6b7c;text-align:center;margin:-4px 0 10px}
pre{background:#0f2237;color:#dce9f7;border-radius:12px;padding:14px;overflow-x:auto;
 font-family:Consolas,'JetBrains Mono',monospace;font-size:13px;line-height:1.55;margin:10px 0}
.box{border-radius:12px;padding:12px 14px;margin:10px 0;font-size:14px;line-height:1.55}
.box b.t{display:block;font-size:12.5px;letter-spacing:.4px;margin-bottom:4px}
.tente{background:#fef4e2;border-left:6px solid #f59e0b}.tente b.t{color:#9a6206}
.okk{background:#e8f4ea;border-left:6px solid #1e7b34}.okk b.t{color:#1e7b34}
.erro{background:#fbeae8;border-left:6px solid #c0392b}.erro b.t{color:#c0392b}
@media(max-width:700px){header h1{font-size:20px}section{padding:14px}}
"""
html = ["<!DOCTYPE html><html lang='pt-br'><head><meta charset='UTF-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1.0'>"
        "<title>Tutorial Ilustrado — Loja Tech da Turma</title><style>" + CSS + "</style></head><body>",
        "<header><h1>🛍️ Tutorial Ilustrado — Loja Tech da Turma</h1>"
        "<p>PI-I + LP2 · Turma 2/2026 · VS Code + XAMPP + MySQL + VB6 · offline</p></header>",
        "<nav>" + "".join(f"<a href='#p{n}'>Passo {n}</a>" for n, _, _, _ in STEPS) + "</nav>",
        "<main>"]
for n, titulo, imgname, blocos in STEPS:
    html.append(f"<section id='p{n}'><h2>Passo {n} — {titulo}</h2>")
    for kind, payload in blocos:
        if kind == "p": html.append(f"<p>{payload}</p>")
        elif kind == "code":
            html.append("<pre>" + "\n".join(payload[1]).replace("&","&amp;").replace("<","&lt;") + "</pre>")
        elif kind == "box":
            cls = {"tente":"tente","ok":"okk","erro":"erro"}[payload[0]]
            lbl = {"tente":"🛠 TENTE VOCÊ","ok":"✔ CHECK","erro":"⚠ ERRO COMUM"}[payload[0]]
            html.append(f"<div class='box {cls}'><b class='t'>{lbl}</b>{payload[1]}</div>")
    if imgname:
        b64 = base64.b64encode(open(os.path.join(MOCK, imgname), "rb").read()).decode()
        html.append(f"<figure><img src='data:image/png;base64,{b64}' alt='print do passo {n}'>"
                    f"<figcaption>Figura do passo {n}: {titulo}</figcaption></figure>")
    html.append("</section>")
html.append("</main></body></html>")
open(os.path.join(ROOT, "output", "Tutorial_Loja_Guia.html"), "w", encoding="utf-8").write("".join(html))
print("site-guia ok")
