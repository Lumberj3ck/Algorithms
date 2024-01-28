## Pytest 

Runing `pytest` will search for test files inside all the subdirectories and files
and search for test function (which should start from either '_test', 'test_')

`pytest directory` the same as `pytest` but for given directory


`pytest help` for the command list 


`-v` verbose flag

`-q` `--quiet` decrease verbosity

`-x` exit first for exiting after first failure
`--maxfail=num` the same as `-x`
`-l` `--showlocals` shows local variables when test failes

`--lf`, `--last-failed` way to run only failed tests
`--ff`, `--first-failed` start from the failed tests then run the rest 

`--tb=no` turns off error traceback


### Marks
`@pytest.mark.mark_name` to mark some tests, group them and run together
to run all tests with the same marker `pytest -v -m marker_name`

`@pytest.mark.xfail(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')`
mark test as expected to fail and do not mark it as failed 
see learning_pytest/test_unique_id.py


`@pytest.mark.skip(reason='misunderstood the api')`
just skip the test if we don't want to see it 
see learning_pytest/test_unique_id.py


`@pytest.mark.skipif(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')`
skipif expression inside True
see learning_pytest/test_unique_id.py


### Pytest Raises
with pytest.raises(SomeError):
construction where pytest expect error of given type
if there is no error test fails
see learning_pytest/test_pyt_raises.py



### Pytest Fixtures
@pytest.fixture

if test_function asks for argument for example  
```python
def test_default_case(unordered_array):
    print(unordered_array)

    result = bubble_sort(unordered_array)
    expected = sorted(unordered_array)

    assert result == expected
```

pytest'll search for unordered_array fixture

```python
@pytest.fixture(scope='module')
def unordered_array():
    import random, time
    unordered_array = [random.randint(1, 50) for i in range(20)]
    time.sleep(2)
    yield unordered_array
```

everything before yield expression is a setup for function 

everything after yield is a teardown 

**scope** argument of decorator helps to determine how frequently fixture will run
e.g for scope = 'function'
setup & teardown will run for every test 
for scope = 'module' 
they will run once per module no matter how many tests in module
for scope = 'class' 
once per class


**autouse** argument for applying fixture for every function regardless of 
argument test function. It quite usefull when fixture don't return data and 
just sets up environment

**params**
`@pytest.fixture(params=['done', 'in prog', 'initial'])`
parametrise fixture for different test cases it's pretty powerfull
feature case gives you the ability create different setup conditions depends 
on different arguments


