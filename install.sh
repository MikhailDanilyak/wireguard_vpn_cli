#!/bin/bash

# Update server packages
sudo apt update

# Install wireguard package
sudo apt install wireguard

# Change directory to wireguard config folder
cd /etc/wireguard/

# Create keypair files for wireguard server
if [ ! -f /etc/wireguard/server_privatekey ] && [ ! -f /etc/wireguard/server_publickey ]; then
    echo "No server config key files find. Let's create new ones!"
    wg genkey | tee /etc/wireguard/server_privatekey | wg pubkey | tee /etc/wireguard/server_publickey
elif [ ! -f /etc/wireguard/server_privatekey ]; then
    echo "/etc/wireguard/server_privatekey is missing. Remove artifacts and try again!"
elif [ ! -f /etc/wireguard/server_publickey ]; then
    echo "/etc/wireguard/server_publickey is missing. Remove artifacts and try again!"
else
    echo "Server config key-pair is set."
fi

# Install python
sudo apt install python3

# Install poetry
mkdir -p ~/scripts
curl -sSL https://install.python-poetry.org > ~/scripts/install_poetry.py
source ~/.bashrc
python3 ~/scripts/install_poetry.py

# Poetry path '~/.local/share'
# Append poetry path to .bashrc
LINE='PATH="$HOME/.local/share/pypoetry/venv/bin:$PATH"'
FILE=$HOME/.bashrc
grep -qF "$LINE" "$FILE"  || echo "$LINE" | sudo tee --append "$FILE"
source ~/.bashrc

# Set up poetry python enviroment to be in .venv folder near pyproject.toml
poetry config virtualenvs.in-project true
