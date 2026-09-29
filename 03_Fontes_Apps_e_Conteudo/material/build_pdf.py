# -*- coding: utf-8 -*-
"""
Gerador da APOSTILA em PDF — Programação para Internet I (Turma 2/2026).
Gera duas versões: ALUNO (sem gabaritos) e PROFESSOR (com gabaritos e orientações).
Uso: python3 build_pdf.py
"""
import os
import re
import sys
from xml.sax.saxutils import escape as xml_escape

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, NextPageTemplate, KeepTogether,
                                HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents

import importlib as _il
_PKG = _il.import_module(os.environ.get("CONTEUDO_PKG", "conteudo"))
MODULOS = _PKG.MODULOS
MODULOS_POR_NUM = _PKG.MODULOS_POR_NUM
GLOSSARIO = _PKG.GLOSSARIO
comuns = _PKG.comuns
avaliacoes = _PKG.avaliacoes

# ---------------------------------------------------------------------------
# FONTES
# ---------------------------------------------------------------------------
F = os.path.join(_ROOT, "fonts") + os.sep
pdfmetrics.registerFont(TTFont("Inter", F + "Inter-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Md", F + "Inter-Medium.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Sb", F + "Inter-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bd", F + "Inter-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bk", F + "Inter-Black.ttf"))
pdfmetrics.registerFont(TTFont("Inter-It", F + "Inter-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Inter-BdIt", F + "Inter-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("Inter", normal="Inter", bold="Inter-Bd",
                              italic="Inter-It", boldItalic="Inter-BdIt")
pdfmetrics.registerFont(TTFont("Mono", F + "JetBrainsMono-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Mono-Bd", F + "JetBrainsMono-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono-It", F + "JetBrainsMono-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Mono-Md", F + "JetBrainsMono-Medium.ttf"))
pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bd",
                              italic="Mono-It", boldItalic="Mono-Bd")

# ---------------------------------------------------------------------------
# PALETA — azul profissional
# ---------------------------------------------------------------------------
NAVY      = HexColor("#0D2B4E")   # azul-marinho (capa, divisórias, cabeçalho de tabela)
NAVY2     = HexColor("#143A66")   # navy claro (caixas da capa)
PRIMARY   = HexColor("#1B5FAA")   # azul principal
PRIMARY_D = HexColor("#124A87")
SKY       = HexColor("#E9F1FA")   # fundo azul claro
SKY2      = HexColor("#D6E4F5")
AMBER     = HexColor("#F59E0B")   # laranja/âmbar de destaque
AMBER_BG  = HexColor("#FEF4E2")
AMBER_D   = HexColor("#9A6206")
RED       = HexColor("#C0392B")
RED_BG    = HexColor("#FBEAE8")
GREEN     = HexColor("#1E7B34")
GREEN_BG  = HexColor("#E8F4EA")
INK       = HexColor("#1F2937")   # texto corrente
INK_SOFT  = HexColor("#51606F")
LINE      = HexColor("#C9D8E8")
ROW_ALT   = HexColor("#F4F8FC")
CODE_BG   = HexColor("#0F2237")   # painel de código
CODE_BAR  = HexColor("#1A3A5C")
CODE_FG   = HexColor("#DCE9F7")
# sintaxe (tema escuro tipo One-Dark)
C_COM  = "#7F96AD"
C_STR  = "#9ECE6A"
C_KEY  = "#D38AE0"
C_VAR  = "#F2777A"
C_FUN  = "#6CB6FF"
C_TAG  = "#6CB6FF"
C_NUM  = "#E5C07B"

PAGE_W, PAGE_H = A4
ML = MR = 1.7 * cm
MT = 2.15 * cm
MB = 1.9 * cm
TW = PAGE_W - ML - MR            # largura útil de texto

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}

# ---------------------------------------------------------------------------
# SANITIZAÇÃO DE TEXTO PARA PARÁGRAFO (preserva <b>, <i>, <u>, <br>)
# ---------------------------------------------------------------------------
EMOJI_MAP = {
    "\u2192": "\u203a", "\u2190": "\u2039", "\u2194": "-",   # → ← ↔
    "\u2713": "\u2022", "\u2714": "\u2022",          # ✓ ✔ -> •
    "\u2610": "[  ]",                                  # ☐
    "\u26a0": "(!)",                                   # ⚠
    "\u2705": "[OK]", "\U0001F6AB": "[X]",            # ✅ 🚫
}
_RE_EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF]")

