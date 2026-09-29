# -*- coding: utf-8 -*-
"""Pacote de conteúdo — Programação para Internet I (Turma 2/2026)."""

from . import comuns, avaliacoes
from . import quizzes_aulas as quizzes
from .m01_02 import MODULOS as M1_2
from .m03_05 import MODULOS as M3_5
from .m06_09 import MODULOS as M6_9
from .m10_12 import MODULOS as M10_12

MODULOS = M1_2 + M3_5 + M6_9 + M10_12
MODULOS_POR_NUM = {m["num"]: m for m in MODULOS}

# ---------------------------------------------------------------------------
# GLOSSÁRIO
# ---------------------------------------------------------------------------
GLOSSARIO = [
    ("Array", "Estrutura que guarda vários valores em uma única variável, acessados por índice (numérico) ou por chave (associativo)."),
    ("Atributo", "Configuração extra de uma tag HTML, escrita na tag de abertura: nome=\"valor\" (ex.: href, src, alt)."),
    ("Boolean", "Tipo de dados com apenas dois valores: true (verdadeiro) ou false (falso)."),
    ("Checkbox", "Campo de formulário de múltipla escolha (marca/desmarca opções independentes)."),
    ("Cliente", "Papel de quem solicita recursos na Web — tipicamente o navegador do usuário."),
    ("colspan", "Atributo de célula de tabela que a faz ocupar N colunas."),
    ("Concatenação", "Junção de textos. Em PHP usa-se o ponto: \"Olá, \" . $nome."),
    ("Constante", "Valor que não muda durante o programa; em PHP: define(\"NOME\", valor)."),
    ("CSS", "Folhas de estilo — definem a aparência (cores, fontes, espaçamento) das páginas HTML."),
    ("DNS", "Sistema que traduz nomes de domínio em endereços IP (a “agenda” da Internet)."),
    ("Domínio", "Nome registrado que identifica um site na Web (ex.: meusite.com.br)."),
    ("DOCTYPE", "Declaração <!DOCTYPE html> que indica ao navegador o uso de HTML5."),
    ("echo", "Comando PHP que envia conteúdo (texto/HTML) para a resposta da página."),
    ("e-Commerce", "Comércio eletrônico — compra e venda on-line (loja virtual)."),
    ("e-Business", "Negócio conduzido de forma digital (conceito amplo, inclui o e-commerce)."),
    ("Elemento HTML", "Conjunto: tag de abertura + conteúdo + tag de fechamento (ex.: <p>texto</p>)."),
    ("float", "Tipo numérico com casas decimais em PHP (ex.: 1.65)."),
    ("foreach", "Laço PHP que percorre todos os elementos de um array (as $item ou as $chave => $valor)."),
    ("Formulário", "Conjunto de campos (form + inputs) para o usuário enviar dados ao servidor."),
    ("FTP", "Protocolo de transferência de arquivos, usado para publicar sites na hospedagem."),
    ("Função", "Bloco de código nomeado, com parâmetros de entrada e valor de retorno (return)."),
    ("GET", "Método de envio de formulário cujos dados viajam visíveis na URL; lido via $_GET."),
    ("Hospedagem", "Serviço que armazena os arquivos do site em um servidor ligado 24 h."),
    ("htmlspecialchars()", "Função PHP que converte caracteres especiais em entidades — sanitização contra XSS."),
    ("HTTP / HTTPS", "Protocolo de comunicação da Web / sua versão criptografada (segura)."),
    ("include / require", "Comandos PHP que inserem o conteúdo de outro arquivo (reutilização: cabeçalho, rodapé, funções)."),
    ("integer", "Tipo numérico inteiro em PHP (ex.: 17)."),
    ("IP (endereço)", "Número que identifica um dispositivo em uma rede (ex.: 142.250.78.14)."),
    ("isset() / empty()", "Funções PHP de validação: o dado foi enviado? / o dado está vazio?"),
    ("Laço (loop)", "Estrutura de repetição: for, while, do...while, foreach."),
    ("Label", "Rótulo de campo de formulário; associado ao campo pelo par for/id."),
    ("localhost", "Endereço do próprio computador — usado para testar o servidor local (http://localhost)."),
    ("Markup (marcação)", "Sistema de anotação de texto que define a estrutura do conteúdo (HTML)."),
    ("Método (HTTP)", "Modo de envio dos dados do formulário: GET ou POST."),
    ("Parâmetro", "Valor de entrada de uma função; na chamada, é o argumento."),
    ("Portal", "Site que concentra conteúdo e serviços (institucional, educacional, de notícias)."),
    ("POST", "Método de envio cujos dados viajam no corpo da requisição (invisíveis na URL); lido via $_POST."),
    ("Radio (botão)", "Campo de escolha única dentro de um grupo (mesmo name)."),
    ("Requisição / Resposta", "Pedido enviado pelo navegador ao servidor / conteúdo devolvido pelo servidor."),
    ("return", "Palavra-chave que devolve o resultado de uma função e a encerra."),
    ("Sanitização", "Tratamento dos dados do usuário para exibição/armazenamento seguros (ex.: htmlspecialchars)."),
    ("Semântica (HTML)", "Uso de tags que transmitem significado (strong, em, nav), não apenas aparência."),
    ("Servidor Web", "Software (ex.: Apache) que atende requisições e entrega páginas; roda na hospedagem."),
    ("string", "Tipo de dados de texto em PHP (entre aspas)."),
    ("switch", "Estrutura de decisão que compara uma variável com valores fixos (case/break/default)."),
    ("Tag", "Marcador HTML entre sinais de menor/maior: de abertura (&lt;p&gt;), fechamento (&lt;/p&gt;) ou vazia (&lt;br&gt;)."),
    ("URL", "Endereço completo de um recurso na Web (protocolo + domínio + caminho + recurso + parâmetros)."),
    ("var_dump()", "Função PHP que exibe tipo e valor de uma variável — essencial para depuração."),
    ("Variável", "Espaço nomeado na memória que guarda um valor; em PHP começa com $."),
    ("XAMPP", "Pacote gratuito com servidor Apache + PHP + MySQL para desenvolvimento local."),
    ("XSS", "Ataque de injeção de script em páginas Web — prevenido com sanitização da saída."),
]
