from collections import namedtuple

Task = namedtuple('Task', ['survey', 'description', 'name'])
new_task = Task(survey=1, description='some note',  name=3)

def test_namedtuple():
    assert new_task.survey == 1
    assert new_task.description == 'some note'
    assert new_task.name == 3 

def test_asdict():
    attr_dict = new_task._asdict()
    expected = {
            'survey': 1, 
            'description': 'some note and text',
            'name': 3
            }
    assert attr_dict == expected



