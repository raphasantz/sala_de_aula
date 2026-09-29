#  Túnel público sem tela de aviso (Cloudflared) — LEIA-ME

## 💛 Para a Juh (não precisa saber NADA de Cloudflare)

Boa notícia: **você não precisa abrir o site da Cloudflare, nem mexer em painel nenhum.**
Ter conta na Cloudflare é opcional — para o link funcionar, **não se usa a conta em nada**.

Quem faz o trabalho é um programinha chamado **cloudflared**, que já fica no servidor.
Ele abre uma "porta mágica" entre o servidor da escola e a Internet, e devolve um link.
Só isso. Não tem configuração, não tem senha, não tem painel.

**O combinado, em 3 frases:**
1. O Rapha (ou quem cuida do servidor) roda **um comando só** (está logo abaixo).
2. O comando **imprime o link na tela** e também salva em `/root/url-tunel.txt`.
3. Você copia o link, cola no grupo da turma e testa no celular (fora do wi-fi da escola).
   Clicou? Cai **direto na tela de nome + senha do aluno** — sem nenhuma tela de aviso
   no meio (era isso que o ngrok fazia e o cloudflared não faz).

**Depois de um reboot do servidor:** o link pode mudar de nome (é assim no plano grátis,
igual acontecia com o ngrok). Rode de novo o comando do passo 1 (ou o comando de
"pegar o link atual", abaixo) e cole o link novo no grupo. O final do link
(`/KiT_Sala_de_Aula/`) é sempre o mesmo.

**E a minha conta da Cloudflare, então, serve para quê?** Para um dia, se você quiser,
criar um **link fixo** (que nunca muda), usando um domínio seu. Isso é opcional, está
explicado no final deste documento, e ninguém precisa fazer agora.

---

## O problema que isso resolve
No **ngrok grátis**, todo clique de aluno passava por uma tela de aviso do próprio
ngrok ("You are about to visit… / Visit Site") antes de chegar no Kit. Além disso,
pré-visualizações de link (WhatsApp etc.) mostravam a propaganda do ngrok em vez da
nossa sala. O **cloudflared quick tunnel** (gratuito, sem conta) não tem nenhuma
tela intermediária: **clicou, caiu no login (nome + senha) do AulaViva**.

## Subida rápida (túnel avulso — 1 comando)
```bash
sudo bash redserver/tunel/sobe-tunel.sh          # porta 8080 (vhost pcs-replica)
```
O script imprime o link e salva em `/root/url-tunel.txt`:
- PI-I: `https://xxxx.trycloudflare.com/KiT_Sala_de_Aula/`
- LP2:  `https://xxxx.trycloudflare.com/KiT_Sala_de_Aula/?d=lp2`

## Subida permanente (recomendado — sobrevive a reboot)
```bash
sudo cp redserver/tunel/tunel-cloudflared.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now tunel-cloudflared
# pegar o link atual:
journalctl -u tunel-cloudflared --no-pager | grep -oE 'https://[a-zA-Z0-9-]+\.trycloudflare\.com' | head -1
```

## Desligando o ngrok (depois de confirmar o cloudflared no ar)
```bash
sudo systemctl stop ngrok    # ou pkill -f 'ngrok start', conforme como ele roda hoje
```
Só pare o ngrok **depois** de testar o link novo no celular (fora do wi-fi da escola).

## ⚠️ O link muda quando o túnel reinicia
Quick tunnel = link sorteado a cada subida (igual ao ngrok mutável que já usamos).
Rotina sugerida: após reboot, rodar o comando do `journalctl` acima e colar o link
novo no grupo da turma. A porta de entrada `/KiT_Sala_de_Aula/` continua a mesma.

## 🔒 Link FIXO (opcional, quando a Juh quiser — é aqui que a conta Cloudflare entra)
Com conta gratuita na Cloudflare + um domínio seu (mesmo um barato), dá para criar
um túnel com nome (ex.: `aula.seudominio.com.br`) que **nunca muda**:
1. No servidor: `cloudflared tunnel login` → abre uma página para autorizar o domínio
   (é aqui, e só aqui, que você usa a sua conta da Cloudflare).
2. `cloudflared tunnel create aula` e `cloudflared tunnel route dns aula aula.seudominio.com.br`.
3. Apontar o service para o túnel nomeado (arquivo de configuração em
   `/etc/cloudflared/config.yml`, documentado no `sobe-tunel.sh`).
Enquanto isso não acontece, o quick tunnel atende a turma perfeitamente.

## Conferência rápida (checklist da Juh)
- [ ] Comando rodado, link impresso/salvo.
- [ ] Link aberto no celular (4G): caiu direto no login nome + senha? ✔
- [ ] Link colado no grupo da turma.
- [ ] ngrok parado só depois do teste ok.
