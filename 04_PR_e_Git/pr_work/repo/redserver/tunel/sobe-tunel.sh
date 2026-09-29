#!/usr/bin/env bash
# sobe-tunel.sh — túnel público SEM tela de aviso (cloudflared quick tunnel)
# O QUÊ: publica o vhost pcs-replica (:8080) num link https://….trycloudflare.com
# POR QUÊ: o ngrok grátis mostra a tela "Visit Site" antes do site; o cloudflared
#          quick tunnel não mostra nada — o aluno clica e cai DIRETO no login.
# ONDE:  rodar no redserver (sudo bash sobe-tunel.sh). Uso:
#          sudo bash sobe-tunel.sh            # sobe na porta 8080 (padrão)
#          sudo bash sobe-tunel.sh 8081       # outra porta, se preciso
#          sudo bash sobe-tunel.sh --parar    # derruba o túnel avulso
# O link muda a cada subida (como no ngrok): ele fica impresso aqui e salvo em
# /root/url-tunel.txt. Para link FIXO, veja LEIA-ME_TUNEL.md (túnel nomeado).
set -euo pipefail

LOG=/var/log/tunel/cloudflared.log
mkdir -p /var/log/tunel

if [ "${1:-}" = "--parar" ]; then
  pkill -f 'cloudflared tunnel' || true
  echo "túnel avulso derrubado."
  exit 0
fi

PORTA="${1:-8080}"

# não deixa dois túneis avulsos brigando
pkill -f 'cloudflared tunnel' || true
sleep 1

if ! command -v cloudflared >/dev/null 2>&1; then
  echo ">> instalando cloudflared (binário oficial)…"
  curl -fsSL -o /tmp/cloudflared \
    https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
  install -m 0755 /tmp/cloudflared /usr/local/bin/cloudflared
fi

: > "$LOG"
nohup cloudflared tunnel --url "http://127.0.0.1:${PORTA}" --no-autoupdate \
  >>"$LOG" 2>&1 &
echo ">> aguardando o túnel registrar o link…"
for i in $(seq 1 20); do
  sleep 1
  URL="$(grep -oE 'https://[a-zA-Z0-9-]+\.trycloudflare\.com' "$LOG" | head -1 || true)"
  [ -n "$URL" ] && break
done

if [ -z "${URL:-}" ]; then
  echo "!! não achei o link no log — veja: tail -50 $LOG" >&2
  exit 1
fi

echo "$URL" > /root/url-tunel.txt
echo
echo "  LINK DOS ALUNOS (PI-I):  ${URL}/KiT_Sala_de_Aula/"
echo "  LINK DOS ALUNOS (LP2):   ${URL}/KiT_Sala_de_Aula/?d=lp2"
echo "  (salvo em /root/url-tunel.txt — clique cai direto no login nome+senha)"
echo
echo "Para subir SEMPRE junto com o servidor, use o serviço systemd:"
echo "  sudo cp tunel-cloudflared.service /etc/systemd/system/"
echo "  sudo systemctl daemon-reload && sudo systemctl enable --now tunel-cloudflared"
echo "  journalctl -u tunel-cloudflared | grep -oE 'https://[a-z0-9-]*\\.trycloudflare\\.com' | head -1"