def safe_para(s):
    if not isinstance(s, str):
        s = str(s)
    for k, v in EMOJI_MAP.items():
        s = s.replace(k, v)
    s = _RE_EMOJI.sub("", s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|nbsp;|#\d+;|#x[0-9a-fA-F]+;)", "&amp;", s)
    s = re.sub(r"<(?!/?(?:b|i|u|br|sub|super|strike)(?:\s[^>]*)?\s*/?>)", "&lt;", s)
    return s

def P(text, style):
    return Paragraph(safe_para(text), style)

def plain(s):
    """Remove marcação para usos em TOC/notas."""
    s = re.sub(r"<[^>]+>", "", str(s))
    return (s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
             .replace("&quot;", '"'))

# ---------------------------------------------------------------------------
# ESTILOS
# ---------------------------------------------------------------------------
S = {}
S["body"] = ParagraphStyle("body", fontName="Inter", fontSize=10, leading=14.8,
                           textColor=INK, alignment=TA_JUSTIFY, spaceAfter=5)
S["body_c"] = ParagraphStyle("body_c", parent=S["body"], alignment=TA_LEFT)
S["li"] = ParagraphStyle("li", parent=S["body"], alignment=TA_LEFT, leftIndent=14,
                         bulletIndent=3, spaceAfter=3)
S["li_num"] = ParagraphStyle("li_num", parent=S["li"])
S["h_sub"] = ParagraphStyle("h_sub", fontName="Inter-Sb", fontSize=11.3, leading=15,
                            textColor=PRIMARY_D, spaceBefore=10, spaceAfter=4)
S["box_title"] = ParagraphStyle("box_title", fontName="Inter-Bd", fontSize=8.6, leading=11,
                                textColor=PRIMARY, spaceAfter=2.5)
S["box_text"] = ParagraphStyle("box_text", fontName="Inter", fontSize=9.6, leading=14,
                               textColor=INK, alignment=TA_JUSTIFY)
S["th"] = ParagraphStyle("th", fontName="Inter-Sb", fontSize=8.8, leading=12,
                         textColor=white)
S["td"] = ParagraphStyle("td", fontName="Inter", fontSize=9, leading=12.8, textColor=INK)
S["td_j"] = ParagraphStyle("td_j", parent=S["td"], alignment=TA_JUSTIFY)
S["code_title"] = ParagraphStyle("code_title", fontName="Mono-Bd", fontSize=8.4, leading=11,
                                 textColor=HexColor("#BBD4EE"))
S["code_lang"] = ParagraphStyle("code_lang", fontName="Mono-Md", fontSize=7.4, leading=10,
                                textColor=HexColor("#8FB3D9"), alignment=TA_RIGHT)
S["code"] = ParagraphStyle("code", fontName="Mono", fontSize=8.3, leading=12.4,
                           textColor=CODE_FG)
S["part_num"] = ParagraphStyle("part_num", fontName="Inter-Bk", fontSize=44, leading=48,
                               textColor=white)
S["part_title"] = ParagraphStyle("part_title", fontName="Inter-Bd", fontSize=21, leading=26,
                                 textColor=white)
S["part_sub"] = ParagraphStyle("part_sub", fontName="Inter-Md", fontSize=11, leading=15,
                               textColor=HexColor("#BBD4EE"))
S["mod_kick"] = ParagraphStyle("mod_kick", fontName="Inter-Bk", fontSize=9.5, leading=12,
                               textColor=AMBER)
S["mod_title"] = ParagraphStyle("mod_title", fontName="Inter-Bk", fontSize=19, leading=23,
                                textColor=white)
S["mod_meta"] = ParagraphStyle("mod_meta", fontName="Inter-Md", fontSize=8.8, leading=12,
                               textColor=HexColor("#C9DCF2"))
S["aula"] = ParagraphStyle("aula", fontName="Inter-Bd", fontSize=12.8, leading=16.5,
                           textColor=NAVY)
S["aula_kick"] = ParagraphStyle("aula_kick", fontName="Inter-Bk", fontSize=8, leading=10,
                                textColor=AMBER_D)
S["band"] = ParagraphStyle("band", fontName="Inter-Bk", fontSize=12.5, leading=16,
                           textColor=white)
S["band_sub"] = ParagraphStyle("band_sub", fontName="Inter-Md", fontSize=8.6, leading=11,
                               textColor=HexColor("#DCE9F7"))
S["obj_title"] = ParagraphStyle("obj_title", fontName="Inter-Bk", fontSize=9, leading=12,
                                textColor=PRIMARY_D, spaceAfter=3)
S["obj_li"] = ParagraphStyle("obj_li", fontName="Inter", fontSize=9.4, leading=13.6,
                             textColor=INK, leftIndent=13, spaceAfter=2)
S["q"] = ParagraphStyle("q", fontName="Inter-Sb", fontSize=10, leading=14.4,
                        textColor=INK, spaceAfter=3, alignment=TA_LEFT)
S["alt"] = ParagraphStyle("alt", fontName="Inter", fontSize=9.8, leading=13.8,
                          textColor=INK, leftIndent=16, spaceAfter=1.5)
S["ans"] = ParagraphStyle("ans", fontName="Inter-It", fontSize=8.6, leading=11,
                          textColor=INK_SOFT, leftIndent=16, spaceBefore=1)
S["gab_title"] = ParagraphStyle("gab_title", fontName="Inter-Bk", fontSize=8.4, leading=11,
                                textColor=GREEN, spaceAfter=2)
S["gab_text"] = ParagraphStyle("gab_text", fontName="Inter", fontSize=9.2, leading=13.4,
                               textColor=INK)
S["ex_title"] = ParagraphStyle("ex_title", fontName="Inter-Bd", fontSize=10.6, leading=14,
                               textColor=NAVY)
S["ex_kick"] = ParagraphStyle("ex_kick", fontName="Inter-Bk", fontSize=8, leading=10,
                              textColor=AMBER_D)
S["h1"] = ParagraphStyle("h1", fontName="Inter-Bk", fontSize=20, leading=25, textColor=NAVY,
                         spaceAfter=8)
S["h2"] = ParagraphStyle("h2", fontName="Inter-Bd", fontSize=13.5, leading=17,
                         textColor=PRIMARY_D, spaceBefore=12, spaceAfter=5)
S["cap"] = ParagraphStyle("cap", fontName="Inter-Bk", fontSize=34, leading=40, textColor=white)
S["cap2"] = ParagraphStyle("cap2", fontName="Inter-Md", fontSize=12.5, leading=17,
                          textColor=HexColor("#C9DCF2"))
S["kick"] = ParagraphStyle("kick", fontName="Inter-Bk", fontSize=9.5, leading=13,
                           textColor=AMBER)
S["stamp"] = ParagraphStyle("stamp", fontName="Inter-Bk", fontSize=12, leading=15,
                            textColor=NAVY)
S["exam_field"] = ParagraphStyle("exam_field", fontName="Inter-Md", fontSize=9.5, leading=15,
                                 textColor=INK)
S["line_ans"] = ParagraphStyle("line_ans", fontName="Mono", fontSize=9, leading=19,
                               textColor=HexColor("#9FB4C8"))
S["toc0"] = ParagraphStyle("toc0", fontName="Inter-Bk", fontSize=10.6, leading=18,
                           textColor=NAVY, spaceBefore=5)
S["toc1"] = ParagraphStyle("toc1", fontName="Inter-Md", fontSize=9.6, leading=15.5,
                           textColor=INK, leftIndent=16)

# ---------------------------------------------------------------------------
# REALCE DE SINTAXE (código)
# ---------------------------------------------------------------------------
PHP_WORDS = ("echo|print|if|else|elseif|endif|for|endforeach|foreach|while|do|switch|case|"
             "break|default|function|return|true|false|null|exit|die|include|require|"
             "include_once|require_once|define|as|new|and|or|xor|isset|empty|array|int|"
             "string|bool|float")
TOK_PHP = re.compile(r"(\$[A-Za-z_]\w*)|\b(" + PHP_WORDS + r")\b|\b([A-Za-z_]\w*)(?=\s*\()"
                     r"|\b(\d+(?:\.\d+)?)\b")
TOK_TAG = re.compile(r"(&lt;/?[A-Za-z][^&<]*?&gt;)")
TOK_PTAG = re.compile(r"(&lt;\?php\b|&lt;\?=|&lt;\?|\?&gt;)")
TOK_STR = re.compile(r'("[^"]*"|\'[^\']*\')')
TOK_COM_PHP = re.compile(r"(//.*$)")
TOK_COM_HTML = re.compile(r"(&lt;!--.*?--&gt;)")
TOK_COM_SH = re.compile(r"(#.*$)")
TOK_HTML_STR = re.compile(r'("[^"]*")')

def _f(color, txt, italic=False, bold=False):
    fname = "Mono-It" if italic else ("Mono-Bd" if bold else "Mono")
    return f'<font color="{color}" name="{fname}">{txt}</font>'

def _php_segment(seg):
    """Colorize keywords/vars/functions/numbers + html tags in a non-string PHP segment."""
    out = []
    pos = 0
    # first split html tags
    for m in TOK_TAG.finditer(seg):
        out.append(_php_tokens(seg[pos:m.start()]))
        tag = m.group(1)
        # color strings inside tag differently
        sub = []
        p2 = 0
        for ms in TOK_HTML_STR.finditer(tag):
            sub.append(_f(C_TAG, tag[p2:ms.start()]))
            sub.append(_f(C_STR, ms.group(1)))
            p2 = ms.end()
        sub.append(_f(C_TAG, tag[p2:]))
        out.append("".join(sub))
        pos = m.end()
    out.append(_php_tokens(seg[pos:]))
    return "".join(out)

def _php_tokens(txt):
    if not txt:
        return ""
    out = []
    pos = 0
    for m in TOK_PHP.finditer(txt):
        out.append(txt[pos:m.start()])
        if m.group(1):
            out.append(_f(C_VAR, m.group(1)))
        elif m.group(2):
            out.append(_f(C_KEY, m.group(2), bold=(m.group(2) in ("echo", "function", "return"))))
        elif m.group(3):
            out.append(_f(C_FUN, m.group(3)))
        elif m.group(4):
            out.append(_f(C_NUM, m.group(4)))
        pos = m.end()
    out.append(txt[pos:])
    return "".join(out)

def hi_php(line):
    esc = xml_escape(line)
    parts = TOK_COM_PHP.split(esc)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:                       # comentário
            out.append(_f(C_COM, part, italic=True))
            continue
        sub = TOK_PTAG.split(part)
        for j, piece in enumerate(sub):
            if j % 2 == 1:
                out.append(_f(C_KEY, piece, bold=True))
                continue
            sp = TOK_STR.split(piece)
            for k, seg in enumerate(sp):
                if k % 2 == 1:
                    out.append(_f(C_STR, seg))
                else:
                    out.append(_php_segment(seg))
    return "".join(out)

def hi_html(line):
    esc = xml_escape(line)
    parts = TOK_COM_HTML.split(esc)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(_f(C_COM, part, italic=True))
            continue
        # blocos <?php ... ?> dentro de html
        sub = TOK_PTAG.split(part)
        for j, piece in enumerate(sub):
            if j % 2 == 1:
                out.append(_f(C_KEY, piece, bold=True))
                continue
            tags = TOK_TAG.split(piece)
            for k, seg in enumerate(tags):
                if k % 2 == 1:
                    sp = TOK_HTML_STR.split(seg)
                    out.append("".join(_f(C_TAG, x) if idx % 2 == 0 else _f(C_STR, x)
                                       for idx, x in enumerate(sp)))
                else:
                    out.append(_html_text(seg))
    return "".join(out)

TOK_ENTITY_TEXT = re.compile(r"(&\w+;)")
def _html_text(seg):
    """Texto fora de tags: mantém entidades visíveis em âmbar suave."""
    if not seg:
        return ""
    return seg

def hi_text(line):
    esc = xml_escape(line)
    parts = TOK_COM_SH.split(esc)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(_f(C_COM, part, italic=True))
        else:
            out.append(part)
    return "".join(out)

def hi_shell(line):
    esc = xml_escape(line)
    parts = TOK_COM_SH.split(esc)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(_f(C_COM, part, italic=True))
        else:
            m = re.match(r"^(\s*)([a-zA-Z][\w-]*)", part)
            if m:
                out.append(m.group(1) + _f(C_FUN, m.group(2), bold=True) + part[m.end():])
            else:
                out.append(part)
    return "".join(out)


VB_WORDS = ("Dim|As|Sub|End|Function|If|Then|Else|ElseIf|For|Next|Do|While|Loop|Until|Select|Case|"
            "Public|Private|Print|Set|New|Not|And|Or|Mod|To|Step|ByVal|ByRef|Type|With|Exit|On|Error|"
            "GoTo|Is|Nothing|True|False|Call|Each|In|Wend|Option|Base|Rem|InputBox|MsgBox|Val|Format")
SQL_WORDS = ("SELECT|FROM|WHERE|INSERT|INTO|VALUES|UPDATE|SET|DELETE|CREATE|TABLE|DATABASE|USE|SHOW|"
             "ORDER|BY|GROUP|AND|OR|NOT|LIKE|BETWEEN|IN|PRIMARY|KEY|AUTO_INCREMENT|INT|VARCHAR|"
             "DECIMAL|DATE|AS|COUNT|SUM|AVG|MAX|MIN|DESC|ASC|DISTINCT|LIMIT|JOIN|LEFT|INNER|ON")

def _vb_seg(seg):
    seg2 = re.sub(r"\b(" + VB_WORDS + r")\b",
                  lambda m: _f(C_KEY, m.group(1), bold=m.group(1) in ("Sub", "Function", "Dim", "End")),
                  seg)
    seg2 = re.sub(r"\b(\d+(?:\.\d+)?)\b", lambda m: _f(C_NUM, m.group(1)), seg2)
    return seg2

def hi_vb(line):
    esc = xml_escape(line)
    instr = False; ci = -1
    for i, ch in enumerate(esc):
        if ch == '"':
            instr = not instr
        elif ch == "'" and not instr:
            ci = i; break
    code, com = (esc[:ci], esc[ci:]) if ci >= 0 else (esc, None)
    parts = TOK_STR.split(code)
    out = []
    for k, seg in enumerate(parts):
        if k % 2 == 1:
            out.append(_f(C_STR, seg))
        else:
            out.append(_vb_seg(seg))
    if com:
        out.append(_f(C_COM, com, italic=True))
    return "".join(out)

def _sql_seg(seg):
    seg2 = re.sub(r"\b(" + SQL_WORDS + r")\b",
                  lambda m: _f(C_KEY, m.group(1),
                               bold=m.group(1) in ("SELECT", "INSERT", "UPDATE", "DELETE", "CREATE")),
                  seg, flags=re.I)
    seg2 = re.sub(r"\b(\d+(?:\.\d+)?)\b", lambda m: _f(C_NUM, m.group(1)), seg2)
    return seg2

def hi_sql(line):
    esc = xml_escape(line)
    parts = re.split(r"(--.*$)", esc)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(_f(C_COM, p, italic=True)); continue
        sp = re.split(r"('[^']*')", p)
        for k, seg in enumerate(sp):
            if k % 2 == 1:
                out.append(_f(C_STR, seg))
            else:
                out.append(_sql_seg(seg))
    return "".join(out)

HILITE = {"php": hi_php, "html": hi_html, "shell": hi_shell, "vb": hi_vb, "sql": hi_sql,
          "texto": hi_text, "text": hi_text, "": hi_text}

# ---------------------------------------------------------------------------
# FLOWABLES AUXILIARES
# ---------------------------------------------------------------------------
class TocFlowMixin:
    def set_toc(self, level, text):
        self._tocEntry = (level, text)
        return self

class TocParagraph(Paragraph):
    def __init__(self, text, style, toc=None):
        super().__init__(safe_para(text), style)
        if toc:
            self._tocEntry = toc

class TocTable(Table):
    def __init__(self, *a, toc=None, **kw):
        super().__init__(*a, **kw)
        if toc:
            self._tocEntry = toc

def rounded(data, colWidths, bg, radius=7, pad=10, border=None, extra=None):
    t = Table(data, colWidths=colWidths)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("ROUNDEDCORNERS", [radius, radius, radius, radius]),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), pad - 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    if border:
        cmds.append(("BOX", (0, 0), (-1, -1), 0.9, border))
    if extra:
        cmds.extend(extra)
    t.setStyle(TableStyle(cmds))
    return t

