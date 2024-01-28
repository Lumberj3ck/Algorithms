import pytest, tasks
from tasks import Task, add


@pytest.mark.smoke
def test_add_returns_valid_id():
    new_task = Task('do something')
    task_id = add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_set_id():
    new_task = Task('do something')
    task_id = add(new_task)

    db_task = tasks.get(task_id)

    assert db_task.id == task_id


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    print(tmpdir)
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    tasks.stop_tasks_db()
