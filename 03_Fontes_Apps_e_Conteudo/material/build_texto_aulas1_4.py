# -*- coding: utf-8 -*-
"""Texto de apoio — Aulas 1 a 4 (Fundamentos da Internet e da Web).
Gera PDF no padrão visual da disciplina com: texto corrido para falar em sala,
resumo 'em uma frase' por aula, termos para o quadro e perguntas orais.
Uso: python3 build_texto_aulas1_4.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Spacer

from build_pdf import P, S, make_box, big_section
from build_tutoriais import build_doc, capa


def story():
    st = []
    st += capa("Fundamentos da Internet<br/>e da Web",
               "Texto de apoio para falar sobre as Aulas 1 a 4 — Parte I do cronograma. "
               "Linguagem simples, com analogias do cotidiano: para ler em voz alta, "
               "explicar no quadro ou entregar como leitura introdutória.",
               "AULAS 1 A 4 · PARTE I · SEMANAS 1 E 2", HexColor("#9CC3EC"))

    st += big_section("O textinho (para falar ou ler com a turma)", "≈ 5 minutos · tom de conversa", page_break=False)

    st.append(P("<b>Abrindo o assunto</b>", S["h2"]))
    st.append(P("Todo dia a gente abre o celular, digita o endereço de um site ou aperta o play de um "
                "vídeo — e tudo aparece na tela como mágica. Mas não é mágica: é um caminho bem "
                "organizado que a informação percorre até chegar a você. Nas aulas 1 a 4, nós vamos "
                "entender esse caminho: o que é a Internet, como a Web funciona, quem guarda os sites "
                "e que tipos de site existem por aí.", S["body"]))

    st.append(P("<b>Aula 1 — O que é a Internet?</b>", S["h2"]))
    st.append(P("A Internet é uma <b>rede mundial de redes</b>: bilhões de computadores, celulares e "
                "servidores ligados entre si, trocando informações por meio de regras comuns. A "
                "<b>Web</b> — esse universo de páginas e sites que a gente acessa — é <b>um dos serviços</b> "
                "que funcionam sobre a Internet, assim como o e-mail, o streaming e os jogos on-line. "
                "E nessa conversa existem dois papéis: o <b>cliente</b>, que pede (o seu navegador), e o "
                "<b>servidor</b>, que atende (a máquina, ligada sem parar, que guarda o site). Pense num "
                "restaurante: você é o cliente, o garçom leva o pedido, a cozinha prepara e o prato volta "
                "prontinho para a mesa.", S["body"]))

    st.append(P("<b>Aula 2 — Como a Web funciona?</b>", S["h2"]))
    st.append(P("Cada clique seu vira uma <b>requisição</b>: o navegador pede uma página; o servidor "
                "processa o pedido e devolve uma <b>resposta</b> com o conteúdo. Essa conversa segue um "
                "protocolo chamado <b>HTTP</b> — e, quando aparece o cadeado ao lado do endereço, é "
                "<b>HTTPS</b>: a mesma conversa, só que <b>criptografada</b>, protegida de curiosos no "
                "caminho. O endereço completo que você digita é a <b>URL</b>, e ela tem partes com funções "
                "certas: o <b>protocolo</b> (como conversar), o <b>domínio</b> (com quem conversar), o "
                "<b>caminho e o recurso</b> (o que você quer) e, às vezes, <b>parâmetros</b> depois do "
                "ponto de interrogação.", S["body"]))

    st.append(P("<b>Aula 3 — Domínio, hospedagem e servidor Web</b>", S["h2"]))
    st.append(P("Nos bastidores, toda máquina conectada tem um “número de casa”: o <b>endereço IP</b>. "
                "Como decorar números seria impossível, existem os <b>domínios</b> — os nomes amigáveis, "
                "registrados por exemplo no registro.br — e o <b>DNS</b>, que funciona como a grande "
                "<b>agenda telefônica</b> da Internet: você digita o nome, ele traduz para o número certo. "
                "E para o site ficar no ar 24 horas por dia, seus arquivos moram numa <b>hospedagem</b>: "
                "um espaço em um <b>servidor Web</b> sempre ligado, que atende cada requisição que chega.",
                S["body"]))

    st.append(P("<b>Aula 4 — Portais, e-business e e-commerce</b>", S["h2"]))
    st.append(P("Por fim, olhamos para os <b>tipos de site</b> que encontramos na Web. <b>Portal</b> é o "
                "site que concentra conteúdo e serviços num lugar só — como um portal de notícias ou o "
                "portal acadêmico da escola. <b>e-Business</b> é o negócio inteiro conduzido de forma "
                "digital: atendimento, fornecedores, marketing. E <b>e-commerce</b> é a parte que vende: a "
                "<b>loja virtual</b>, com aquele fluxo que você já conhece de cor — página inicial, "
                "catálogo, ficha do produto, carrinho e checkout.", S["body"]))

    st.append(P("<b>Fechando a ideia</b>", S["h2"]))
    st.append(P("Resumindo em uma imagem só: a <b>Internet é a estrada</b>, a <b>Web é o trânsito de "
                "páginas</b> que passa por ela, o <b>servidor é quem entrega</b> a carga e o <b>domínio é o "
                "endereço</b> escrito na placa. A partir da próxima aula, nós deixamos de só visitar sites "
                "e começamos a <b>construir os nossos</b>.", S["body"]))

    # ---- resumo em uma frase ----
    st += big_section("Em uma frase (para escrever no quadro)", "O essencial de cada aula")
    for t in [
        "<b>Aula 1:</b> Internet é a rede mundial; a Web é um dos serviços dela; navegador é o cliente e o "
        "servidor Web é quem atende.",
        "<b>Aula 2:</b> a Web funciona em requisição e resposta (HTTP/HTTPS); a URL junta protocolo, "
        "domínio, caminho e recurso.",
        "<b>Aula 3:</b> o IP identifica a máquina, o DNS traduz o nome em IP, o domínio é o nome registrado "
        "e a hospedagem mantém o site no ar.",
        "<b>Aula 4:</b> portal concentra conteúdo, e-business é o negócio digital inteiro e e-commerce é a "
        "venda on-line (início → catálogo → carrinho → checkout).",
    ]:
        st.append(Paragraph("•&nbsp;&nbsp;" + t, S["li"]))
    st.append(Spacer(1, 6))
    st.append(make_box("conceito", "Internet · Web · cliente · servidor · navegador · HTTP/HTTPS · URL · "
                       "IP · DNS · domínio · hospedagem · portal · e-business · e-commerce.",
                       title="TERMOS PARA DEIXAR NO QUADRO"))

    # ---- perguntas orais ----
    st += big_section("Para fixar conversando", "5 perguntas orais para fechar a semana")
    for i, q in enumerate([
        "Qual é a diferença entre Internet e Web?",
        "Quando você abre um site, quem é o cliente e quem é o servidor?",
        "O que significa o cadeado que aparece na barra de endereços?",
        "Quem “traduz” o nome do site (domínio) para o número do servidor (IP)?",
        "Uma loja que vende pela Internet é exemplo de qual conceito? E o fluxo dela, você lembra?",
    ], 1):
        st.append(Paragraph(f"<b>{i}.</b>&nbsp;&nbsp;{q}", S["li_num"]))
    st.append(Spacer(1, 4))
    st.append(make_box("dica", "Respostas esperadas: 1) Internet é a rede, Web é um serviço dela; 2) navegador "
                       "= cliente, máquina do site = servidor; 3) conexão HTTPS criptografada; 4) o DNS; "
                       "5) e-commerce — início, catálogo, ficha, carrinho e checkout.",
                       title="GABARITO RÁPIDO DO PROFESSOR"))
    return st


if __name__ == "__main__":
    build_doc(os.path.join(_ROOT, "output",
                           "Texto_Apoio_Aulas_1_a_4_Fundamentos_da_Internet_e_Web.pdf"),
              story, label="TEXTO DE APOIO · AULAS 1 A 4 · PARTE I",
              header="PROGRAMAÇÃO PARA INTERNET I — TEXTO DE APOIO",
              centro="Material de apoio da disciplina · Turma 2/2026")