def make_code(spec, width=None):
    """Painel de código com barra de título."""
    width = width or TW
    lang = spec.get("ling", "php")
    hi = HILITE.get(lang, hi_text)
    titulo = spec.get("titulo", "")
    linhas = spec.get("linhas", [])
    bar = Table([[Paragraph(safe_para(titulo) or "&nbsp;", S["code_title"]),
                  Paragraph(lang.upper(), S["code_lang"])]],
                colWidths=[width * 0.82, width * 0.18])
    bar.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BAR),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROUNDEDCORNERS", [7, 7, 0, 0]),
    ]))
    body_rows = []
    for ln in linhas:
        markup = hi(ln) if ln.strip() else "&nbsp;"
        body_rows.append([Paragraph(markup, S["code"])])
    if not body_rows:
        body_rows = [[Paragraph("&nbsp;", S["code"])]]
    body = Table(body_rows, colWidths=[width])
    body.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
        ("TOPPADDING", (0, 0), (0, 0), 7),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROUNDEDCORNERS", [0, 0, 7, 7]),
    ]))
    outer = Table([[bar], [body]], colWidths=[width])
    outer.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return KeepTogether([Spacer(1, 3), outer, Spacer(1, 7)])

BOX_STYLE = {
    "conceito": (SKY, PRIMARY, "CONCEITO-CHAVE"),
    "analogia": (HexColor("#EFF3FB"), PRIMARY_D, "ANALOGIA"),
    "dica":     (AMBER_BG, AMBER_D, "DICA"),
    "atencao":  (RED_BG, RED, "ATENÇÃO"),
    "prof":     (GREEN_BG, GREEN, "GABARITO — VERSÃO DO PROFESSOR"),
    "prof_o":   (GREEN_BG, GREEN, "ORIENTAÇÕES DE CORREÇÃO — VERSÃO DO PROFESSOR"),
}

def make_box(kind, text, title=None):
    bg, fg, default_title = BOX_STYLE[kind]
    tit = title if title is not None else default_title
    tst = ParagraphStyle("t", parent=S["box_title"], textColor=fg)
    bst = ParagraphStyle("b", parent=S["box_text"])
    cell = [Paragraph(safe_para(tit), tst), Paragraph(safe_para(text), bst)]
    t = rounded([[cell]], [TW], bg, pad=11, extra=[("LINEBEFORE", (0, 0), (0, -1), 3.2, fg)])
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 7)])

