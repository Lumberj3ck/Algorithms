import tasks, pytest



@pytest.mark.get
@pytest.mark.smoke
def test_add_raise():
    with pytest.raises(TypeError):
        tasks.add(task='not a task object')

@pytest.mark.smoke
def test_start_tasks_db_raises():
    with pytest.raises(ValueError) as ex_info:
        tasks.start_tasks_db('some/great/path', 'sqlite')

    assert ex_info.value.args[0] == "db_type must be a 'tiny' or 'mongo'"
 



