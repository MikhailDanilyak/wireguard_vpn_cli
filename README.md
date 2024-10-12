# wireguard_vpn_cli
Надстройка над протоколом WireGuard для более удобного использования

Первым делом заходим в скопированную папку из git и выполняем bash-скрипт, который установит необходимые пакеты, обновит зависимости и создаст пару ключей для WireGuard сервера с помощью команды:
```sh
./install.sh
```

## Дополнительная информация

Удаление созданных окружений poetry в папке:
```sh
rm -rfv `poetry env info -p`
```

Под капотом генерации ключа работает:
```sh
openssl rand -base64 32
```

Запуск тестов:
```sh
poetry run pytest tests/test_wg_server.py -vv
```