def make_table(spec, width=None):
    width = width or TW
    cab, lin = spec["cab"], spec["lin"]
    nc = len(cab)
    if spec.get("larguras"):
        tot = float(sum(spec["larguras"]))
        cw = [width * w / tot for w in spec["larguras"]]
    else:
        cw = [width / nc] * nc
    data = [[Paragraph(safe_para(c), S["th"]) for c in cab]]
    for row in lin:
        cells = []
        for i, c in enumerate(row):
            st = S["td_j"] if (isinstance(c, str) and len(plain(c)) > 60) else S["td"]
            cells.append(Paragraph(safe_para(c), st))
        data.append(cells)
    t = Table(data, colWidths=cw, repeatRows=1)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("GRID", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(cmds))
    out = []
    if spec.get("titulo"):
        out.append(Paragraph(safe_para(spec["titulo"]),
                             ParagraphStyle("ct", parent=S["box_title"], fontSize=9,
                                            textColor=INK_SOFT)))
        out.append(Spacer(1, 2))
    out.append(t)
    out.append(Spacer(1, 8))
    return out

def render_bloco(b, story):
    kind = b[0]
    if kind == "p":
        story.append(P(b[1], S["body"]))
    elif kind == "h":
        story.append(P(b[1], S["h_sub"]))
    elif kind == "lista":
        for item in b[1]:
            story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(item), S["li"]))
        story.append(Spacer(1, 4))
    elif kind == "lista_num":
        for i, item in enumerate(b[1], 1):
            story.append(Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;" + safe_para(item), S["li_num"]))
        story.append(Spacer(1, 4))
    elif kind in ("conceito", "analogia"):
        title, text = b[1]
        story.append(make_box(kind, text, title=title))
    elif kind in ("dica", "atencao"):
        story.append(make_box(kind, b[1]))
    elif kind == "codigo":
        story.append(make_code(b[1]))
    elif kind == "tabela":
        story.extend(make_table(b[1]))

def render_blocos(blocos, story):
    for b in blocos:
        render_bloco(b, story)

# ---------------------------------------------------------------------------
# CABEÇALHOS DE SEÇÃO (bands)
# ---------------------------------------------------------------------------
def band(title, sub=None, bg=PRIMARY, width=None):
    width = width or TW
    cell = [Paragraph(safe_para(title), S["band"])]
    if sub:
        cell.append(Paragraph(safe_para(sub), S["band_sub"]))
    t = rounded([[cell]], [width], bg, pad=10)
    return KeepTogether([Spacer(1, 6), t, Spacer(1, 9)])

def module_header(m, parte_info):
    kick = (f"MÓDULO {m['num']} &nbsp;·&nbsp; {m['aulas_faixa'].upper()} "
            f"&nbsp;·&nbsp; {m['semanas'].upper()}")
    meta = f"PARTE {ROMAN[m['parte_num']]} — {m['parte_titulo'].upper()}"
    cell = [Paragraph(kick, S["mod_kick"]),
            Paragraph(safe_para(m["titulo"]), S["mod_title"]),
            Spacer(1, 2),
            Paragraph(safe_para(meta), S["mod_meta"])]
    t = TocTable([[cell]], colWidths=[TW],
                 toc=(1, f"Módulo {m['num']} — {plain(m['titulo'])} ({m['aulas_faixa']})"))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("ROUNDEDCORNERS", [9, 9, 9, 9]),
        ("LINEBELOW", (0, 0), (-1, 0), 0, NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 13),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
    ]))
    return KeepTogether([PageBreak(), t, Spacer(1, 10)])

def aula_header(aula):
    kick = f"AULA {aula['num']}"
    cell = [Paragraph(kick, S["aula_kick"]),
            Paragraph(safe_para(aula["titulo"]), S["aula"])]
    bar = Table([["", cell]], colWidths=[0.16 * cm, TW - 0.16 * cm])
    bar.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), AMBER),
        ("BACKGROUND", (1, 0), (1, 0), SKY),
        ("ROUNDEDCORNERS", [0, 6, 6, 0]),
        ("LEFTPADDING", (1, 0), (1, 0), 11),
        ("RIGHTPADDING", (1, 0), (1, 0), 11),
        ("TOPPADDING", (1, 0), (1, 0), 7),
        ("BOTTOMPADDING", (1, 0), (1, 0), 7),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return KeepTogether([Spacer(1, 10), bar, Spacer(1, 8)])

def objetivos_box(m):
    items = [Paragraph("✓&nbsp;&nbsp;" + safe_para(o), S["obj_li"]) for o in m["objetivos"]]
    cell = [Paragraph("OBJETIVOS DE APRENDIZAGEM", S["obj_title"])] + items
    t = rounded([[cell]], [TW], SKY, pad=12,
                extra=[("LINEBEFORE", (0, 0), (0, -1), 3.2, PRIMARY)])
    return KeepTogether([t, Spacer(1, 6)])

# ---------------------------------------------------------------------------
# EXERCÍCIOS / TESTE RÁPIDO
# ---------------------------------------------------------------------------
def exercicio_card(m, ex, professor):
    tipo = {"pratico": "PRÁTICO · LABORATÓRIO", "escrito": "ESCRITO",
            "grupo": "EM GRUPO"}.get(ex["tipo"], "EXERCÍCIO")
    header = Table(
        [[Paragraph(f"EXERCÍCIO {ex['num']} — {safe_para(ex['titulo'])}", S["ex_title"]),
          Paragraph(tipo, ParagraphStyle("chip", fontName="Inter-Bk", fontSize=7.4,
                                         leading=10, textColor=AMBER_D, alignment=TA_RIGHT))]],
        colWidths=[TW * 0.74, TW * 0.26])
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), AMBER_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, AMBER),
        ("ROUNDEDCORNERS", [6, 6, 0, 0]),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    body = [[Paragraph(safe_para(ex["enunciado"]), S["body_c"])]]
    if ex.get("passos"):
        for i, p_ in enumerate(ex["passos"], 1):
            body.append([Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{safe_para(p_)}", S["li_num"])])
    if ex.get("codigo"):
        pass
    body_t = Table(body, colWidths=[TW])
    body_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FFFDF7")),
        ("BOX", (0, 0), (-1, -1), 0.8, HexColor("#EAD9B5")),
        ("LINEABOVE", (0, 0), (-1, 0), 0, white),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROUNDEDCORNERS", [0, 0, 6, 6]),
    ]))
    story = [Spacer(1, 4), header, body_t]
    if ex.get("codigo"):
        story.append(Spacer(1, 5))
        story.append(make_code(ex["codigo"]))
    if professor:
        if ex.get("esperado"):
            story.append(make_box("prof", ex["esperado"], title="RESULTADO ESPERADO"))
        if ex.get("orientacao"):
            story.append(make_box("prof_o", ex["orientacao"]))
    else:
        story.append(Spacer(1, 6))
    return KeepTogether(story) if len(story) <= 4 else story

