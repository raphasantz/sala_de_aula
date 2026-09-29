-- =====================================================================
--  AulaViva · Migração do banco (redserver) — contas com senha,
--  progresso, materiais e entregas dos alunos.
--  Banco: loja_turma (o MESMO do v1 e do site da loja — o usuário
--  `loja_app` já tem acesso; nada novo para criar).
--  Rodar:  mysql -u root -p loja_turma < aulaviva_v2.sql
--  Idempotente: tudo com IF NOT EXISTS (pode rodar de novo sem medo).
-- =====================================================================

USE loja_turma;

-- Contas de alunos (nome único por disciplina; senha em hash bcrypt)
CREATE TABLE IF NOT EXISTS aulaviva_contas (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(16) NOT NULL,           -- 16 p/ compatibilidade com o v1
  nome        VARCHAR(80) NOT NULL,
  nome_lc     VARCHAR(80) NOT NULL,        -- nome normalizado (unicidade)
  turma       VARCHAR(30) DEFAULT '',
  senha_hash  VARCHAR(255) NOT NULL,
  adm         TINYINT(1) DEFAULT 0,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY un_disc_code (disc, code),
  UNIQUE KEY un_disc_nome (disc, nome_lc)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Progresso/payload (pts, cartas, hist de respostas etc.)
CREATE TABLE IF NOT EXISTS aulaviva_progresso (
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(16) NOT NULL,
  nome        VARCHAR(80) DEFAULT '',
  turma       VARCHAR(30) DEFAULT '',
  payload     MEDIUMTEXT,
  updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (disc, code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Materiais enviados pela professora
CREATE TABLE IF NOT EXISTS aulaviva_arquivos (
  disc        ENUM('pi1','lp2') NOT NULL,
  nome        VARCHAR(200) NOT NULL,
  tipo        VARCHAR(80) DEFAULT '',
  tamanho     INT DEFAULT 0,
  updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (disc, nome)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Entregas de atividades dos alunos (txt/doc/docx/pdf/odt)
CREATE TABLE IF NOT EXISTS aulaviva_entregas (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(16) NOT NULL,
  aluno       VARCHAR(100) DEFAULT '',
  arquivo     VARCHAR(255) NOT NULL,       -- caminho no servidor (entregas/<disc>/<code>/…)
  nome        VARCHAR(200) NOT NULL,       -- nome original do arquivo
  tamanho     INT DEFAULT 0,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  KEY ix_disc_code (disc, code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Se por acaso o `loja_app` não tiver acesso (não deve ser o caso — o v1 já
-- usava loja_turma), descomente e rode como root:
-- GRANT SELECT, INSERT, UPDATE, DELETE ON loja_turma.aulaviva_contas    TO 'loja_app'@'localhost';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON loja_turma.aulaviva_progresso TO 'loja_app'@'localhost';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON loja_turma.aulaviva_arquivos  TO 'loja_app'@'localhost';
-- GRANT SELECT, INSERT, UPDATE, DELETE ON loja_turma.aulaviva_entregas  TO 'loja_app'@'localhost';
-- FLUSH PRIVILEGES;

-- ---------------------------------------------------------------------
-- Migração OPCIONAL dos dados do v1 (tabela aulaviva_alunos, mesmo banco).
-- Atenção: o progresso antigo fica amarrado ao `code` velho do v1; quando o
-- aluno cria a conta nova (reg), ele gera um code novo e começa do zero.
-- Só descomente se quiser PRESERVAR o histórico antigo no banco (consulta):
--
-- INSERT IGNORE INTO aulaviva_progresso (disc, code, nome, turma, payload, updated_at)
--   SELECT disc, code, nome, turma, payload, updated_at
--   FROM aulaviva_alunos
--   WHERE disc IN ('pi1','lp2');
-- ---------------------------------------------------------------------
