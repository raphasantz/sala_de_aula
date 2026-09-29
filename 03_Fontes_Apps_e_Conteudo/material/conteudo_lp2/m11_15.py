# -*- coding: utf-8 -*-
"""LP2 — Módulos 11 a 15 (Partes V e VI): Cliente/Servidor, backup/recuperação,
relatórios/documentos fiscais, disco de instalação/gráficos e projeto integrador.
Semanas 15 a 24."""

M11 = {
    "num": 11, "titulo": "Manipulação de dados Cliente/Servidor (ADO)",
    "parte_num": 5, "parte_titulo": "Dados Cliente/Servidor e Administração do Banco",
    "aulas_faixa": "Aulas 57 a 64", "semanas": "Semanas 15 a 16",
    "objetivos": [
        "Explicar o fluxo Cliente/Servidor: aplicação → SQL → SGBD → resultados.",
        "Percorrer resultados com Recordset (EOF, MoveNext, campos por nome).",
        "Executar CRUD completo (CREATE/INSERT/SELECT/UPDATE/DELETE) pelo VB6.",
        "Validar entradas e tratar problemas de conexão/SQL em tempo de execução.",
    ],
    "aulas": [
        {"num": 15, "titulo": "Cliente/Servidor: o fluxo completo com ADO", "blocos": [
            ("h", "O fluxo que rege tudo"),
            ("p", "A aplicação VB6 (cliente) monta o SQL, envia pela conexão; o MySQL (servidor) executa, "
                  "e devolve: ou um <b>Recordset</b> (consulta) ou um <b>número de linhas afetadas</b> "
                  "(manipulação). Entender esse vai-e-vem é entender sistemas reais."),
            ("codigo", {"titulo": "Recordset: percorrendo o resultado", "ling": "vb", "linhas": [
                "Dim rs As ADODB.Recordset",
                "Set rs = cn.Execute(\"SELECT nome, nota FROM alunos \" & _",
                "                      \"WHERE nota >= 7 ORDER BY nome\")",
                "",
                "Do While Not rs.EOF",
                "    List1.AddItem rs!nome & \" - \" & rs!nota",
                "    rs.MoveNext",
                "Loop",
                "rs.Close",
                "Set rs = Nothing",
            ]}),
            ("conceito", ("O trio sagrado do Recordset",
                          "<b>rs.EOF</b>: chegou ao fim? · <b>rs.MoveNext</b>: avance uma linha · "
                          "<b>rs!campo</b>: leia o valor da coluna. Sem MoveNext, laço infinito; sem Close, "
                          "recurso preso no servidor.")),
            ("h", "CRUD completo pelo programa"),
            ("codigo", {"titulo": "Modulo CrudAlunos.bas", "ling": "vb", "linhas": [
                "Public Sub Inserir(nome As String, nota As Single)",
                "    cn.Execute \"INSERT INTO alunos (nome, nota) VALUES ('\" & _",
                "                 nome & \"', \" & Format(nota, \"0.0\") & \")\"",
                "End Sub",
                "",
                "Public Sub Atualizar(id As Integer, nota As Single)",
                "    cn.Execute \"UPDATE alunos SET nota = \" & Format(nota, \"0.0\") & _",
                "                 \" WHERE id = \" & id",
                "End Sub",
                "",
                "Public Sub Excluir(id As Integer)",
                "    cn.Execute \"DELETE FROM alunos WHERE id = \" & id",
                "End Sub",
                "",
                "Public Function Existe(id As Integer) As Boolean",
                "    Dim rs As ADODB.Recordset",
                "    Set rs = cn.Execute(\"SELECT id FROM alunos WHERE id = \" & id)",
                "    Existe = Not rs.EOF",
                "    rs.Close",
                "End Function",
            ]}),
            ("h", "Validação e tratamento de problemas"),
            ("lista", [
                "Validar ANTES de mandar SQL: Len/Trim/Val/IsNumeric no cliente;",
                "Aspas simples em textos: escapar ' duplicando ('') para não quebrar o comando;",
                "On Error GoTo em toda operação de banco; Err.Number 2000+ = erro de banco/conexão;",
                "Confirmar exclusões com MsgBox vbYesNo antes do DELETE;",
                "Mostrar ao usuário mensagem amiga + detalhe técnico no log (Debug.Print).",
            ]),
            ("atencao", "Injeção de SQL: se o texto digitado entra direto no comando, um usuário mal-"
                        "intencionado ‘fecha as aspas’ e injeta comandos. Por isso validamos, escapamos e, "
                        "em sistemas reais, usamos parâmetros preparados. Consciência desde já."),
        ], "slides": {"pontos": [
            "Cliente monta SQL → servidor executa → Recordset ou linhas afetadas",
            "Trio do Recordset: EOF · MoveNext · rs!campo",
            "CRUD em módulo próprio (Inserir/Atualizar/Excluir/Existe)",
            "Validar no cliente + On Error + Escapar aspas = defesa em camadas",
        ], "codigo": {"titulo": "Percurso padrão", "linhas": [
            "Do While Not rs.EOF",
            "    List1.AddItem rs!nome & \" - \" & rs!nota",
            "    rs.MoveNext",
            "Loop",
            "rs.Close",
        ]}, "nota": "Semana 16 termina com a A2 (prova). Aula 64: revisão ativa com o modelo de prova da "
                   "apostila em duplas + correção comentada."}},
        {"num": 16, "titulo": "Cliente/Servidor — prática e validação em grupo", "blocos": [
            ("h", "Oficina de CRUD com tela"),
            ("lista_num", [
                "Formulário frmAlunos: Text nome, Text nota, botões Incluir/Alterar/Excluir/Listar;",
                "Listar preenche ListBox via Recordset (nome + nota + id entre colchetes);",
                "Incluir valida (nome >= 5 caracteres, nota 0–10) antes do INSERT;",
                "Alterar/Excluir pedem o id e confirmam com MsgBox vbYesNo;",
                "Toda operação termina atualizando a ListBox (refresh).",
            ]),
            ("h", "Testes de robustez (atividade em grupo)"),
            ("tabela", {"titulo": "Plano de testes da oficina",
                        "cab": ["Teste", "Entrada", "Esperado"],
                        "lin": [["Nome vazio", "(vazio)", "MsgBox de validação, nada vai ao banco"],
                                ["Nota fora de faixa", "nota = 15", "MsgBox, nada vai ao banco"],
                                ["Aspas no nome", "O'Connor", "INSERT funciona (aspas escapadas)"],
                                ["Excluir inexistente", "id = 999", "Aviso ‘não encontrado’ (Existe=False)"],
                                ["Serviço parado", "MySQL off", "MsgBox amiga de falha de conexão"]]}),
            ("dica", "Teste em dupla trocada: uma dupla ataca o programa da outra com o plano de testes. "
                     "Quem acha bug, assina o relatório — caçar bug também é conteúdo."),
        ], "slides": {"pontos": [
            "frmAlunos: CRUD completo com refresh da ListBox",
            "Validação no cliente antes de todo comando SQL",
            "Confirmação vbYesNo em Alterar/Excluir",
            "Plano de testes de 5 casos, executado em dupla trocada",
        ], "nota": "Aula de laboratório cheia: circule com o plano de testes impresso; registre os bugs mais "
                   "criativos para a correção coletiva."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "CRUD de produtos", "tipo": "pratico",
         "enunciado": "Replique a oficina para a tabela produtos(id, nome, preco, estoque): formulário "
                      "completo com as 4 operações e validações (preco > 0, estoque >= 0).",
         "esperado": "CRUD funcional com validações e refresh; aspas escapadas em nomes.",
         "orientacao": "Conferir Escape de aspas (Replace(nome, \"'\", \"''\")) e confirmações."},
        {"num": 2, "titulo": "Consulta com filtro dinâmico", "tipo": "pratico",
         "enunciado": "Text de busca + botão: SELECT ... WHERE nome LIKE '%texto%' ORDER BY nome; preencha a "
                      "ListBox; mostre contagem de resultados com rs.RecordCount ou contador próprio.",
         "esperado": "Busca parcial funcionando com LIKE montado por concatenação segura e contagem exibida.",
         "orientacao": "Discuta: por que RecordCount pode vir -1 em alguns cursores? (contagem manual é "
                       "portável)."},
        {"num": 3, "titulo": "Relatório de falhas", "tipo": "escrito",
         "enunciado": "Do teste em dupla trocada: liste os 3 bugs mais sérios encontrados no programa "
                      "avaliado, com: sintoma, causa provável e correção proposta.",
         "esperado": "Relatório claro ligando sintoma → causa → correção (ex.: falta de validação, falta de "
                     "MoveNext, aspas não escapadas).",
         "orientacao": "Correção coletiva no projetor com os 3 melhores relatórios; vira material de revisão "
                       "da A2."},
    ],
    "teste_rapido": [
        {"enunciado": "Sem rs.MoveNext dentro do Do While Not rs.EOF, o programa:",
         "alt": ["pula a primeira linha", "entra em laço infinito", "fecha o Recordset", "dá erro de sintaxe"],
         "resposta": 1, "comentario": "O ponteiro não avança: EOF nunca chega."},
        {"enunciado": "rs!nota lê:",
         "alt": ["o nome da coluna", "o valor do campo nota da linha atual", "a primeira linha inteira",
                 "o total de linhas"],
         "resposta": 1, "comentario": "Acesso ao campo da linha corrente do Recordset."},
        {"enunciado": "Para escapar uma aspa simples dentro de um texto que vai virar SQL:",
         "alt": ["duplica a aspa ('')", "remove a aspa", "troca por aspas duplas", "usa \\ ' "],
         "resposta": 0, "comentario": "Em SQL, '' representa uma aspa literal dentro do texto."},
        {"enunciado": "cn.Execute de um UPDATE devolve:",
         "alt": ["um Recordset com as linhas alteradas", "nada de tabela; afeta linhas no banco",
                 "um arquivo temporário", "um MsgBox automático"],
         "resposta": 1, "comentario": "Manipulação não retorna Recordset; consulta retorna."},
        {"enunciado": "Validar no cliente antes de enviar SQL serve para:",
         "alt": ["deixar o banco mais rápido", "evitar comandos inválidos/perigosos e mensagens ruins",
                 "substituir o On Error", "economizar memória"],
         "resposta": 1, "comentario": "Defesa em camadas: cliente valida, servidor protege, erro tratado."},
    ],
    "avaliacao_ref": "A2",
}

M12 = {
    "num": 12, "titulo": "Backup e recuperação de banco de dados",
    "parte_num": 5, "parte_titulo": "Dados Cliente/Servidor e Administração do Banco",
    "aulas_faixa": "Aulas 65 a 72", "semanas": "Semanas 17 a 18",
    "objetivos": [
        "Explicar a finalidade de backup e os cuidados de organização das cópias.",
        "Executar backup do MySQL com mysqldump e restaurar com mysql <.",
        "Validar a recuperação restaurando em banco de teste e conferindo dados.",
        "Planejar rotina de cópias (frequência, nomeação, guarda) para um cenário real.",
    ],
    "aulas": [
        {"num": 17, "titulo": "Backup: a cópia que salva o semestre", "blocos": [
            ("h", "Por que backup (e por que agora)"),
            ("p", "Dados são o ativo mais valioso de um sistema: discos falham, alguém executa DELETE sem "
                  "WHERE, um UPDATE errado reescreve notas. <b>Backup</b> é a cópia que permite voltar no "
                  "tempo; <b>recuperação</b> é o treino que garante que a cópia funciona."),
            ("codigo", {"titulo": "Backup com mysqldump (prompt de comando)", "ling": "shell", "linhas": [
                "REM copia estrutura + dados do banco escola:",
                "mysqldump -u root -paluno123 escola > c:\\lp2\\backups\\escola_2026-09-18.sql",
                "",
                "REM só a estrutura (sem dados):",
                "mysqldump -u root -paluno123 --no-data escola > estrutura.sql",
            ]}),
            ("h", "Organização das cópias"),
            ("lista", [
                "Nome com data: banco_YYYY-MM-DD.sql (ordena sozinho na pasta);",
                "Pasta própria fora do servidor (c:\\lp2\\backups\\ ou Drive/nuvem da escola);",
                "Rotina mínima de laboratório: backup ao fim de cada semana de uso do banco;",
                "Testar a recuperação PELO MENOS uma vez por mês (cópia não testada = esperança).",
            ]),
            ("conceito", ("Backup bom é backup restaurado",
                          "Um .sql nunca visto pode estar truncado, com senha errada ou banco errado dentro. "
                          "A validação é prática: restaurar em um banco de teste e conferir contagens "
                          "(SELECT COUNT(*) antes × depois).")),
        ], "slides": {"pontos": [
            "Backup = voltar no tempo; recuperação = provar que a máquina do tempo funciona",
            "mysqldump -u root -p banco > arquivo.sql",
            "Nome com data + pasta fora do servidor + rotina semanal",
            "Cópia não testada = esperança, não backup",
        ], "codigo": {"titulo": "Backup", "linhas": [
            "mysqldump -u root -paluno123 escola > escola_2026-09-18.sql",
        ]}, "nota": "Provoque o desastre didático: DELETE sem WHERE na tabela de testes e recupere ao vivo "
                   "com o backup da aula anterior."}},
        {"num": 18, "titulo": "Recuperação e validação pós-restauro", "blocos": [
            ("codigo", {"titulo": "Restaurar (prompt de comando)", "ling": "shell", "linhas": [
                "REM restaura sobre o banco escola (recria tabelas e dados do .sql):",
                "mysql -u root -paluno123 escola < c:\\lp2\\backups\\escola_2026-09-18.sql",
                "",
                "REM restauração segura em banco de TESTE:",
                "mysql -u root -paluno123 -e \"CREATE DATABASE escola_teste;\"",
                "mysql -u root -paluno123 escola_teste < escola_2026-09-18.sql",
            ]}),
            ("h", "Validação após recuperação"),
            ("lista_num", [
                "Conferir tabelas: SHOW TABLES; no banco restaurado;",
                "Conferir contagens: SELECT COUNT(*) de cada tabela (antes × depois);",
                "Conferir amostras: 3 linhas conhecidas batem campo a campo;",
                "Registrar: data/hora do restauro, arquivo usado, responsável, resultado;",
                "Só então apontar a aplicação para o banco recuperado.",
            ]),
            ("h", "Cenários de desastre (estudo de caso)"),
            ("tabela", {"titulo": "Qual cópia usar?",
                        "cab": ["Cenário", "Ação"],
                        "lin": [["DELETE sem WHERE apagou tudo às 10h", "Restaurar backup de ontem + reaplicar inserções de hoje (se houver log)"],
                                ["Disco do servidor morreu", "Restaurar último backup em servidor novo e reconfigurar conexão"],
                                ["UPDATE errado mudou 200 notas", "Restaurar em banco de teste, extrair só a coluna correta e corrigir"],
                                ["Backup de sexta corrompido", "Usar o de quinta (por isso guardamos várias gerações!)"]]}),
            ("dica", "Gerações de backup (avô-pai-filho): manter pelo menos as 4 últimas cópias semanais "
                     "resolve 90% dos cenários acima sem drama."),
        ], "slides": {"pontos": [
            "mysql -u root -p banco < arquivo.sql = restaurar",
            "Restaurar em banco de TESTE antes de produção",
            "Validar: SHOW TABLES + COUNT(*) + amostras",
            "Gerações (4 últimas semanas) cobrem os cenários reais",
        ], "codigo": {"titulo": "Recuperação", "linhas": [
            "mysql -u root -paluno123 escola_teste < escola_2026-09-18.sql",
        ]}, "nota": "Laboratório: cada dupla destrói e recupera seu banco de teste — o medo vira procedimento."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Rotina completa de backup", "tipo": "pratico",
         "enunciado": "Gere backup do banco escola com nome datado; apague uma tabela de testes (DROP); "
                      "restaure do .sql; valide com SHOW TABLES e COUNT(*).",
         "esperado": "Ciclo completo executado com validação registrada no caderno.",
         "orientacao": "Conferir o nome datado do arquivo e a conferência de contagens pós-restauro."},
        {"num": 2, "titulo": "Recuperação cirúrgica", "tipo": "pratico",
         "enunciado": "Simule UPDATE errado em 5 notas; restaure o backup em escola_teste; escreva o SQL que "
                      "copia de volta apenas as notas corretas do banco de teste para o produção "
                      "(UPDATE com JOIN ou subselect, demonstrado no quadro).",
         "esperado": "Notas corrigidas por recuperação seletiva, sem derrubar o resto dos dados.",
         "orientacao": "Demonstre a versão com subselect UPDATE ... SET nota = (SELECT ... WHERE id = ...) "
                       "e discuta quando ela é segura."},
        {"num": 3, "titulo": "Plano de backup da escola", "tipo": "escrito",
         "enunciado": "Proponha por escrito a rotina de backup do laboratório: frequência, nomeação, local "
                      "de guarda, gerações mantidas, responsável e procedimento de recuperação testada.",
         "esperado": "Plano coerente (semanal + antes de provas; 4 gerações; Drive + pasta local; teste "
                     "mensal) com justificativas.",
         "orientacao": "Os 3 melhores planos viram o procedimento oficial do laboratório (com crédito aos "
                       "autores)."},
    ],
    "teste_rapido": [
        {"enunciado": "mysqldump banco > arquivo.sql produz:",
         "alt": ["um banco novo", "um arquivo com estrutura + dados em SQL", "um backup binário criptografado",
                 "um relatório em PDF"],
         "resposta": 1, "comentario": "Texto SQL reproduzível em qualquer servidor MySQL."},
        {"enunciado": "Para restaurar o conteúdo do arquivo no banco:",
         "alt": ["mysqldump < arquivo", "mysql banco < arquivo.sql", "RESTORE FILE arquivo", "cn.Execute(arquivo)"],
         "resposta": 1, "comentario": "O cliente mysql executa o script .sql dentro do banco indicado."},
        {"enunciado": "Validar uma recuperação inclui:",
         "alt": ["só olhar o tamanho do arquivo", "SHOW TABLES + contagens + amostras conferidas",
                 "reiniciar o servidor", "abrir o .sql no Bloco de Notas"],
         "resposta": 1, "comentario": "Conferência estrutural e de conteúdo após o restauro."},
        {"enunciado": "Manter várias gerações de backup (avô-pai-filho) protege contra:",
         "alt": ["falta de espaço", "cópias corrompidas ou desastres descobertos tardiamente",
                 "senhas fracas", "vírus de tela"],
         "resposta": 1, "comentario": "Se a cópia de ontem está ruim, a de quinta-feira salva."},
        {"enunciado": "Restaurar primeiro em banco de TESTE serve para:",
         "alt": ["treinar SQL", "não arriscar o banco de produção durante a validação",
                 "acelerar o mysqldump", "economizar disco"],
         "resposta": 1, "comentario": "Valida o arquivo e o procedimento sem tocar em dados reais."},
    ],
    "avaliacao_ref": None,
}

M13 = {
    "num": 13, "titulo": "Relatórios, impressão e documentos fiscais",
    "parte_num": 6, "parte_titulo": "Saídas, Distribuição, Gráficos e Projeto Integrador",
    "aulas_faixa": "Aulas 73 a 80", "semanas": "Semanas 19 a 20",
    "objetivos": [
        "Gerar relatórios com seleção e organização de dados (tela e papel).",
        "Usar o objeto Printer (Print, Tab, String, EndDoc) para saídas impressas.",
        "Montar documentos fiscais simples (cupom/nota) com layout controlado.",
        "Aplicar Format e alinhamentos para saída profissional.",
    ],
    "aulas": [
        {"num": 19, "titulo": "Relatórios: dados que viram informação", "blocos": [
            ("h", "Anatomia de um relatório"),
            ("lista", [
                "<b>Cabeçalho</b>: título, empresa, data/hora de emissão, página;",
                "<b>Colunas</b>: nomes alinhados sobre os dados;",
                "<b>Corpo</b>: linhas selecionadas e ordenadas (SQL faz o pesado);",
                "<b>Rodapé de grupo/geral</b>: contagens, somas, médias;",
                "<b>Separadores</b>: linhas String(80, \"-\") entre blocos.",
            ]),
            ("codigo", {"titulo": "Relatório de aprovados na tela (montado por Sub)", "ling": "vb", "linhas": [
                "Public Sub RelatorioAprovados()",
                "    Dim rs As ADODB.Recordset",
                "    Print Tab(20); \"RELATÓRIO DE APROVADOS - \" & Format(Date, \"dd/mm/yyyy\")",
                "    Print String(60, \"-\")",
                "    Print \"NOME\"; Tab(35); \"NOTA\"",
                "    Print String(60, \"-\")",
                "    Set rs = cn.Execute(\"SELECT nome, nota FROM alunos \" & _",
                "                          \"WHERE nota >= 7 ORDER BY nome\")",
                "    Do While Not rs.EOF",
                "        Print rs!nome; Tab(35); Format(rs!nota, \"0.0\")",
                "        rs.MoveNext",
                "    Loop",
                "    rs.Close",
                "    Print String(60, \"-\")",
                "End Sub",
            ]}),
            ("h", "Do tela para o papel: objeto Printer"),
            ("codigo", {"titulo": "Impressão com Printer", "ling": "vb", "linhas": [
                "Public Sub ImprimirRelatorio()",
                "    Printer.Print Tab(20); \"RELATÓRIO DE APROVADOS\"",
                "    Printer.Print String(60, \"-\")",
                "    ' ...mesmas linhas do corpo, trocando Print por Printer.Print...",
                "    Printer.Print String(60, \"-\")",
                "    Printer.Print \"Emitido em \" & Now",
                "    Printer.EndDoc          ' envia o trabalho à impressora'",
                "End Sub",
            ]}),
            ("conceito", ("Printer = a impressora como objeto",
                          "Tudo que você Printa no Printer entra na fila de impressão; <b>EndDoc</b> fecha o "
                          "documento e despacha. Sem EndDoc, o trabalho fica preso. Tab() e String() cuidam "
                          "do alinhamento em colunas de caracteres.")),
        ], "slides": {"pontos": [
            "Relatório = cabeçalho + colunas + corpo (SQL) + rodapé + separadores",
            "Tab(n) alinha colunas; String(n, \"-\") separa blocos",
            "Printer.Print monta a página; EndDoc despacha à impressora",
            "Format nos números e datas = aparência profissional",
        ], "codigo": {"titulo": "Impressão", "linhas": [
            "Printer.Print Tab(20); \"RELATÓRIO\"",
            "Printer.Print String(60, \"-\")",
            "Printer.EndDoc",
        ]}, "nota": "Se o laboratório não tiver impressora, gere ‘PDF’ com impressora virtual (Microsoft "
                   "Print to PDF) — mesmo código, saída em arquivo."}},
        {"num": 20, "titulo": "Documentos fiscais: cupom e nota simplificados", "blocos": [
            ("h", "Layout de cupom (monoespaçado)"),
            ("codigo", {"titulo": "Cupom de venda não fiscal (modelo didático)", "ling": "vb", "linhas": [
                "Public Sub Cupom(venda As Integer)",
                "    Printer.Print Tab(12); \"MERCADO ESCOLA LTDA\"",
                "    Printer.Print Tab(8); \"CNPJ 00.000.000/0001-00\"",
                "    Printer.Print String(48, \"-\")",
                "    Printer.Print \"CUPOM NÃO FISCAL - Venda \"; venda",
                "    Printer.Print String(48, \"-\")",
                "    ' itens: codigo, descricao, qtd, unit, total",
                "    Printer.Print \"001 ARROZ 5KG      2 x  22,90   45,80\"",
                "    Printer.Print String(48, \"-\")",
                "    Printer.Print Tab(30); \"TOTAL R$   45,80\"",
                "    Printer.Print \"Obrigado pela preferência!\"",
                "    Printer.EndDoc",
                "End Sub",
            ]}),
            ("h", "O que um documento fiscal de verdade exige (contexto)"),
            ("lista", [
                "Identificação do emitente (razão social, CNPJ, endereço);",
                "Numeração sequencial e data/hora de emissão;",
                "Itens com quantidade, unitário e total conferindo (soma validada);",
                "Totais e forma de pagamento;",
                "Em sistemas reais: autorização da SEFAZ (NF-e/NFC-e) — aqui, o MODELO didático.",
            ]),
            ("dica", "Monte os itens do cupom vindo do banco (tabela itens_venda) com Recordset: o cupom "
                     "deixa de ser texto fixo e vira saída de dados — exatamente como no projeto final."),
            ("atencao", "Alinhamento em impressora real muda com fonte proporcional: fixe fonte monoespaçada "
                        "(Printer.FontName = \"Courier New\") para as colunas fecharem."),
        ], "slides": {"pontos": [
            "Cupom didático: emitente + numeração + itens + totais + agradecimento",
            "Itens vêm do banco via Recordset (não texto fixo)",
            "Fonte monoespaçada (Courier New) para colunas fecharem",
            "Contexto real: NF-e/NFC-e com autorização SEFAZ (visão geral)",
        ], "codigo": {"titulo": "Fonte fixa", "linhas": [
            "Printer.FontName = \"Courier New\"",
            "Printer.Print String(48, \"-\")",
        ]}, "nota": "Mostre um cupom real de mercado ao lado do modelo didático: a turma identifica cada "
                   "bloco."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Relatório de estoque", "tipo": "pratico",
         "enunciado": "Relatório (tela + Printer) dos produtos com estoque < mínimo: cabeçalho com data, "
                      "colunas codigo/descricao/estoque, rodapé com contagem e valor total imobilizado.",
         "esperado": "Saída alinhada com Tab/String e totais corretos; impressão (ou PDF) conferida.",
         "orientacao": "Conferir o SQL com WHERE e o acumulador do valor imobilizado."},
        {"num": 2, "titulo": "Cupom dinâmico", "tipo": "pratico",
         "enunciado": "Cupom que lê a venda pelo id: cabeçalho do emitente (tabela loja), itens da tabela "
                      "itens_venda via Recordset, totais calculados (qtd × unit) e EndDoc.",
         "esperado": "Cupom impresso/PDF com itens reais do banco e total batendo com a soma manual.",
         "orientacao": "Validação cruzada: soma manual dos itens × total impresso."},
        {"num": 3, "titulo": "Leitura de documento fiscal", "tipo": "escrito",
         "enunciado": "Traga (ou receba) um cupom/NF-e real e identifique por escrito: emitente, numeração, "
                      "data, itens com unit/qtd/total, totais e pagamento; marque o que nosso modelo didático "
                      "já reproduz e o que ficaria por conta da SEFAZ.",
         "esperado": "Identificação completa dos blocos e separação clara didático × fiscal real.",
         "orientacao": "Discussão de 10 min: por que a autorização fiscal existe (contexto profissional)."},
    ],
    "teste_rapido": [
        {"enunciado": "Para alinhar colunas em relatórios de texto usamos:",
         "alt": ["Space( ) apenas", "Tab(n) e String(n, \"-\")", "MsgBox", "Printer.Page"],
         "resposta": 1, "comentario": "Tab posiciona colunas; String desenha separadores."},
        {"enunciado": "Sem Printer.EndDoc, o trabalho de impressão:",
         "alt": ["sai imediatamente", "fica retido/no buffer sem despachar", "é cancelado", "imprime em dobro"],
         "resposta": 1, "comentario": "EndDoc fecha o documento e envia à fila."},
        {"enunciado": "Para colunas fecharem em impressora real, a fonte deve ser:",
         "alt": ["proporcional (Arial)", "monoespaçada (Courier New)", "itálica", "decorativa"],
         "resposta": 1, "comentario": "Largura fixa por caractere = colunas alinhadas."},
        {"enunciado": "Os itens de um cupom ‘de verdade’ no nosso sistema vêm:",
         "alt": ["digitados fixos no código", "do banco, via Recordset", "de um arquivo .bmp", "do Clipboard"],
         "resposta": 1, "comentario": "Saída de dados: SQL + Recordset alimentam o layout."},
        {"enunciado": "Um relatório gerencial típico termina com:",
         "alt": ["somente os detalhes", "totais/contagens/médias de fechamento", "o código SQL",
                 "a string de conexão"],
         "resposta": 1, "comentario": "Rodapé de fechamento dá a leitura gerencial do conjunto."},
    ],
    "avaliacao_ref": None,
}

M14 = {
    "num": 14, "titulo": "Disco de instalação e recursos gráficos",
    "parte_num": 6, "parte_titulo": "Saídas, Distribuição, Gráficos e Projeto Integrador",
    "aulas_faixa": "Aulas 81 a 88", "semanas": "Semanas 21 a 22",
    "objetivos": [
        "Preparar e organizar os arquivos necessários à distribuição do programa.",
        "Gerar o pacote/disco de instalação com o Package & Deployment Wizard.",
        "Aplicar recursos gráficos no VB6 (PictureBox: Line, Circle, PSet) com herança do modo DOS.",
        "Testar a instalação em máquina/conta limpa.",
    ],
    "aulas": [
        {"num": 21, "titulo": "Disco de instalação: do projeto ao pacote", "blocos": [
            ("h", "O que vai dentro de um instalador"),
            ("lista", [
                "Executável compilado (.exe) do projeto;",
                "Bibliotecas de tempo de execução (runtime VB6, MSADO/ODBC);",
                "Arquivos de dados/modelos (textos, logs, templates de relatório);",
                "Configurações (string de conexão parametrizável!);",
                "Atalhos e desinstalador.",
            ]),
            ("h", "Package & Deployment Wizard passo a passo"),
            ("lista_num", [
                "No VB6: Add-Ins → Package & Deployment Wizard;",
                "Compile o projeto primeiro (File → Make projeto.exe);",
                "Escolha o projeto e a opção <b>Package</b>;",
                "Selecione os arquivos dependentes sugeridos (marque os .bas de dados e templates);",
                "Defina o grupo de menu/atalhos e o destino padrão (C:\\MeuSistema);",
                "Gere a pasta/pacote (setup.exe + cab) e copie para a pasta de distribuição;",
                "Teste em conta/máquina limpa: instalar, executar, conectar ao banco, desinstalar.",
            ]),
            ("conceito", ("Configuração fora do executável",
                          "Senha/servidor nunca vão compilados no .exe: o instalador copia um "
                          "<b>config.txt/ini</b> que o programa lê ao abrir (conexão parametrizável). "
                          "Assim o mesmo pacote serve para laboratórios diferentes.")),
            ("atencao", "Teste de instalação que não passa em máquina limpa = pacote incompleto (falta "
                        "dependência). O erro clássico é esquecer o driver ODBC na lista de pré-requisitos "
                        "documentados."),
        ], "slides": {"pontos": [
            "Instalador = exe + runtimes + dados + config + atalhos + desinstalador",
            "Package & Deployment Wizard: Package → dependentes → atalhos → setup.exe",
            "Conexão parametrizável via config.ini (nunca senha compilada)",
            "Teste em máquina/conta limpa é obrigatório",
        ], "nota": "Se o laboratório não tiver o Wizard disponível, documente o roteiro alternativo: pasta "
                   "rede + atalhos + script de cópia (mesmo conceito de distribuição)."}},
        {"num": 22, "titulo": "Recursos gráficos: a herança do modo DOS", "blocos": [
            ("h", "Do DOS ao formulário"),
            ("p", "A ementa cita ‘programação gráfica em ambiente DOS’: nos PCs antigos, gráficos nasciam de "
                  "comandos de desenho em modo texto/gráfico (SCREEN, LINE, CIRCLE). No VB6, o mesmo espírito "
                  "vive no <b>PictureBox</b>: coordenadas, cores e métodos de desenho."),
            ("codigo", {"titulo": "Desenhando no PictureBox", "ling": "vb", "linhas": [
                "Picture1.ScaleMode = 3                 ' pixels",
                "Picture1.BackColor = vbWhite",
                "",
                "Picture1.Line (10, 10)-(200, 120), vbBlue, B     ' retângulo (B = box)",
                "Picture1.Circle (110, 65), 40, vbRed              ' círculo",
                "Picture1.Line (10, 130)-(200, 130), vbBlack       ' linha simples",
                "",
                "Dim x As Integer",
                "For x = 10 To 200 Step 5",
                "    Picture1.PSet (x, 140 + 10 * Sin(x / 10)), vbGreen  ' pontos (onda)",
                "Next x",
            ]}),
            ("h", "Gráficos com dados do sistema"),
            ("codigo", {"titulo": "Gráfico de barras das notas (dados do banco)", "ling": "vb", "linhas": [
                "Dim rs As ADODB.Recordset, x As Integer",
                "Set rs = cn.Execute(\"SELECT nome, nota FROM alunos ORDER BY nome\")",
                "x = 20",
                "Do While Not rs.EOF",
                "    Picture1.Line (x, 160)-(x + 18, 160 - rs!nota * 14), vbBlue, BF",
                "    Picture1.CurrentX = x: Picture1.CurrentY = 165",
                "    Picture1.Print Left$(rs!nome, 3)",
                "    x = x + 26",
                "    rs.MoveNext",
                "Loop",
                "rs.Close",
            ]}),
            ("dica", "Gráfico de barras com BF (box filled) + escala simples (nota × 14) transforma qualquer "
                     "consulta em painel visual — use no dashboard do projeto final."),
        ], "slides": {"pontos": [
            "Herança DOS: desenhar por comandos (LINE/CIRCLE) → PictureBox no VB6",
            "Line (x1,y1)-(x2,y2), cor, B/BF · Circle (x,y), raio · PSet ponto",
            "Gráfico de barras vindo do banco = dashboard do projeto",
        ], "codigo": {"titulo": "Barras do banco", "linhas": [
            "Picture1.Line (x, 160)-(x+18, 160 - rs!nota*14), vbBlue, BF",
        ]}, "nota": "Laboratório gráfico é o recreio dirigido: dê o desafio ‘desenhe a bandeira da escola’ "
                   "com Line/Circle após o exemplo das barras."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Pacote de instalação", "tipo": "pratico",
         "enunciado": "Compile um projeto seu (ex.: CRUD de produtos) e gere o pacote com o Wizard; teste em "
                      "conta limpa: instalar, rodar, conectar, desinstalar. Registre o passo a passo com "
                      "prints.",
         "esperado": "Pacote funcional com teste em ambiente limpo documentado.",
         "orientacao": "Conferir presença do config.ini parametrizável e do driver ODBC na documentação do "
                       "pacote."},
        {"num": 2, "titulo": "Bandeira e onda", "tipo": "pratico",
         "enunciado": "No PictureBox: desenhe a bandeira da escola (retângulos/círculos com B/BF) e uma onda "
                      "com PSet em laço; adicione botão Limpar (Picture1.Cls).",
         "esperado": "Duas composições gráficas com laços e botão de limpeza.",
         "orientacao": "Valorize o uso de laços (não 40 linhas de PSet à mão)."},
        {"num": 3, "titulo": "Dashboard de notas", "tipo": "pratico",
         "enunciado": "Gráfico de barras das notas por aluno (consulta SQL) com eixo, rótulos (Left$ do nome) "
                      "e legenda; inclua o dashboard como tela do seu projeto.",
         "esperado": "Barras proporcionais às notas com rótulos legíveis.",
         "orientacao": "Integração direta com o projeto integrador (semana 23): já deixe a tela pronta."},
    ],
    "teste_rapido": [
        {"enunciado": "O Package & Deployment Wizard gera:",
         "alt": ["o banco de dados", "o pacote/disco de instalação (setup + dependentes)",
                 "o relatório fiscal", "o backup do MySQL"],
         "resposta": 1, "comentario": "Empacota exe, runtimes, dados e atalhos para distribuição."},
        {"enunciado": "Senha/servidor de conexão devem ficar:",
         "alt": ["compilados no .exe", "em arquivo de configuração lido em tempo de execução",
                 "no título do formulário", "no Registry sem documentação"],
         "resposta": 1, "comentario": "Config.ini parametrizável: mesmo pacote em ambientes diferentes."},
        {"enunciado": "No PictureBox, o método que desenha um retângulo preenchido usa:",
         "alt": ["Box F", "BF no final do Line", "Fill automaticamente", "Rect()"],
         "resposta": 1, "comentario": "Line (x1,y1)-(x2,y2), cor, BF (B = borda, BF = preenchido)."},
        {"enunciado": "PSet serve para:",
         "alt": ["desenhar um ponto na coordenada", "imprimir texto", "limpar a tela", "mover o formulário"],
         "resposta": 0, "comentario": "Ponto único — ondas e texturas nascem de laços com PSet."},
        {"enunciado": "Testar a instalação em máquina/conta limpa serve para:",
         "alt": ["ganhar tempo", "garantir que o pacote leva todas as dependências",
                 "economizar licença", "validar o banco"],
         "resposta": 1, "comentario": "Ambiente limpo revela dependência esquecida no pacote."},
    ],
    "avaliacao_ref": None,
}

M15 = {
    "num": 15, "titulo": "Projeto integrador e consolidação final",
    "parte_num": 6, "parte_titulo": "Saídas, Distribuição, Gráficos e Projeto Integrador",
    "aulas_faixa": "Aulas 89 a 96", "semanas": "Semanas 23 a 24",
    "objetivos": [
        "Integrar banco + SQL + estruturas + modularização + arquivos + relatórios + gráficos no projeto.",
        "Aplicar revisão geral da ementa como preparação da prova final.",
        "Testar, revisar e apresentar o projeto com demonstração completa.",
        "Consolidar o portfólio do semestre: código, pacote de instalação e documentação.",
    ],
    "aulas": [
        {"num": 23, "titulo": "Integração do projeto (semana 23)", "blocos": [
            ("h", "O que o projeto precisa ter"),
            ("lista", [
                "<b>Banco</b>: tabelas criadas por script .sql versionado;",
                "<b>Conexão</b>: módulo Conexao.bas com tratamento de falhas;",
                "<b>CRUD</b>: cadastro e consulta via ADO com validação no cliente;",
                "<b>Estruturas</b>: vetor/matriz/registro onde fizer sentido (ex.: cache, cálculos);",
                "<b>Modularização</b>: regras em Modules (Functions puras);",
                "<b>Arquivos</b>: importação/exportação de dados (txt) com validação;",
                "<b>Relatório</b>: saída Printer/PDF com totais; <b>gráfico</b> PictureBox opcional;",
                "<b>Instalação</b>: pacote gerado + config.ini parametrizável.",
            ]),
            ("h", "Roteiro de acompanhamento por aula"),
            ("tabela", {"titulo": "Semana 23 — aulas 89 a 92",
                        "cab": ["Aula", "Foco", "Entrega"],
                        "lin": [["89", "Integração: banco + SQL + telas (CRUD completo)", "Entrega 2"],
                                ["90", "Arquivos + relatório acoplados ao fluxo", "—"],
                                ["91", "Modularização final + gráficos/dashboard", "—"],
                                ["92", "Testes internos com plano de testes da dupla", "Entrega 3"]]}),
            ("dica", "Congele escopo na semana 23: o que não entrou até a aula 92 vira ‘versão 2’ no "
                     "relatório, não dívida na apresentação."),
        ], "slides": {"pontos": [
            "Checklist de integração: banco, conexão, CRUD, estruturas, módulos, arquivos, relatório, pacote",
            "Semana 23: CRUD → arquivos/relatório → módulos/gráficos → testes",
            "Congelar escopo na aula 92 = apresentação tranquila",
        ], "nota": "Circule com o checklist impresso por dupla; marque pendências a lápis para a semana 24."}},
        {"num": 24, "titulo": "Consolidação, prova final e apresentações (semana 24)", "blocos": [
            ("h", "Revisão geral (aulas 93–94)"),
            ("lista", [
                "SGBD/conexão: string, On Error, abrir/fechar;",
                "SQL: CREATE/INSERT/UPDATE/DELETE/SELECT com WHERE/ORDER/GROUP;",
                "Estruturas: vetor, matriz, registro; Strings e funções;",
                "Modularização: Sub/Function, ByVal/ByRef, escopos;",
                "Arquivos: Output/Append/Input, EOF, FreeFile, Split;",
                "Cliente/Servidor: Recordset (EOF/MoveNext/rs!campo);",
                "Backup/recuperação: mysqldump/mysql <, validação;",
                "Relatórios/Printer e gráficos PictureBox; pacote de instalação.",
            ]),
            ("h", "Prova final escrita (30 pts) e apresentações (10 pts)"),
            ("lista_num", [
                "Aulas 93–94: revisão ativa com o modelo de prova da apostila (em duplas, correção comentada);",
                "Prova escrita individual e cumulativa conforme o Plano de Ensino;",
                "Aula 95: ensaio geral cronometrado (5–8 min) com demonstração: cadastro válido, tentativa "
                "inválida, consulta/relatório ao vivo;",
                "Aula 96: apresentações + entrega do pacote de instalação + encerramento.",
            ]),
            ("conceito", ("Demonstração que convence",
                          "Mostre o fluxo completo com dados reais: cadastre → erre de propósito (validação) "
                          "→ corrija → consulte → imprima relatório. Erro tratado ao vivo vale mais que demo "
                          "perfeita ensaiada demais.")),
        ], "slides": {"pontos": [
            "Revisão em 8 blocos = mapa da prova final",
            "Prova escrita individual (30) + projeto/apresentação (10)",
            "Ensaio cronometrado com demonstração de erro tratado",
            "Aula 96: apresentações + pacote de instalação + encerramento",
        ], "nota": "Sorteie a ordem das apresentações na aula 95; plateia faz 1 pergunta por dupla "
                   "(registra participação)."}},
    ],
    "exercicios": [
        {"num": 1, "titulo": "Checklist de integração", "tipo": "grupo",
         "enunciado": "Preencham o checklist de integração do projeto (8 itens da aula 89) com status "
                      "Feito/Parcial/Pendente e plano para os pendentes até a aula 92.",
         "esperado": "Checklist realista com plano de ação datado.",
         "orientacao": "Visto do professor em cada dupla; pendências viram acompanhamento da semana 24."},
        {"num": 2, "titulo": "Plano de testes do projeto", "tipo": "grupo",
         "enunciado": "Montem a tabela de testes com mínimo 8 casos: cadastro válido/inválido, consulta com "
                      "e sem resultado, exclusão confirmada/cancelada, importação com linha corrompida, "
                      "relatório com zero registros, conexão com serviço parado.",
         "esperado": "Tabela executada com resultados OK/FALHOU e correções aplicadas.",
         "orientacao": "Troca de testes entre duplas na aula 92 (olho novo acha bug novo)."},
        {"num": 3, "titulo": "Ensaio cronometrado", "tipo": "grupo",
         "enunciado": "Ensaio de 5–8 min com cronômetro: abertura (tema/tabela), demonstração completa "
                      "(válido, inválido, consulta, relatório), fechamento (o que ficou para a versão 2). "
                      "Gravem no celular como plano B.",
         "esperado": "Apresentação dentro do tempo com demonstração de erro tratado e vídeo de backup.",
         "orientacao": "Feedback sanduíche em 2 min por dupla: ponto forte, ajuste, ponto forte."},
    ],
    "teste_rapido": [
        {"enunciado": "O checklist de integração do projeto exige, entre outros:",
         "alt": ["somente telas bonitas", "banco + CRUD + módulos + arquivos + relatório + pacote",
                 "apenas o relatório", "somente backup"],
         "resposta": 1, "comentario": "Integração é o nome do jogo: todas as camadas do semestre."},
        {"enunciado": "Congelar escopo na semana 23 significa:",
         "alt": ["não testar mais", "não acrescentar funcionalidades novas; pendências viram ‘versão 2’",
                 "parar de programar", "adiar a apresentação"],
         "resposta": 1, "comentario": "Escopo fechado = entrega e apresentação confiáveis."},
        {"enunciado": "Na demonstração, mostrar uma entrada inválida sendo barrada prova:",
         "alt": ["que o programa tem bugs", "que a validação funciona", "que o banco está lento",
                 "que faltou teste"],
         "resposta": 1, "comentario": "Erro tratado ao vivo é demonstração de qualidade, não defeito."},
        {"enunciado": "A prova final (30 pts) é:",
         "alt": ["em duplas com consulta", "escrita, individual e cumulativa", "oral", "só do projeto"],
         "resposta": 1, "comentario": "Conforme o Plano de Ensino; os 10 pts restantes são do projeto."},
        {"enunciado": "O pacote de instalação entregue deve incluir:",
         "alt": ["somente o .exe", "exe + dependentes + config.ini parametrizável + atalhos",
                 "o banco com senhas compiladas", "os fontes sem compilar"],
         "resposta": 1, "comentario": "Distribuição profissional: instalável e configurável por ambiente."},
    ],
    "avaliacao_ref": "A3",
}

MODULOS = [M11, M12, M13, M14, M15]