def quiz(m, professor):
    story = [band(f"⚡ TESTE RÁPIDO — MÓDULO {m['num']}: {plain(m['titulo'])}",
                  "5 questões objetivas · responda sem consultar o material e depois corrija"
                  + (" · gabarito comentado incluído" if professor else ""),
                  bg=PRIMARY_D)]
    letters = ["A", "B", "C", "D"]
    for i, q in enumerate(m["teste_rapido"], 1):
        item = [Paragraph(f"<b>{i}.</b>&nbsp; {safe_para(q['enunciado'])}", S["q"])]
        for li, alt in enumerate(q["alt"]):
            item.append(Paragraph(f"<b>({letters[li]})</b>&nbsp;&nbsp;{safe_para(alt)}", S["alt"]))
        if professor:
            gab = rounded([[ [Paragraph(f"RESPOSTA: <b>{letters[q['resposta']]}</b>", S["gab_title"]),
                              Paragraph(safe_para(q.get("comentario", "")), S["gab_text"])] ]],
                          [TW - 1.2 * cm], GREEN_BG, radius=6, pad=8,
                          extra=[("LINEBEFORE", (0, 0), (0, -1), 2.6, GREEN)])
            item.append(Spacer(1, 3))
            item.append(Table([[gab]], colWidths=[TW]))
            item[-1].setStyle(TableStyle([
                ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        else:
            item.append(Paragraph("Sua resposta: ( &nbsp;&nbsp;&nbsp; )", S["ans"]))
        item.append(Spacer(1, 8))
        story.append(KeepTogether(item))
    return story

# ---------------------------------------------------------------------------
# MÓDULO COMPLETO
# ---------------------------------------------------------------------------
def build_module(m, professor):
    story = [module_header(m, None), objetivos_box(m)]
    for aula in m["aulas"]:
        story.append(aula_header(aula))
        render_blocos(aula["blocos"], story)
    # exercícios
    story.append(band(f"🛠 EXERCÍCIOS — MÓDULO {m['num']}",
                      "Atividades práticas e escritas · resolva no laboratório e complete em casa (AVA)",
                      bg=HexColor("#B4700A")))
    for ex in m["exercicios"]:
        card = exercicio_card(m, ex, professor)
        if isinstance(card, list):
            story.extend(card)
        else:
            story.append(card)
    # teste rápido
    story.extend(quiz(m, professor))
    # referência a avaliação
    if m.get("avaliacao_ref"):
        ref = {"A1": "AVALIAÇÃO 1 (A1 — 30 pts): trabalho “site da empresa fictícia” (10 pts) + "
                     "atividades AVA (5 pts) + teste escrito-prático (15 pts). "
                     "Enunciado completo e rubrica na seção AVALIAÇÕES.",
               "A1-teste": "Semana 8: TESTE ESCRITO-PRÁTICO da A1 (15 pts) sobre Web e HTML. "
                           "Modelo completo na seção AVALIAÇÕES.",
               "A2": "AVALIAÇÃO 2 (A2 — 30 pts): prova obrigatória nesta semana (aula 48) — "
                     "HTML, PHP e GET/POST. Modelo completo na seção AVALIAÇÕES.",
               "A3": "AVALIAÇÃO 3 (A3 — 40 pts): prova escrita final individual (30 pts, aulas 70–71) "
                     "+ projeto e apresentação (10 pts, aula 72). Modelo e rubrica na seção AVALIAÇÕES."}
        story.append(make_box("dica", ref[m["avaliacao_ref"]], title="📝 AVALIAÇÃO À VISTA"))
    return story

# ---------------------------------------------------------------------------
# DIVISÓRIAS DE PARTE / CAPA
# ---------------------------------------------------------------------------
def part_divider(parte, mods_info, note=None):
    roman = ROMAN[parte["num"]]
    chip = rounded([[Paragraph(f"{parte['aulas'].upper()} &nbsp;&nbsp;·&nbsp;&nbsp; {parte['semanas'].upper()}",
                               ParagraphStyle("c", fontName="Inter-Bk", fontSize=9.5,
                                              leading=13, textColor=NAVY))]],
                   [TW * 0.62], AMBER, radius=14, pad=8)
    mods_lines = [Paragraph(f"<b>Módulo {n}</b> — {safe_para(t)}",
                            ParagraphStyle("ml", fontName="Inter", fontSize=10.5, leading=17,
                                           textColor=HexColor("#C9DCF2")))
                  for n, t in mods_info]
    cell = [Paragraph(f"PARTE {roman}", S["part_num"]),
            Spacer(1, 2),
            HRFlowable(width="26%", thickness=3, color=AMBER, hAlign="LEFT",
                       spaceBefore=2, spaceAfter=12),
            Paragraph(safe_para(parte["titulo"].upper()), S["part_title"]),
            Spacer(1, 12), chip, Spacer(1, 16)] + mods_lines
    if note:
        cell.append(Spacer(1, 14))
        cell.append(Paragraph(safe_para(note),
                              ParagraphStyle("nt", fontName="Inter-It", fontSize=9, leading=13,
                                             textColor=HexColor("#9FBBD9"))))
    t = TocTable([[cell]], colWidths=[TW], toc=(0, f"PARTE {roman} — {plain(parte['titulo'])}"))
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [NextPageTemplate("divider"), PageBreak(), Spacer(1, 3.2 * cm), t,
            NextPageTemplate("normal"), PageBreak()]

def big_section(title, kicker, toc=True, page_break=True):
    cell = [Paragraph(kicker.upper(), S["mod_kick"]),
            Paragraph(safe_para(title), S["mod_title"])]
    t = TocTable([[cell]], colWidths=[TW],
                 toc=(0, plain(title)) if toc else None)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 16), ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 13), ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
        ("ROUNDEDCORNERS", [9, 9, 9, 9]),
    ]))
    out = [PageBreak(), t, Spacer(1, 12)] if page_break else [t, Spacer(1, 12)]
    return out

