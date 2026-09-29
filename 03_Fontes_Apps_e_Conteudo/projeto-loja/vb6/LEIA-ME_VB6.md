# 🧾 Gerencial VB6 da Loja — LEIA-ME do professor

## O que é
Um **sistema de gerenciamento de estoque** em Visual Basic 6.0 que conversa com o
**mesmo banco MySQL** (`loja_turma`) usado pelo site em PHP. É a ponte viva entre as
duas disciplinas:

- **PI-I** cuida do site (HTML + PHP + formulários);
- **LP2** cuida do banco (SGBD/SQL), do gerencial VB6 (estruturas, Strings, arquivos,
  relatórios/Printer) e do backup/restauração.

## Arquivos desta pasta
| Arquivo | Papel | Semanas da LP2 |
|---|---|---|
| `mdlConexao.bas` | Conexão ADO/ODBC + CRUD (INSERT/UPDATE/DELETE/SELECT) | 3, 5, 6, 15, 16 |
| `mdlRelatorios.bas` | Relatório via Printer + exportar/importar arquivos .txt | 13, 14, 19, 20 |
| `frmGerencial_codigo.txt` | Código do formulário + lista de controles para montar no IDE | 7–12 (estruturas/Strings) |

## Pré-requisitos na máquina
1. **VB6** (licença/CD da escola — a Microsoft não distribui mais);
2. **MySQL Connector/ODBC** instalado (driver “MySQL ODBC 8.0 ANSI Driver”);
3. No VB6: **Projeto > Referências > Microsoft ActiveX Data Objects 2.8 Library**;
4. Banco importado: `banco/loja_turma.sql` no phpMyAdmin;
5. Pasta `C:\lp2\export\` criada (para o botão Exportar).

## Roteiro de aula sugerido (S)
1. **Semana 15**: montar o form (controles da lista) + importar `mdlConexao.bas` → botão Atualizar lista funcionando (uau!);
2. **Semana 16**: Adicionar produto com validação + teste de estoque baixo no site (integração visível!);
3. **Semanas 19–20**: botão Relatório (impressora ou “Microsoft Print to PDF”) + Exportar .txt;
4. **Semana 17–18**: backup/restauração com `banco/backup_restore.md` (inclua o desastre didático 😈).

## Erros comuns da turma (e o que dizer)
| Sintoma no VB6 | Causa | Frase salvadora |
|---|---|---|
| “Data source name not found” | Driver ODBC ausente/nome errado | “Confira no painel ODBC o nome EXATO do driver” |
| Erro de referência ao compilar | Falta marcar ADO 2.8 | “Projeto > Referências é o crachá da biblioteca” |
| Lista vazia mas sem erro | Banco sem dados / SELECT errado | “Rode o SELECT no phpMyAdmin primeiro” |
| Relatório não imprime | Falta `Printer.EndDoc` | “Sem EndDoc o job dorme na fila” |
| Arquivo .txt não grava | Falta `Close #n` | “Close é o lacre do caminhão de dados” |
