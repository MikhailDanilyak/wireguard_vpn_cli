from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader

from typing import List, Tuple
from dataclasses import dataclass

PYTHON_BASE_PATH = Path(__file__).parents[1]
WG_BASE_PATH = Path('/etc/wireguard/')


@dataclass
class WGClientConfig():
    '''
    Класс переменных для конфигурации WireGuard Client.
    '''
    client_name: str
    public_key_path: str
    private_key_path: str
    internal_address: str
    python_base_path: Path = PYTHON_BASE_PATH
    wg_base_path: Path = WG_BASE_PATH

    def _get_private_key_value(self):
        with open(self.private_key_path, 'r') as f:
            private_key = f.readlines()[0].rstrip()

        return private_key

    def _get_public_key_value(self):
        with open(self.public_key_path, 'r') as f:
            public_key = f.readlines()[0].rstrip()

        return public_key

    def _build_conf_dict(self):
        self.config_dict = {
            'private_key_path': self.private_key_path,
            'public_key_path': self.public_key_path,
            'client_name': self.client_name,
            'internal_address': self.internal_address,
        }

    def save_to_yaml(self):
        '''
        Сохраняет серверный конфигурационный файл по пути `wg_configs/users/<client_name>.yaml`.
        '''
        self._build_conf_dict()

        with open(self.python_base_path.joinpath('wg_configs', 'users', f'{self.client_name}.yaml'), 'w') as f:
            f.write(yaml.dump(self.config_dict))


@dataclass
class WGServerConfig():
    '''
    Класс переменных для конфигурации WireGuard server.
    '''
    private_key_path: str
    public_key_path: str
    external_address: str
    internal_address: str = '10.0.0.1/24'
    listen_port: str = '51820'
    interface: str = 'eth0'
    user_list: Tuple[str] = ()
    python_base_path: Path = PYTHON_BASE_PATH
    wg_base_path: Path = WG_BASE_PATH

    def _get_private_key_value(self):
        with open(self.private_key_path, 'r') as f:
            private_key = f.readlines()[0].rstrip()

        return private_key

    def _get_public_key_value(self):
        with open(self.public_key_path, 'r') as f:
            public_key = f.readlines()[0].rstrip()

        return public_key

    def _build_conf_dict(self):
        self.config_dict = {
            'private_key_path': self.private_key_path,
            'public_key_path': self.public_key_path,
            'external_address': self.external_address,
            'internal_address': self.internal_address,
            'listen_port': self.listen_port,
            'interface': self.interface,
            'user_list': self.user_list,
        }

    def save_to_yaml(self, file_name: str = 'wg_server'):
        '''
        Сохраняет серверный конфигурационный файл по пути `wg_configs/<file_name>`.
        '''
        self._build_conf_dict()

        with open(self.python_base_path.joinpath('wg_configs', f'{file_name}.yaml'), 'w') as f:
            f.write(yaml.dump(self.config_dict))

    def save_to_wg_config(self, file_name: str = 'wg0'):
        '''
        Сохраняет в целевое место файл с информацией для сервиса WireGuard.
        '''
        self._build_conf_dict()

        templates_path = self.python_base_path.joinpath('templates/')
        environment = Environment(loader=FileSystemLoader(templates_path))
        template = environment.get_template('wg0.conf.j2')

        private_key = self._get_private_key_value()

        content = template.render(
            private_key=private_key,
            **self.config_dict
        )

        with open(self.wg_base_path.joinpath(f'{file_name}.conf'), 'w+') as f:
            f.write(content+'\n')

        # TODO Добавить обработку и темплейт под новых юзеров


class WGServer():
    '''
    Класс описывающий серверную часть WireGuard.
    Методы для извлечения конфигов, инициализации, получения статусов.
    '''
    def __init__(self):
        pass