# ---------------------------------------------------------------------------
# AVALIAÇÕES (provas)
# ---------------------------------------------------------------------------
def exam_header(titulo):
    campos = [
        [Paragraph("<b>ESCOLA:</b> Instituto Técnico — Curso Técnico em Informática", S["exam_field"])],
        [Paragraph("<b>ALUNO(A):</b> " + "_" * 66, S["exam_field"])],
        [Paragraph("<b>TURMA:</b> 2/2026&nbsp;&nbsp;&nbsp; <b>DATA:</b> ____ / ____ / ________ &nbsp;&nbsp;&nbsp;"
                    " <b>NOTA:</b> __________", S["exam_field"])],
    ]
    dados = Table(campos, colWidths=[TW - 2.4 * cm])
    dados.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    titulo_p = Paragraph(safe_para(titulo), ParagraphStyle("eh", fontName="Inter-Bk",
                                                           fontSize=12.5, leading=16,
                                                           textColor=white))
    outer = Table([[titulo_p], [dados]], colWidths=[TW - 2.4 * cm])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), NAVY),
        ("BACKGROUND", (0, 1), (0, 1), white),
        ("BOX", (0, 0), (-1, -1), 1.1, NAVY),
        ("LINEBELOW", (0, 0), (0, 0), 1.1, NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 13), ("RIGHTPADDING", (0, 0), (-1, -1), 13),
        ("TOPPADDING", (0, 0), (0, 0), 10), ("BOTTOMPADDING", (0, 0), (0, 0), 10),
        ("TOPPADDING", (0, 1), (0, 1), 8), ("BOTTOMPADDING", (0, 1), (0, 1), 8),
        ("ROUNDEDCORNERS", [8, 8, 8, 8]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return KeepTogether([outer, Spacer(1, 6)])


def answer_space(n=4, mono=False):
    st = S["line_ans"]
    lines = [Paragraph("_" * 78, st) for _ in range(n)]
    t = Table([[x] for x in lines], colWidths=[TW])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return t

LETTERS = ["A", "B", "C", "D"]

def q_objetiva(n, q, professor):
    item = [Paragraph(f"<b>Questão {n}.</b>&nbsp; {safe_para(q['enunciado'])}", S["q"])]
    for li, alt in enumerate(q["alt"]):
        item.append(Paragraph(f"<b>({LETTERS[li]})</b>&nbsp;&nbsp;{safe_para(alt)}", S["alt"]))
    if professor:
        item.append(Spacer(1, 4))
        item.append(gab_box(f"Resposta: <b>{LETTERS[q['resposta']]}</b>", q.get("comentario", "")))
    else:
        item.append(Paragraph("Resposta: ( &nbsp;&nbsp;&nbsp; )", S["ans"]))
    item.append(Spacer(1, 9))
    return item

def gab_box(title, text, code=None, criterio=None):
    cell = [Paragraph(safe_para(title), S["gab_title"])]
    if text:
        cell.append(Paragraph(safe_para(text), S["gab_text"]))
    if code:
        cell.append(Spacer(1, 4))
        st = ParagraphStyle("gc", parent=S["code"], fontSize=7.8, leading=11.4)
        st.code = None
        for ln in code:
            cell.append(Paragraph(hi_generic(ln), st))
    if criterio:
        cell.append(Spacer(1, 3))
        cell.append(Paragraph("<b>Critérios:</b> " + safe_para(criterio),
                              ParagraphStyle("cr", parent=S["gab_text"], fontSize=8.6,
                                             textColor=GREEN)))
    return rounded([[cell]], [TW], GREEN_BG, radius=6, pad=9,
                   extra=[("LINEBEFORE", (0, 0), (0, -1), 2.8, GREEN)])

def hi_generic(line):
    """Realce simples para código de gabarito: detecta html vs php vs texto."""
    stripped = line.strip()
    if stripped.startswith("<?") or "$" in line or stripped.startswith(("echo", "function", "if", "foreach", "switch", "while", "for ", "return", "define", "require", "include")):
        return hi_php(line)
    if stripped.startswith("<") or "</" in line:
        return hi_html(line)
    return hi_text(line)

def q_pratica(n, q, professor):
    item = [Paragraph(f"<b>Questão {n}.</b>&nbsp; {safe_para(q['enunciado'])}", S["q"])]
    if q.get("codigo"):
        item.append(Spacer(1, 3))
        item.append(make_code({"titulo": "Código para análise", "ling": "php",
                               "linhas": q["codigo"]}))
    if professor:
        if q.get("resposta_texto"):
            item.append(gab_box("GABARITO", q["resposta_texto"], criterio=q.get("criterio")))
        elif q.get("resposta_codigo"):
            item.append(gab_box("GABARITO — código modelo", None,
                                code=q["resposta_codigo"], criterio=q.get("criterio")))
        item.append(Spacer(1, 9))
    else:
        item.append(Paragraph("Resposta:", S["ans"]))
        item.append(answer_space(5))
        item.append(Spacer(1, 9))
    return item

def build_avaliacoes(professor):
    story = big_section("Avaliações — 100 pontos no semestre",
                        "A1 · 30 pts&nbsp;&nbsp;|&nbsp;&nbsp;A2 · 30 pts&nbsp;&nbsp;|&nbsp;&nbsp;A3 · 40 pts")
    story.append(P("Regras oficiais do Plano de Ensino e proposta de operacionalização do cronograma (S). "
                   "Os modelos de prova abaixo são <b>propostas (S)</b> — o professor pode adaptá-los.",
                   S["body"]))
    story.extend(make_table({"titulo": "Regras oficiais",
                             "cab": ["Avaliação", "Pontos", "Regra oficial"],
                             "lin": [
                                 ["1ª Avaliação", "30 pts",
                                  "Distribuídos a critério do professor (trabalhos, seminários, testes etc.), admitindo-se inclusive provas."],
                                 ["2ª Avaliação", "30 pts",
                                  "Obrigatoriamente por meio de prova; poderá ser em duplas ou com consultas."],
                                 ["3ª Avaliação", "40 pts",
                                  "30 pts obrigatoriamente em prova escrita final individual + 10 pts distribuídos a critério do professor."],
                             ], "larguras": [2.6, 1.6, 12.8]}))
    story.extend(make_table({"titulo": "Proposta de operacionalização no cronograma (S)",
                             "cab": ["Etapa", "Período", "Proposta"],
                             "lin": [[a, b, c] for a, b, c, in
                                     [(r[0], r[2], r[3]) for r in comuns.AVALIACOES_RESUMO]]}))
    story.append(make_box("conceito", "Identificação precoce de dificuldades pelos exercícios de cada aula; "
                          "revisões estratégicas ao final dos blocos (aulas 36 e 60); listas de reforço e "
                          "atividades diferenciadas no AVA; reforço dos pré-requisitos de HTML antes do PHP e "
                          "de lógica antes de formulários; nova oportunidade de demonstrar aprendizagem por "
                          "meio das entregas do projeto final.", title="APOIO E RECUPERAÇÃO (PROPOSTA — S)"))

    # ---------------- A1 ----------------
    A1 = avaliacoes.A1
    story.append(band("AVALIAÇÃO 1 (A1) — 30 PONTOS · SEMANAS 1 A 8 (S)",
                      "Trabalho HTML (10) + atividades AVA (5) + teste escrito-prático (15)",
                      bg=HexColor("#B4700A")))
    story.extend(make_table({"cab": ["Componente", "Pontos", "Quando"],
                             "lin": [[c, p, q] for c, p, q in A1["composicao"]],
                             "larguras": [9.5, 2.2, 5.3]}))
    trab = A1["trabalho"]
    story.append(P(f"<b>{trab['titulo']}</b>", S["h2"]))
    story.append(P(trab["descricao"], S["body"]))
    story.append(P("<b>Requisitos do trabalho:</b>", S["body_c"]))
    for r in trab["requisitos"]:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(r), S["li"]))
    story.append(Spacer(1, 5))
    story.extend(make_table({"titulo": "Rubrica de correção do trabalho (10 pts)",
                             "cab": ["Critério", "Pontos", "O que se espera"],
                             "lin": [[a, b, c] for a, b, c in trab["rubrica"]],
                             "larguras": [4.2, 1.6, 11.2]}))
    if professor:
        story.append(make_box("prof_o", "Aplique a rubrica item a item com visto no checklist; devolva com "
                              "feedback escrito. Trabalhos com links quebrados perdem o critério 'Estrutura e "
                              "navegação' integralmente.Combine a entrega via AVA/Drive + pasta do laboratório."))
    # teste escrito-prático
    teste = A1["teste"]
    story.append(P(f"<b>{teste['titulo']}</b>", S["h2"]))
    story.append(exam_header("AVALIAÇÃO 1 — TESTE ESCRITO-PRÁTICO (15 pts) · WEB E HTML"))
    story.append(Spacer(1, 8))
    story.append(P("<b>Instruções:</b>", S["body_c"]))
    for ins in teste["instrucoes"]:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(ins), S["li"]))
    story.append(Spacer(1, 6))
    story.append(P(teste["parte_a"]["titulo"], S["h2"]))
    n = 1
    for q in teste["parte_a"]["questoes"]:
        story.extend(q_objetiva(n, q, professor)); n += 1
    story.append(P(teste["parte_b"]["titulo"], S["h2"]))
    for q in teste["parte_b"]["questoes"]:
        story.extend(q_pratica(n, q, professor)); n += 1

    # ---------------- A2 ----------------
    A2 = avaliacoes.A2
    story.append(band("AVALIAÇÃO 2 (A2) — 30 PONTOS · SEMANA 16, AULA 48 (S)",
                      "Prova obrigatória (pode ser em duplas ou com consulta) — HTML + PHP + GET/POST",
                      bg=PRIMARY_D))
    story.append(exam_header("AVALIAÇÃO 2 — PROVA (30 pts) · HTML, PHP E FORMULÁRIOS"))
    story.append(Spacer(1, 8))
    story.append(P("<b>Instruções:</b>", S["body_c"]))
    for ins in A2["teste"]["instrucoes"]:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(ins), S["li"]))
    story.append(Spacer(1, 6))
    n = 1
    for q in A2["teste"]["questoes"]:
        if q["tipo"] == "objetiva":
            story.extend(q_objetiva(n, q, professor))
        else:
            story.extend(q_pratica(n, q, professor))
        n += 1

    # ---------------- A3 ----------------
    A3 = avaliacoes.A3
    story.append(band("AVALIAÇÃO 3 (A3) — 40 PONTOS · SEMANA 24",
                      "Prova escrita final individual (30 pts, aulas 70–71 — S) + projeto e apresentação (10 pts, aula 72)",
                      bg=NAVY2))
    story.append(exam_header("AVALIAÇÃO 3 — PROVA ESCRITA FINAL INDIVIDUAL (30 pts) · CUMULATIVA"))
    story.append(Spacer(1, 8))
    story.append(P("<b>Instruções:</b>", S["body_c"]))
    for ins in A3["teste"]["instrucoes"]:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(ins), S["li"]))
    story.append(Spacer(1, 6))
    n = 1
    for q in A3["teste"]["questoes"]:
        if q["tipo"] == "objetiva":
            story.extend(q_objetiva(n, q, professor))
        else:
            story.extend(q_pratica(n, q, professor))
        n += 1
    # rubrica do projeto
    rub = A3["projeto_rubrica"]
    story.append(P(f"<b>{rub['titulo']}</b>", S["h2"]))
    story.extend(make_table({"cab": ["Critério", "Pontos", "Descrição"],
                             "lin": [[a, b, c] for a, b, c in rub["itens"]],
                             "larguras": [4.6, 1.5, 10.9]}))
    for o in rub["observacoes"]:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(o), S["li"]))
    return story

