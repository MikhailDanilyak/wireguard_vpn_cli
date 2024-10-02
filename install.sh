#!/bin/bash

# Обновляем пакеты на сервере
sudo apt update

# Устанавливаем сам клиент wireguard
sudo apt install wireguard

# Переходим в конфигурационную папку для wireguard
cd /etc/wireguard/

# Создаем файлы с парой ключей для сервера wireguard
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
