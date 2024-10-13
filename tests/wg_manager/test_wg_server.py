import pytest
from pathlib import Path
import sys
import os 

sys.path.insert(0, Path(__file__).parents[1])

from wg_manager.wg_server import WGServerConfig, WGClientConfig

TEST_PATH = Path(__file__).parents[1]
TEST_PYTHON_BASE_PATH = Path(__file__).parents[0]
TEST_WG_BASE_PATH = TEST_PATH.joinpath('etc', 'wireguard')

EXTERNAL_IP = '84.252.134.48'

class TestWGServerConfig():
    def setup_method(self):
        pass

    def tear_down_method(self):
        pass

    def test__save_to_yaml(self):
        private_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_privatekey'))
        public_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_publickey'))
        external_address = EXTERNAL_IP
        internal_address = '10.1.1.1/24'
        listen_port = '51830'
        user_list = ()

        wg_server_config = WGServerConfig(
            private_key_path=private_key_path,
            public_key_path=public_key_path,
            external_address=external_address,
            internal_address=internal_address,
            listen_port=listen_port,
            user_list=user_list,
            python_base_path=TEST_PATH,
            wg_base_path=TEST_WG_BASE_PATH,
        )

        wg_server_config.save_to_yaml(file_name='test_wg_server')

        expected_path = str(TEST_PATH.joinpath('wg_configs','test_wg_server.yaml'))

        assert os.path.isfile(expected_path)

    def test__save_to_wg_config(self):
        private_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_privatekey'))
        public_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_publickey'))
        external_address = EXTERNAL_IP
        internal_address = '10.1.1.1/24'
        listen_port = '51830'
        user_list = ()

        wg_server_config = WGServerConfig(
            private_key_path=private_key_path,
            public_key_path=public_key_path,
            external_address=external_address,
            internal_address=internal_address,
            listen_port=listen_port,
            user_list=user_list,
            python_base_path=TEST_PATH,
            wg_base_path=TEST_WG_BASE_PATH,
        )

        wg_server_config.save_to_wg_config()

        assert os.path.isfile(str(TEST_WG_BASE_PATH.joinpath('wg0.conf')))


class TestWGClientConfig():
    def setup_method(self):
        pass

    def tear_down_method(self):
        pass

    def test__save_to_yaml(self):
        client_name = 'test_user'
        public_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_user_publickey'))
        private_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_user_privatekey'))
        internal_address = '10.1.1.2/24'

        wg_client_config = WGClientConfig(
            client_name=client_name,
            public_key_path=public_key_path,
            private_key_path=private_key_path,
            internal_address=internal_address,
            python_base_path=TEST_PATH,
        )

        wg_client_config.save_to_yaml()

        expected_path = str(TEST_PATH.joinpath('wg_configs', 'users', 'test_user.yaml'))

        assert os.path.isfile(expected_path)
