import pytest, tasks
from tasks import *

@pytest.mark.skip(reason='misunderstood the api')
def test_unique_id():
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2

@pytest.mark.skipif(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')
def test_unique_id_1():
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2

@pytest.mark.xfail(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')
def test_unique_id_1():
    ''' expected to fail''' 
    id1 = tasks.unique_id()
    assert id1 == 'asdf' 

@pytest.mark.xfail(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')
def test_unique_id_2():
    ''' expected to pass''' 
    id1 = tasks.unique_id()
    assert id1 != 'asdf' 

def test_unique_id_3():
    ids = []
    ids.append(tasks.add(Task('task one')))
    ids.append(tasks.add(Task('task two')))
    ids.append(tasks.add(Task('task three')))
    new_id = tasks.unique_id()
    assert new_id not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()
