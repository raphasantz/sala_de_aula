# 💾 Backup e Recuperação do banco `loja_turma` (LP2 · semanas 17–18)

> Abra o **Prompt de Comando** do Windows e vá até a pasta do XAMPP:
> `cd C:\xampp\mysql\bin`

## 1) Backup (cópia de segurança)
```bat
mysqldump -u root loja_turma > C:\lp2\backups\loja_turma_%date:~-4%%date:~3,2%%date:~0,2%.sql
```
Versão simples (sem data no nome), ótima para aula:
```bat
mysqldump -u root loja_turma > C:\lp2\backups\loja_turma_aula.sql
```
Só a estrutura (sem dados):
```bat
mysqldump -u root --no-data loja_turma > C:\lp2\backups\estrutura.sql
```

## 2) Recuperação (restaurar)
Em um banco de TESTE primeiro (regra de ouro!):
```bat
mysql -u root -e "CREATE DATABASE loja_turma_teste;"
mysql -u root loja_turma_teste < C:\lp2\backups\loja_turma_aula.sql
```
Validação pós-restauro:
```bat
mysql -u root loja_turma_teste -e "SHOW TABLES; SELECT COUNT(*) AS produtos FROM produtos;"
```
Confira: 4 tabelas e 8 produtos. Bateu? Então pode restaurar em produção:
```bat
mysql -u root loja_turma < C:\lp2\backups\loja_turma_aula.sql
```

## 3) Rotina sugerida para o laboratório (S)
- Backup ao **fim de cada aula prática** que alterar dados;
- Guardar as **4 últimas gerações** (avô-pai-filho);
- Pasta de backups **fora** da pasta do XAMPP (ex.: `C:\lp2\backups` ou Drive da escola);
- Teste de recuperação **uma vez por mês** (cópia não testada = esperança 🙏).

## 4) Desastre didático recomendado 😈
1. `DELETE FROM produtos;` sem WHERE (sim, dói);
2. Site quebrado/vitrine vazia (dramatize!);
3. Recupere com o backup da aula anterior;
4. Aplausos. 🎉 (É assim que a turma nunca mais esquece backup.)
