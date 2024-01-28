def gen():
    print('pre test')
    yield 
    print('post test')


print(gen())
some_gen = gen()
next(some_gen)
# next(some_gen)


from dataclasses import asdict, dataclass, field
import pytest

@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = None
    id: int = field(default=None, compare=False)

    @staticmethod
    def from_dict(d):
        return Card(**d)

    def to_dict(self):
        return asdict(self)

def test_field_mutability():
    card.summary = 'sometext'
    card1 = Card('sometext', 'lumberjack', 'todo', 12)
    assert card == card1

def test_from_dict():
    new_card = Card.from_dict({'summary': 'asdf', 'owner': 'lumberjack', 'state': 'todo', 'id': 12})
    assert new_card == card


def test_two_inst_equal():
    card2 = Card('asdf', 'lumberjack', 'todo', 12)
    card3 = Card('asdf', 'lumberjack', 'todo', 99)
    assert card == card2 
    assert card2 == card3 


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    global card
    card = Card('asdf', 'lumberjack', 'todo', 12)
    yield
