import pytest 



@pytest.mark.raises
def test_raises():
    with pytest.raises(ValueError):
        'asdfasdf'[0] = 'asdf'


