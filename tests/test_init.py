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

def test_arrow_flight():
    client = init()
    root = client.data

    my_source = root.hkex_sandbox_test.test.get()
    # my_source = root.as_stm_sanctumapp.test.get()
    my_source_content = my_source.query()
    print(my_source_content)
    assert my_source_content is not None

def test_arrow_flight_client_reuse():
    client = init()
    root = client.data

    my_source = root.hkex_sandbox_test.test.get()
    # my_source = root.as_stm_sanctumapp.test.get()
    my_source_content = my_source.query()
    print(my_source_content)

def test_arrow_flight_number_path():
    client = init()
    root = client.data

    # my_source = root.hkex_sandbox_test.__getattr__('2021').test1.get()
    # my_source = root.hkex_sandbox_test.__getattr__('2021folder').test3.get()
    # my_source = root.hkex_sandbox_test.test.get()
    # my_source = root.hkex_sandbox_test.test2021.test2.get()
    my_source = root.ng_test_space.ng_test_folder.test_1028.get()
    # my_source = root.as_stm_sanctumapp.test.get()
    my_source_content = my_source.query()
    print(my_source_content)
    assert my_source_content is not None