# ---------------------------------------------------------------------------
# PROJETO FINAL / GLOSSÁRIO / BIBLIOGRAFIA / ABERTURA
# ---------------------------------------------------------------------------
def build_projeto(professor):
    PF = avaliacoes.PROJETO_FINAL
    story = big_section("Projeto Final Integrador", "Aulas 49 a 72 · semanas 17 a 24 · 6 entregas")
    story.append(P("<b>O que é:</b> " + PF["o_que_e"], S["body"]))
    story.append(P("<b>Temas sugeridos no material didático:</b> " + " · ".join(PF["temas"]) + ".", S["body"]))
    story.extend(make_table({"titulo": "Entregas do projeto",
                             "cab": ["Entrega", "Descrição", "Aulas", "Semana"],
                             "lin": [list(e) for e in PF["entregas"]],
                             "larguras": [2.2, 9.2, 2.9, 2.7]}))
    story.extend(make_table({"titulo": "Critérios sugeridos para os 10 pts (S)",
                             "cab": ["Critério", "Pontos", "O que se espera"],
                             "lin": [[a, b, c] for a, b, c in PF["criterios_10pts"]],
                             "larguras": [4.6, 1.5, 10.9]}))
    story.append(make_box("dica", "O desenvolvimento do projeto é guiado aula a aula no Módulo 12 desta "
                          "apostila: requisitos (aula 50), estrutura (51), páginas (52–55), testes (58), "
                          "correção de erros (59) e apresentação (70–72)."))
    if professor:
        story.append(make_box("prof_o", "Acompanhe as 6 entregas com vistos e feedback curto. A nota de "
                              "projeto (10 pts) considera o processo (entregas 1–5) e a apresentação final. "
                              "Sugestão: teste cruzado entre grupos na aula 69 e ensaio geral na 71."))
    return story

def build_glossario():
    story = big_section("Glossário", "Termos essenciais da disciplina")
    rows = [[Paragraph(f"<b>{safe_para(t)}</b>", S["td"]),
             Paragraph(safe_para(d), S["td_j"])] for t, d in GLOSSARIO]
    t = Table(rows, colWidths=[TW * 0.24, TW * 0.76], repeatRows=0)
    cmds = [("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 4.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5)]
    for i in range(len(rows)):
        if i % 2 == 1:
            cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(cmds))
    story.append(t)
    return story

def build_bibliografia():
    story = big_section("Bibliografia", "Oficial do Plano de Ensino")
    story.append(P("<b>Básica</b>", S["h2"]))
    for b in comuns.BIBLIOGRAFIA_BASICA:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(b), S["li"]))
    story.append(P("<b>Complementar</b>", S["h2"]))
    for b in comuns.BIBLIOGRAFIA_COMPLEMENTAR:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(b), S["li"]))
    story.append(Spacer(1, 16))
    story.append(make_box("dica", "Itens marcados com (S) neste material são propostas pedagógicas de "
                          "organização (datas de avaliações, entregas e distribuição das horas não "
                          "presenciais) — não especificadas no Plano de Ensino original. As demais "
                          "informações reproduzem o Plano de Ensino oficial da disciplina.",
                          title="COMO LER ESTE DOCUMENTO"))
    return story

def build_abertura(professor):
    story = []
    # ---- página de rosto interna + apresentação
    story.append(TocParagraph("Apresentação da apostila", S["h1"], toc=(0, "Apresentação da apostila")))
    render_blocos(comuns.APRESENTACAO, story)
    story.append(Spacer(1, 6))
    story.extend(make_table(comuns.COMO_USAR_ICONES[0][1]))
    # ---- visão geral do curso
    story.extend(big_section("Visão geral do curso", "Disciplina · carga horária · módulos · avaliações"))
    story.extend(make_table({"cab": ["Item", "Informação"],
                             "lin": [
                                 ["Disciplina", comuns.CURSO["disciplina"] + " — " + comuns.CURSO["curso"]],
                                 ["Turma", comuns.CURSO["turma"] + " · " + comuns.CURSO["eixo"]],
                                 ["Carga horária presencial", comuns.CURSO["ch_presencial"]],
                                 ["Carga horária não presencial", comuns.CURSO["ch_nao_presencial"]],
                                 ["Estrutura", comuns.CURSO["aulas"]],
                             ], "larguras": [4.6, 12.4]}))
    story.append(make_box("conceito", comuns.EMENTA, title="EMENTA (SÍNTESE OFICIAL)"))
    story.extend(make_table({"titulo": "Módulos do semestre (distribuição oficial dos conteúdos)",
                             "cab": ["#", "Módulo", "Conteúdo principal", "Aulas", "Semanas"],
                             "lin": [list(r) for r in comuns.MAPA_MODULOS],
                             "larguras": [0.8, 3.7, 8.6, 2.0, 1.9]}))
    story.append(P("<b>Metodologia (estratégias de ensino oficiais)</b>", S["h2"]))
    for m_ in comuns.METODOLOGIA:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(m_), S["li"]))
    story.append(P("<b>Recursos didáticos</b>", S["h2"]))
    for r_ in comuns.RECURSOS:
        story.append(Paragraph("•&nbsp;&nbsp;" + safe_para(r_), S["li"]))
    story.append(Spacer(1, 4))
    story.extend(make_table({"titulo": "Atividades extraclasse orientadas — 10 h (proposta — S)",
                             "cab": ["Fase", "Semanas", "Horas", "Atividades previstas"],
                             "lin": [list(r) for r in comuns.ATIVIDADES_EXTRACLASSE],
                             "larguras": [4.0, 2.2, 1.4, 9.4]}))
    story.extend(make_table({"titulo": "Avaliações — 100 pontos no semestre",
                             "cab": ["Avaliação", "Pontos", "Período", "Composição (proposta — S)"],
                             "lin": [[a, b, c, d] for a, b, c, d in
                                     [(r[0], r[1], r[2], r[3]) for r in comuns.AVALIACOES_RESUMO]],
                             "larguras": [2.4, 1.5, 2.9, 10.2]}))
    return story

def build_sumario():
    story = [PageBreak(),
             TocParagraph("Sumário", S["h1"], toc=None),
             Spacer(1, 4)]
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]
    toc.dotsMinLevel = 0
    story.append(toc)
    return story

# ---------------------------------------------------------------------------
# DOCUMENTO
# ---------------------------------------------------------------------------
class MyDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        entry = getattr(flowable, "_tocEntry", None)
        if entry:
            level, text = entry
            self.notify("TOCEntry", (level, text, self.page))

def _paint_navy(c, doc):
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # círculos decorativos
    c.setFillColor(NAVY2)
    c.circle(PAGE_W - 1.2 * cm, PAGE_H - 2.2 * cm, 3.4 * cm, stroke=0, fill=1)
    c.circle(0.6 * cm, 2.4 * cm, 2.6 * cm, stroke=0, fill=1)
    c.setFillColor(HexColor("#1B4B85"))
    c.circle(PAGE_W - 2.6 * cm, PAGE_H - 3.4 * cm, 1.7 * cm, stroke=0, fill=1)
    # barra laranja
    c.setFillColor(AMBER)
    c.rect(0, PAGE_H - 0.45 * cm, PAGE_W, 0.45 * cm, stroke=0, fill=1)
    c.restoreState()

def capa_page(c, doc):
    _paint_navy(c, doc)

