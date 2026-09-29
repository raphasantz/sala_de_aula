# Deploy no redserver (regra de ouro do handover)

Fonte de verdade: **/root/_drop/kit_sala/** → scp → **/mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/**
Confira `md5sum` local × remoto antes de dar por pronto. Teste SEMPRE pela URL do ngrok.

## Arquivos desta pasta de manutenção
| Origem (aqui) | Destino no servidor |
|---|---|
| aulaviva/api.php | Kit_Sala_de_Aula/aulaviva/api.php |
| aulaviva/aulaviva_alunos.sql | executar 1× no MySQL (sudo mysql loja_turma) |
| apps-nuvem/AulaViva_PI-I_index.html | Kit_Sala_de_Aula/apps-nuvem/… |
| apps-nuvem/AulaViva_LP2_index.html | idem |
| apps-nuvem/Painel_Professor_PI-I.html | idem |
| apps-nuvem/Painel_Professor_LP2.html | idem |

## Comandos modelo
    scp aulaviva/api.php rednerd@100.84.203.66:/tmp/
    ssh rednerd@100.84.203.66 'sudo cp /tmp/api.php /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php && sudo chown www-data:www-data /mnt/hdd/dev-replica/htdocs/Kit_Sala_de_Aula/aulaviva/api.php'
    md5sum aulaviva/api.php   # e compare com o remoto

## Antes do primeiro uso
1. Rode `aulaviva_alunos.sql` no MySQL (tabela aulaviva_alunos);
2. Crie `aulaviva/materiais/pi1/` e `aulaviva/materiais/lp2/` (chown www-data);
3. Defina no php-fpm (pool do vhost pcs-replica):
   `env[LOJA_DB_PASS] = <senha do loja_app>` e `env[AULAVIVA_PROF_TOKEN] = <token novo>`;
4. **ROTACIONE** a senha antiga e o token antigo (o doc de handover circulou com eles em claro).

## Regras que eu (manutenção) respeito
- Nada de localStorage nos apps (shim de memória injetado);
- Erros de banco → error_log, mensagem genérica pro browser;
- Pedido de loja: transação + SELECT … FOR UPDATE (não reverter);
- Não tocar em outros vhosts (8081/8082, mesanerd, calistenia, siad…);
- Resíduos de teste (linhas qa_*) sempre apagados após QA.
