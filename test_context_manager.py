"""
With statement is a context manager
Helps to wrap the executioni of block with methods defined inside
It helps us to get rid off try except finally statemtents
"""


def test_cm_open():
    with open("test_context_manager.py", "r") as file:
        text = file.read()
        # file.write('asdfasdf')

    assert file.closed is True


class File:
    def __init__(self, path) -> None:
        self.file_obj = open(path)

    def __enter__(self):
        """
        if there is a target the value returned here is asigned to a target
        """
        print("\ninside enter method\ndoing something")
        return self.file_obj

    def __exit__(self, *args, **kwargs):
        print("\ninside exit method\ndoing something before exit")
        return self.file_obj.close()


def test_file_cm():
    """First of all expression is initialised then value returned by `__enter__` method is
    supplied to a target in current context it is a `file` var
    then context manager runs suite (nested code inside with block)
    if exception raised it calls `__exit__` method with parammentrs type value traceback
    based on this information we can differently manage execution of our code
    also with `__exit__` method we can replace `finally` block
    """

    with File("test_context_manager.py") as file:
        text = file.read()

    assert file.closed is True
