-- =====================================================================
--  AulaViva · Banco v2 (redserver) — contas com senha, progresso,
--  materiais e entregas dos alunos
--  Rodar:  mysql -u root -p < aulaviva_v2.sql
--  Depois: criar usuário e ajustar senhas em api.php
-- =====================================================================

CREATE DATABASE IF NOT EXISTS loja_aulaviva
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE loja_aulaviva;

-- Contas de alunos (nome único por disciplina)
CREATE TABLE IF NOT EXISTS aulaviva_contas (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(12) NOT NULL,
  nome        VARCHAR(80) NOT NULL,
  nome_lc     VARCHAR(80) NOT NULL,
  turma       VARCHAR(30) DEFAULT '',
  senha_hash  VARCHAR(255) NOT NULL,
  adm         TINYINT(1) DEFAULT 0,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY un_disc_code (disc, code),
  UNIQUE KEY un_disc_nome (disc, nome_lc)
) ENGINE=InnoDB;

-- Progresso/payload (pts, cartas, hist de respostas etc.)
CREATE TABLE IF NOT EXISTS aulaviva_progresso (
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(12) NOT NULL,
  nome        VARCHAR(80) DEFAULT '',
  turma       VARCHAR(30) DEFAULT '',
  payload     MEDIUMTEXT,
  updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (disc, code)
) ENGINE=InnoDB;

-- Materiais enviados pela professora
CREATE TABLE IF NOT EXISTS aulaviva_arquivos (
  disc        ENUM('pi1','lp2') NOT NULL,
  nome        VARCHAR(200) NOT NULL,
  tipo        VARCHAR(80) DEFAULT '',
  tamanho     INT DEFAULT 0,
  updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (disc, nome)
) ENGINE=InnoDB;

-- Entregas de atividades dos alunos (txt/doc/pdf)
CREATE TABLE IF NOT EXISTS aulaviva_entregas (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  disc        ENUM('pi1','lp2') NOT NULL,
  code        CHAR(12) NOT NULL,
  aluno       VARCHAR(100) DEFAULT '',
  arquivo     VARCHAR(255) NOT NULL,
  nome        VARCHAR(200) NOT NULL,
  tamanho     INT DEFAULT 0,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  KEY ix_disc_code (disc, code)
) ENGINE=InnoDB;

-- Usuário da aplicação (troque a senha!)
CREATE USER IF NOT EXISTS 'loja_app'@'localhost'
  IDENTIFIED BY 'TROQUE_ESTA_SENHA_2026';
GRANT SELECT, INSERT, UPDATE, DELETE ON loja_aulaviva.* TO 'loja_app'@'localhost';
FLUSH PRIVILEGES;

-- Migração de dados antigos (se a tabela aulaviva_alunos existir do v1):
-- INSERT IGNORE INTO aulaviva_progresso (disc, code, nome, turma, payload, updated_at)
--   SELECT disc, code, nome, turma, payload, updated_at FROM loja_aulaviva.aulaviva_alunos;
