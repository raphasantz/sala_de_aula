# -*- coding: utf-8 -*-
"""Pacote de conteúdo — Linguagem de Programação II (Turma 2/2026)."""

from . import comuns, avaliacoes, quizzes
from .m01_04 import MODULOS as M_A
from .m05_10 import MODULOS as M_B
from .m11_15 import MODULOS as M_C

MODULOS = M_A + M_B + M_C

# Semana 1 = uma única entrada interativa (o app usa a semana como chave dos quizzes):
_m1 = MODULOS[0]
if len(_m1["aulas"]) == 2:
    _a, _b = _m1["aulas"]
    _a["titulo"] = "Ambientação, linguagem estruturada e primeiro programa VB6"
    _a["blocos"] = _a["blocos"] + _b["blocos"]
    _a["slides"]["pontos"] = _a["slides"]["pontos"] + _b["slides"].get("pontos", [])
    _m1["aulas"] = [_a]

MODULOS_POR_NUM = {m["num"]: m for m in MODULOS}

GLOSSARIO = [
    ("ADO", "Biblioteca de acesso a dados do VB6 (Connection, Recordset) usada para falar com o SGBD."),
    ("Append (For Append)", "Modo de abertura de arquivo que acrescenta linhas sem apagar o conteúdo."),
    ("AUTO_INCREMENT", "Recurso que numera automaticamente a chave primária a cada INSERT."),
    ("Backup", "Cópia de segurança da estrutura e dos dados do banco (ex.: mysqldump)."),
    ("ByRef", "Passagem de parâmetro por referência: a Sub altera a variável original do chamador."),
    ("ByVal", "Passagem de parâmetro por valor: o parâmetro recebe uma cópia (original protegido)."),
    ("Cliente/Servidor", "Modelo em que a aplicação (cliente) requisita e o SGBD (servidor) processa e responde."),
    ("Close #n", "Comando que fecha um arquivo aberto, descarregando o buffer de gravação."),
    ("cn.Execute", "Método do ADODB.Connection que envia um comando SQL ao servidor."),
    ("Connection string", "Texto com driver, servidor, banco e credenciais usado para abrir a conexão."),
    ("COUNT/SUM/AVG/MAX/MIN", "Funções de agregação do SQL que resumem conjuntos de linhas."),
    ("CREATE TABLE", "Comando DDL que define uma tabela (colunas, tipos, chave primária)."),
    ("DDL", "Família de comandos SQL de definição de estrutura (CREATE, ALTER, DROP)."),
    ("DML", "Família de comandos SQL de manipulação de dados (INSERT, UPDATE, DELETE, SELECT)."),
    ("Do While / Do Until", "Laços do VB6: repete enquanto verdadeiro / até virar verdadeiro."),
    ("Documento fiscal", "Saída padronizada de venda (cupom/NF); no curso, modelo didático com Printer."),
    ("DSN/ODBC", "Ponte de drivers entre a aplicação e o SGBD; DSN é o nome da conexão configurada."),
    ("EOF(n)", "Função que indica fim de arquivo durante a leitura (condição de parada do laço)."),
    ("Err.Description", "Mensagem técnica do último erro em tempo de execução (tratamento com On Error)."),
    ("For Output / For Input", "Modos de abertura de arquivo: gravação (substitui) / somente leitura."),
    ("Format()", "Função que formata números e datas para saída legível (ex.: \"0.00\", \"dd/mm/yyyy\")."),
    ("FreeFile", "Função que devolve um número de arquivo livre para Open."),
    ("Function", "Rotina que retorna valor; o retorno é atribuído ao próprio nome."),
    ("GROUP BY", "Cláusula SQL que agrupa linhas para agregações por grupo."),
    ("InStr", "Função que devolve a posição de um trecho no texto (0 = não encontrou)."),
    ("LIKE", "Operador SQL de comparação com padrões e curingas (% e _)."),
    ("Line Input #n", "Leitura de uma linha inteira de arquivo texto."),
    ("Mid$ / Left$ / Right$", "Funções de recorte de texto por posição (contagem a partir de 1)."),
    ("Module (.bas)", "Arquivo de código com rotinas Public/Private reutilizáveis no projeto."),
    ("mysqldump", "Utilitário que gera backup do banco em script .sql."),
    ("On Error GoTo", "Estrutura de tratamento de erros em tempo de execução do VB6."),
    ("ORDER BY", "Cláusula SQL de ordenação do resultado (ASC/DESC)."),
    ("Package & Deployment Wizard", "Ferramenta do VB6 que gera o pacote/disco de instalação."),
    ("PictureBox", "Controle VB6 usado para recursos gráficos (Line, Circle, PSet)."),
    ("Printer", "Objeto VB6 que monta e envia saída à impressora (Print, Tab, EndDoc)."),
    ("PRIMARY KEY", "Coluna que identifica cada linha de forma única e não nula."),
    ("Recordset", "Objeto ADO com o resultado de uma consulta; percorrido com EOF/MoveNext/rs!campo."),
    ("Registro (Type)", "Tipo estruturado que agrupa campos de tipos diferentes (ficha)."),
    ("Restore (recuperação)", "Restauração de um backup: mysql banco < arquivo.sql."),
    ("Select Case", "Estrutura de seleção para comparar um valor com casos fixos (menus)."),
    ("Sentinela", "Valor combinado que encerra uma leitura (ex.: -1)."),
    ("SGBD", "Sistema Gerenciador de Banco de Dados (MySQL, PostgreSQL, SQL Server, Access)."),
    ("Split()", "Função que quebra uma string em um vetor de partes por separador."),
    ("SQL", "Linguagem padrão de definição e manipulação de dados em bancos relacionais."),
    ("String * n", "Campo de texto de tamanho fixo em um Type (herança de arquivos de registro)."),
    ("Sub", "Rotina que executa ações sem retornar valor."),
    ("Trim$ / UCase$ / LCase$", "Funções de normalização de texto (pontas, caixa alta/baixa)."),
    ("Vetor / Matriz", "Arrays uni e bidimensionais: muitas posições sob um nome, acessadas por índice."),
    ("WHERE", "Cláusula SQL que filtra linhas por condição."),
]
