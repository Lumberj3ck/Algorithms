"""
So Mock it's stub which we can use instead of real objects
and then check if it was called right
"""


from unittest import mock
import pytest
from unittest.mock import Mock


class foo:
    bar = 12
    asdf = 1234

    def method1(self):
        return 23


def test_called_with(mock_obj):
    mock_obj(3, 4, 5, key="value")
    mock_obj.assert_called_with(3, 4, 5, key="value")
    assert isinstance(mock_obj, Mock)


def test_assign_value(mock_obj):
    mock_obj.asdf = 5
    assert mock_obj.asdf == 5


def test_mock_spec_undefined_attribute(mock_spec):
    with pytest.raises(AttributeError):
        mock_spec.undefined_attr
    mock_spec.bar


def test_mock_spec(mock_spec, mock_obj):
    assert isinstance(mock_spec, foo)
    assert not isinstance(mock_obj, foo)


def test_return_val():
    """value returned by mock when it's called"""
    m = Mock(return_value=42)

    assert m(1, 2, 3) == 42


def test_deleting_attributes(mock_obj):
    """deleting attribute if don't need,
    the same behavior we can get passing the object to spec attribute
    """
    mock_obj.some_attribute
    del mock_obj.some_attribute
    with pytest.raises(AttributeError):
        mock_obj.some_attribute


@pytest.fixture
def mock_spec():
    mock_with_spec = Mock(spec=foo)
    return mock_with_spec


@pytest.fixture
def mock_obj():
    return Mock()
