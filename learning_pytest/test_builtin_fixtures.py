import pytest

def test_tmp_path(tmp_path):
    file = tmp_path / "file1.txt"
    print(file)
    file.write_text("Hello")

    assert file.read_text() == 'Hello'

def test_tmp_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub")
    file = path / "file.txt"
    file.write_text("Hello")

    assert file.read_text() == 'Hello'

def hello():
    with open('file.txt', 'w') as file:
        file.write('Hello')

@pytest.mark.skip(reason='creates file and don`t delete it')
def test_hello():
    hello()
    with open('file.txt', 'r') as file:
        assert file.read() == 'Hello'

def test_hello_tmp(tmp_path, monkeypatch):
    print(tmp_path)
    monkeypatch.chdir(tmp_path)
    hello()
    with open('file.txt', 'r') as file:
        assert file.read() == 'Hello'



