import pytest, cards
from tasks import delete
from cards import Card

@pytest.mark.parametrize('card_state', ['done', 'in prog', 'initial'])
def test_finish(cards_db, card_state):
    index = cards_db.add_card(Card('some cards', state=card_state))
    cards_db.finish(index)
    card_from_db = cards_db.get_card(index)                         

    assert card_from_db.state == 'done'

@pytest.fixture(scope='session')
def cards_session(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp('db_temp')
    _db = cards.CardsDB(tmp_dir) 
    # if return instead of yield just returns value without teardown

    yield _db

    _db.close()

@pytest.fixture(scope='function')
def cards_db(cards_session, request):
    db = cards_session
    db.delete_all()
    # from test requesting this fixture we try to get marker with name cards_number 
    mark = request.node.get_closest_marker('cards_number')

    if mark and len(mark.args) > 0:
        num_cards = mark.args[0]
        for _ in range(num_cards):
            db.add_card(Card('learn something'))
    # don't need close db cause it doing session fixture we don't need to care about it
    return db

@pytest.fixture(scope='function')
def cards_db_with_3_card(cards_session):
    db = cards_session
    db.delete_all()
    # don't need close db cause it doing session fixture we don't need to care about it
    db.add_card(Card('learn something'))
    db.add_card(Card('learn something 1'))
    db.add_card(Card('learn something 2'))
    return db

@pytest.mark.cards_number(3)
def test_cards_0(cards_db):
    assert cards_db.count() == 3

def test_cards_3(cards_db_with_3_card):
    assert cards_db_with_3_card.count() == 3


@pytest.fixture(params=['done', 'in prog', 'initial'])
def card_state(request):
    return request.param
    
