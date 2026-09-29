# 🛍️ Projeto Loja Tech da Turma — GUIA DA PROFESSORA

Projeto-modelo **integrado** das disciplinas **Programação para Internet I** e
**Linguagem de Programação II** (Turma 2/2026). Os alunos estudam este modelo e
depois criam **a própria loja** com a mesma estrutura.

## 📄 Páginas do site (todas .php — o Apache executa o PHP)
| Página | O que faz |
|---|---|
| `index.php` | Home com fundo texturizado, banner e vitrine de produtos CLICÁVEIS (vindos do banco) |
| `produtos.php` | Catálogo com filtro por categoria (?cat=) + tabela de estoque; cards levam ao detalhe |
| `produto.php?id=N` | Detalhe do item: foto grande, descrição, preço, estoque e botão de pagamento |
| `pagamentos.php?id=N` | Resumo do pedido + quantidade + Pix/Cartão/Boleto (simulados, com ícones) |
| `processar_pedido.php` | Valida, grava a VENDA e BAIXA o estoque (INSERT + UPDATE) |
| `contato.php` | Contato + Localização NA MESMA PÁGINA (formulário + mapa + horários) |
| `cadastro.php` | Cadastro de clientes com validação |

> ⚠️ Não existem mais páginas .html: arquivo .html não executa PHP no XAMPP
> (esse era o bug do “site sem fundo/imagem” quando aberto errado).

## 📱 Para testar no CELULAR (mesmo Wi-Fi da escola)
1. No PC: `Win+R` → `cmd` → digite `ipconfig` → anote o **IPv4** (ex.: 192.168.0.15);
2. No celular (mesmo Wi-Fi): abra `http://192.168.0.15/loja/index.php` (troque pelo seu IP);
3. O layout se ajusta sozinho à tela (site responsivo).

## 🗂️ O que tem dentro
```
projeto-loja/
├── site/                      ← PI-I: site em HTML + CSS + PHP (XAMPP)
│   ├── index.php              home com vitrine vinda DO BANCO
│   ├── produtos.php           catálogo + filtro por categoria (?cat=...) + tabela de estoque
│   ├── cadastro.html          formulário de clientes (label/name/types/required)
│   ├── processar_cadastro.php validação + sanitização + INSERT
│   ├── contato.html           formulário de contato (POST)
│   ├── processar_contato.php  validação + INSERT + protocolo
│   ├── includes/              conexao.php · cabecalho.php · rodape.php
│   ├── css/estilo.css         identidade azul+âmbar, comentada
│   └── imagens/               logo, banner, 4 produtos, sem-foto (flat)
├── banco/
│   ├── loja_turma.sql         CREATE DATABASE + 4 tabelas + seed + VIEW + consultas-treino
│   └── backup_restore.md      mysqldump/restauração + desastre didático 😈
── vb6/                       ← LP2: gerencial em VB6 no MESMO banco
│   ├── mdlConexao.bas         conexão ADO/ODBC + CRUD
│   ├── mdlRelatorios.bas      relatório Printer + exportar/importar .txt
│   ├── frmGerencial_codigo.txt código do form + lista de controles
│   └── LEIA-ME_VB6.md         roteiro de aula + erros comuns da turma
└── README.md                  ← você está aqui
```

## 🚀 Como subir o modelo no laboratório (10 min)
1. Copie a pasta `site/` para `C:\xampp\htdocs\loja\`;
2. phpMyAdmin (`http://localhost/phpmyadmin`) → **Importar** → `banco/loja_turma.sql` → Executar;
3. Abra `http://localhost/loja/index.php` → vitrine com 4 destaques = **banco vivo**;
4. (LP2) Siga `vb6/LEIA-ME_VB6.md` para o gerencial.

## 🎯 Como aplicar como aula prática (sugestão S)
| Etapa | Aula | Atividade do aluno |
|---|---|---|
| 1 | PI-I (formulários) | Estudar `cadastro.html` + `processar_cadastro.php` e recriar com 3 campos novos |
| 2 | PI-I (PHP+MySQL) | Criar uma página nova que liste UMA tabela do banco (ex.: mensagens) |
| 3 | LP2 (SQL) | Rodar as consultas-treino do `.sql` e criar 2 novas (WHERE/GROUP BY) |
| 4 | LP2 (VB6) | Montar o frmGerencial e fazer o botão Adicionar funcionar |
| 5 | Integradora | **Projeto final do aluno: “Minha Loja”** — mesmo esqueleto, tema livre, com: 4 páginas, 1 tabela nova no banco, 1 relatório/impressão ou exportação, backup executado |

## ✅ Checklist de avaliação do projeto do aluno (S — 10 pts)
- [ ] Site abre sem erro e menu funciona (2,0)
- [ ] Formulários com label/name/validação/sanitização (2,0)
- [ ] Pelo menos 1 consulta SQL exibindo dados do banco (2,0)
- [ ] Tabela criada pelo aluno com seed próprio (1,5)
- [ ] Gerencial/relatório OU exportação de arquivo funcionando (1,5)
- [ ] Backup executado e comprovado (1,0)

## 🔌 Stack (o que o aluno precisa ter)
VS Code + XAMPP + navegador · (LP2: + ODBC + VB6 da escola).
Veja o **Checklist_Downloads.pdf** entregável aos alunos.
