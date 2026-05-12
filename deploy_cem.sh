#!/usr/bin/env bash
# Deploiement / mise a jour du bot CEM-CG sur le VPS Contabo
# Usage : bash deploy_cem.sh
# Prerequis : git, python3, python3-venv installes ; user freqtrader avec sudo
set -e

REPO="https://github.com/Gamehdi05/CEM-CG.git"
DIR="/home/freqtrader/cem-cg"

echo "=== 1. Recuperation du code ==="
if [ -d "$DIR/.git" ]; then
    cd "$DIR" && git pull
else
    git clone "$REPO" "$DIR"
    cd "$DIR"
fi

echo "=== 2. Environnement virtuel Python ==="
if [ ! -d "$DIR/venv" ]; then
    python3 -m venv "$DIR/venv"
fi
"$DIR/venv/bin/pip" install --upgrade pip
"$DIR/venv/bin/pip" install -r "$DIR/requirements.txt"

echo "=== 3. Navigateur Playwright (chromium headless) ==="
"$DIR/venv/bin/playwright" install chromium
echo "    Libs systeme (apt, via sudo) :"
sudo "$DIR/venv/bin/playwright" install-deps chromium \
    || echo "    ATTENTION: install-deps a echoue — relancer manuellement : sudo $DIR/venv/bin/playwright install-deps chromium"

echo "=== 4. Verification du .env ==="
if [ ! -f "$DIR/.env" ]; then
    cp "$DIR/.env.example" "$DIR/.env"
    echo ""
    echo "    >>> Le fichier $DIR/.env vient d'etre cree depuis l'exemple."
    echo "    >>> EDITE-LE avec tes vraies cles API, puis relance ce script :"
    echo "    >>>   nano $DIR/.env"
    echo ""
    exit 1
fi

echo "=== 5. Service systemd ==="
sudo cp "$DIR/cem-cg.service" /etc/systemd/system/cem-cg.service
sudo systemctl daemon-reload
sudo systemctl enable cem-cg
sudo systemctl restart cem-cg

echo ""
echo "=== Termine. Etat du service : ==="
sudo systemctl status cem-cg --no-pager || true
echo ""
echo "Commandes utiles :"
echo "  sudo systemctl status cem-cg       # etat"
echo "  sudo systemctl restart cem-cg      # redemarrer"
echo "  sudo systemctl stop cem-cg         # arreter"
echo "  journalctl -u cem-cg -f            # logs systemd en direct"
echo "  tail -f $DIR/bot.log               # logs applicatifs"
