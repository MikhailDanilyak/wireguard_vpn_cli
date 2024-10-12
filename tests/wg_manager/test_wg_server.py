import pytest
from pathlib import Path
import sys
import os 

sys.path.insert(0, Path(__file__).parents[1])

from wg_manager.wg_server import WGServerConfig

TEST_PATH = Path(__file__).parents[1]
TEST_PYTHON_BASE_PATH = Path(__file__).parents[0]
TEST_WG_BASE_PATH = TEST_PATH.joinpath('etc', 'wireguard')

class TestWGServerConfig():
    def setup_method(self):
        pass

    def tear_down_method(self):
        pass

    def test__save_to_yaml(self):
        private_key_path = '/etc/wireguard/test_private_key'
        address = '10.1.1.1/24'
        listen_port = '51830'
        user_list = ()

        wg_server_config = WGServerConfig(
            private_key_path=private_key_path,
            address=address,
            listen_port=listen_port,
            user_list=user_list,
            python_base_path=TEST_PATH,
            wg_base_path=TEST_WG_BASE_PATH
        )

        wg_server_config.save_to_yaml(file_name='test_wg_server.yaml')

        expected_path = str(TEST_PATH.joinpath('wg_configs','test_wg_server.yaml'))

        assert os.path.isfile(expected_path)

    def test__save_to_wg_config(self):
        private_key_path = str(TEST_PATH.joinpath('etc/wireguard/test_private_key'))
        address = '10.1.1.1/24'
        listen_port = '51830'
        user_list = ()

        wg_server_config = WGServerConfig(
            private_key_path=private_key_path,
            address=address,
            listen_port=listen_port,
            user_list=user_list,
            python_base_path=TEST_PATH,
            wg_base_path=TEST_WG_BASE_PATH
        )

        wg_server_config.save_to_wg_config()

        assert os.path.isfile(str(TEST_WG_BASE_PATH.joinpath('wg0.conf')))