def divider_page(c, doc):
    _paint_navy(c, doc)
    c.saveState()
    c.setFillColor(AMBER)
    c.rect(0, 0, PAGE_W, 0.35 * cm, stroke=0, fill=1)
    c.setFont("Inter-Md", 8)
    c.setFillColor(HexColor("#9FBBD9"))
    c.drawString(ML, 0.75 * cm, "PROGRAMAÇÃO PARA INTERNET I · CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026")
    c.drawRightString(PAGE_W - MR, 0.75 * cm, f"{doc.page}")
    c.restoreState()

def normal_page(c, doc):
    c.saveState()
    # barra superior
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 0.28 * cm, PAGE_W, 0.28 * cm, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.rect(0, PAGE_H - 0.36 * cm, PAGE_W * 0.32, 0.08 * cm, stroke=0, fill=1)
    # cabeçalho
    c.setFont("Inter-Sb", 7.3)
    c.setFillColor(INK_SOFT)
    c.drawString(ML, PAGE_H - 0.95 * cm, comuns.META["header"])
    c.setFont("Inter-Md", 7.3)
    c.drawRightString(PAGE_W - MR, PAGE_H - 0.95 * cm,
                      "CURSO TÉCNICO EM INFORMÁTICA · TURMA 2/2026")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(ML, PAGE_H - 1.18 * cm, PAGE_W - MR, PAGE_H - 1.18 * cm)
    # rodapé
    c.line(ML, MB - 0.45 * cm, PAGE_W - MR, MB - 0.45 * cm)
    c.setFont("Inter-Md", 7.6)
    c.setFillColor(INK_SOFT)
    vers = "VERSÃO DO PROFESSOR · COM GABARITOS" if doc.professor else "VERSÃO DO ALUNO"
    c.drawString(ML, MB - 0.95 * cm, vers)
    c.drawCentredString(PAGE_W / 2 + 1.2 * cm, MB - 0.95 * cm, comuns.META.get("rodape", "(S) = proposta pedagógica"))
    # número de página em “círculo”
    c.setFillColor(NAVY)
    c.circle(PAGE_W - MR - 0.35 * cm, MB - 0.82 * cm, 0.34 * cm, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Inter-Bd", 8.6)
    c.drawCentredString(PAGE_W - MR - 0.35 * cm, MB - 0.95 * cm, str(doc.page))
    c.restoreState()

def build(professor, out_path):
    doc = MyDoc(out_path, pagesize=A4,
                leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
                title=comuns.META["titulo_doc"] + " — Apostila Completa ("
                      + ("Professor" if professor else "Aluno") + ")",
                author="Curso Técnico em Informática — Turma 2/2026",
                subject="Teoria, exercícios, testes rápidos e avaliações — 72 aulas / 24 semanas")
    doc.professor = professor

    frame_normal = Frame(ML, MB, TW, PAGE_H - MT - MB, id="normal",
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame_big = Frame(ML, MB, TW, PAGE_H - 2.2 * cm - MB, id="big",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="capa", frames=[frame_big], onPage=capa_page),
        PageTemplate(id="divider", frames=[frame_big], onPage=divider_page),
        PageTemplate(id="normal", frames=[frame_normal], onPage=normal_page),
    ])

    story = []
    # ============ CAPA ============
    vers_stamp = ("VERSÃO DO PROFESSOR · CONTÉM GABARITOS" if professor else "VERSÃO DO ALUNO")
    stamp_bg = AMBER if professor else HexColor("#9CC3EC")
    capa_cell = [
        Spacer(1, 0.6 * cm),
        Paragraph(comuns.META["kicker"],
                  ParagraphStyle("ck", fontName="Inter-Bk", fontSize=9.5, leading=13,
                                 textColor=AMBER)),
        Spacer(1, 0.5 * cm),
        Paragraph(comuns.META["titulo_capa"], S["cap"]),
        Spacer(1, 0.45 * cm),
        HRFlowable(width="34%", thickness=3.4, color=AMBER, hAlign="LEFT", spaceAfter=16),
        Paragraph(comuns.META["sub_capa"], S["cap2"]),
        Spacer(1, 1.1 * cm),
    ]
    info_rows = [
        ["72 aulas · 24 semanas", "3 aulas semanais (50 min)"],
        ["60 h presenciais", "10 h não presenciais (AVA)"],
        ["12 módulos · 6 partes", "3 avaliações · 100 pts"],
    ]
    info_t = Table([[Paragraph(f"<b>{r[0]}</b>", ParagraphStyle("iA", fontName="Inter-Bd",
                                                                 fontSize=10.5, leading=14,
                                                                 textColor=white)),
                     Paragraph(r[1], ParagraphStyle("iB", fontName="Inter-Md", fontSize=9.6,
                                                    leading=14, textColor=HexColor("#BBD4EE")))]
                    for r in info_rows],
                   colWidths=[TW * 0.42, TW * 0.58])
    info_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY2),
        ("ROUNDEDCORNERS", [9, 9, 9, 9]),
        ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, -2), 0.7, HexColor("#2A527F")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    capa_cell += [info_t, Spacer(1, 1.0 * cm)]
    stamp = rounded([[Paragraph(vers_stamp, ParagraphStyle("st", fontName="Inter-Bk",
                                                           fontSize=11.5, leading=15,
                                                           textColor=NAVY))]],
                    [TW * 0.86], stamp_bg, radius=8, pad=10)
    capa_cell += [stamp, Spacer(1, 0.9 * cm),
                  Paragraph("Material elaborado a partir do Plano de Ensino e do Cronograma oficiais "
                            "da disciplina · Setembro / 2026 · " + comuns.CURSO["docente"],
                            ParagraphStyle("ft", fontName="Inter-Md", fontSize=8.6, leading=12.5,
                                           textColor=HexColor("#9FBBD9")))]
    capa_t = Table([[capa_cell]], colWidths=[TW])
    capa_t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story += [capa_t, NextPageTemplate("normal"), PageBreak()]

    # ============ ABERTURA ============
    story += build_abertura(professor)
    # ============ SUMÁRIO ============
    story += build_sumario()

    # ============ PARTES E MÓDULOS ============
    ordem_partes = comuns.ORDEM_PARTES
    notas = {
        3: "Observação: a aula 36 (revisão cumulativa + projeto PHP), ministrada na semana 12, "
           "pertence ao Módulo 10 — seu conteúdo completo está na Parte V.",
        5: "O Módulo 10 inclui a aula 36 (revisão cumulativa), ministrada na semana 12, ao final "
           "da Parte III — conforme a tabela oficial de módulos do cronograma.",
    }
    for parte in comuns.PARTES:
        mods = ordem_partes[parte["num"]]
        mods_info = [(n, MODULOS_POR_NUM[n]["titulo"]) for n in mods]
        story += part_divider(parte, mods_info, note=comuns.NOTAS_PARTES.get(parte["num"]))
        for n in mods:
            story += build_module(MODULOS_POR_NUM[n], professor)

    # ============ PROJETO FINAL ============
    story += build_projeto(professor)
    # ============ AVALIAÇÕES ============
    story += build_avaliacoes(professor)
    # ============ GLOSSÁRIO ============
    story += build_glossario()
    # ============ BIBLIOGRAFIA ============
    story += build_bibliografia()

    # página final
    story.append(Spacer(1, 1.2 * cm))
    fim = rounded([[ [Paragraph("Bons estudos e bom código! 💻",
                                ParagraphStyle("fim1", fontName="Inter-Bk", fontSize=15,
                                               leading=20, textColor=white)),
                      Spacer(1, 4),
                      Paragraph(comuns.META["fecho"],
                                ParagraphStyle("fim2", fontName="Inter-Md", fontSize=8.8, leading=13,
                                               textColor=HexColor("#BBD4EE")))] ]],
                  [TW], NAVY, radius=9, pad=16)
    story.append(fim)

    doc.multiBuild(story)
    print(f"OK: {out_path}")

if __name__ == "__main__":
    suf = comuns.META["slug"]
    build(False, os.path.join(_ROOT, "output", f"Apostila_{suf}_ALUNO.pdf"))
    build(True, os.path.join(_ROOT, "output", f"Apostila_{suf}_PROFESSOR.pdf"))
