from pathlib import Path

def test_home_path():
    home_path = Path().home()

    assert str(home_path) == '/home/lumberjack'


def test_given_directory():
    dir = '/home/lumberjack/code'
    path_obj = Path(dir)

    assert str(path_obj) == dir

def test_current_directory():
    curr_dir = Path().cwd() / 'test_pathlib.py'

    assert  str(curr_dir) == __file__

def test_output():
    assert str(Path(__file__)) == __file__

def test_is_exsist():
    print(Path().group())
    assert Path(__file__).exists() is True
    assert Path('some_random_name.py').exists() is False 

