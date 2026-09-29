-- ============================================================
-- BANCO DA LOJA — loja_turma.sql
-- LP2: semanas 2-6 (SGBD, conexão, SQL) · usado pelo site (PI-I)
-- Como importar: phpMyAdmin → Importar → escolha este arquivo → Executar
-- (ou no terminal: mysql -u root < loja_turma.sql)
-- ============================================================

CREATE DATABASE IF NOT EXISTS loja_turma CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE loja_turma;

-- ---------- TABELA: PRODUTOS ----------
CREATE TABLE produtos (
    id        INT PRIMARY KEY AUTO_INCREMENT,
    nome      VARCHAR(60)  NOT NULL,
    categoria VARCHAR(20)  NOT NULL,
    preco     DECIMAL(8,2) NOT NULL,
    estoque   INT          NOT NULL DEFAULT 0,
    foto      VARCHAR(60)  DEFAULT 'imagens/sem-foto.png',
    descricao VARCHAR(220) NOT NULL DEFAULT '',
    destaque  TINYINT(1)   DEFAULT 0
);

-- ---------- TABELA: CLIENTES ----------
CREATE TABLE clientes (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    nome       VARCHAR(60) NOT NULL,
    email      VARCHAR(80) NOT NULL,
    telefone   VARCHAR(20),
    nascimento DATE,
    cidade     VARCHAR(40),
    origem     VARCHAR(20),
    cadastrado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------- TABELA: MENSAGENS (formulário de contato) ----------
CREATE TABLE mensagens (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    nome        VARCHAR(60)  NOT NULL,
    email       VARCHAR(80)  NOT NULL,
    assunto     VARCHAR(20),
    mensagem    TEXT         NOT NULL,
    novidades   TINYINT(1)   DEFAULT 0,
    enviada_em  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ---------- TABELA: VENDAS (para relatórios da LP2) ----------
CREATE TABLE vendas (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT NOT NULL,
    qtd        INT NOT NULL DEFAULT 1,
    total      DECIMAL(8,2) NOT NULL,
    vendida_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

-- ---------- DADOS INICIAIS (seed) ----------
INSERT INTO produtos (nome, categoria, preco, estoque, foto, destaque, descricao) VALUES
('Mouse Gamer AzulTech',   'perifericos',  89.90,  12, 'imagens/prod-mouse.png',   1,
 'Mouse ergonômico com 6 botões, LED azul e sensor de 7200 DPI. Ideal para jogos e para o CAD da aula de desenho.'),
('Teclado Mecânico Turbo', 'perifericos', 249.00,   4, 'imagens/prod-teclado.png', 1,
 'Teclado mecânico switch blue com teclas âmbar de atalho. Clique alto, orgulho maior.'),
('Headset Som de Turma',   'audio',        179.50,   8, 'imagens/prod-headset.png', 1,
 'Headset com microfone destacável e almofadas macias para maratona de estudos (ou de rank).'),
('Webcam FullHD Aula',     'perifericos', 199.90,   3, 'imagens/prod-webcam.png',  1,
 'Webcam 1080p com anel de luz e clipe universal — perfeita para apresentar o projeto final.'),
('Mousepad Gigante XL',    'perifericos',  59.90,  25, 'imagens/sem-foto.png',     0,
 'Mousepad 80x40 cm com borda costurada: cabe o teclado, o mouse e o sonho.'),
('Hub USB 4 portas',       'acessorios',   45.00,  18, 'imagens/sem-foto.png',     0,
 'Hub USB 3.0 com 4 portas e LED de atividade. Chega de brigar por tomada de dados.'),
('SSD 480GB Rápido',       'componentes', 219.00,   6, 'imagens/sem-foto.png',     0,
 'SSD SATA 480GB: o upgrade que faz o PC da vovó virar nave de desenvolvimento.'),
('Memória 8GB DDR4',       'componentes', 149.90,   9, 'imagens/sem-foto.png',     0,
 'Pente de memória 8GB DDR4 3200MHz para o Chrome parar de chorar com 40 abas.');

INSERT INTO clientes (nome, email, telefone, nascimento, cidade, origem) VALUES
('Maria Professora', 'maria@escola.edu.br', '(32) 98888-0001', '1985-03-12', 'Muriaé', 'escola'),
('Aluno Testador',   'aluno@escola.edu.br', '(32) 97777-0002', '2008-07-30', 'Ubá',    'amigos');

INSERT INTO mensagens (nome, email, assunto, mensagem, novidades) VALUES
('Cliente Curioso', 'curioso@exemplo.com', 'orcamento', 'Quero um orçamento de 10 headsets!', 1);

INSERT INTO vendas (produto_id, qtd, total) VALUES
(1, 2, 179.80),
(3, 1, 179.50),
(2, 1, 249.00);

-- ---------- VIEW (LP2 semana 6): estoque baixo ----------
CREATE VIEW vw_estoque_baixo AS
SELECT id, nome, categoria, estoque
FROM produtos
WHERE estoque <= 5
ORDER BY estoque;

-- ---------- CONSULTAS-TREINO (LP2): rode uma por uma no phpMyAdmin ----------
-- SELECT * FROM produtos ORDER BY preco DESC;
-- SELECT nome, preco FROM produtos WHERE categoria = 'perifericos';
-- SELECT categoria, COUNT(*) AS qtd, AVG(preco) AS media FROM produtos GROUP BY categoria;
-- SELECT p.nome, v.qtd, v.total FROM vendas v JOIN produtos p ON p.id = v.produto_id;
-- UPDATE produtos SET estoque = estoque - 1 WHERE id = 1;
-- SELECT * FROM vw_estoque_baixo;
