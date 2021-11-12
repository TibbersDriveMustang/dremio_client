import dremio_client

def test_version():
    assert dremio_client.__version__ == '0.15.1'


