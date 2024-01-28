def bubble_sort(unordered_array: list) -> list:
    for i in range(len(unordered_array)):
        for j in range(len(unordered_array) - i - 1):
            if unordered_array[j] > unordered_array[j + 1]:
                unordered_array[j], unordered_array[j + 1] = unordered_array[j + 1], unordered_array[j]

    return unordered_array


import pytest, time
# @pytest.mark.parametrize('unordered_array,time',
# [
# ( [3, 7, 5, 1, 8, 2], 'time' ),                    
# ( [1, 6, 3, 8, 5, 4 ], 'time' ),                    
# ( [6, 4, 7, 1, 8, 4 ], 'time' )                    ]
# )
def test_default_case(unordered_array):
    result = bubble_sort(unordered_array)
    expected = sorted(unordered_array)

    assert result == expected


@pytest.fixture(autouse=True)
def time_measure():
    ''' 
    Fixture which measures test running time
    '''
    start_time = time.time()
    yield 
    end_time = time.time()
    delta = end_time - start_time
    print('\nTest duration: {:0.2}'.format(delta))


@pytest.fixture(scope='module')
def unordered_array():
    '''
    Generate random array of 20 items
    '''
    import random
    unordered_array = [random.randint(1, 50) for i in range(20)]
    yield unordered_array
