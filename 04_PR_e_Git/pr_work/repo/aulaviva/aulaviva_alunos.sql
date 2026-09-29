-- Tabela de progresso do AulaViva (MySQL do redserver) — execute 1x
CREATE TABLE IF NOT EXISTS aulaviva_alunos (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  disc VARCHAR(8) NOT NULL,
  code CHAR(16) NOT NULL,
  nome VARCHAR(80) DEFAULT '',
  turma VARCHAR(40) DEFAULT '',
  payload JSON,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_disc_code (disc, code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
