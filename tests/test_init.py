import os
from dremio_client import init

def test_config_dir():
    # config_dir = '/var/run/secrets/user_credentials'
    config_dir = '/Users/hongyiguo/Desktop/HKEX/Sanctum/dremio_client/dremio_client'
    init(config_dir)
    if 'XDG_CONFIG_DIRS' in os.environ:
        assert os.environ['XDG_CONFIG_DIRS'] == config_dir
        del os.environ['XDG_CONFIG_DIRS']

def test_default_config():
    client = init()
