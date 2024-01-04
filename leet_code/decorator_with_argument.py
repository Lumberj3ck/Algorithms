import time


def timer(time_type):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            resp = func(*args, **kwargs)
            end = time.time()
            print(end - start, "s" if time_type == "seconds" else "m")
            return resp

        return wrapper

    return actual_decorator


func = lambda x: x * 8

func = timer("asdf")(func)
# print(func(1234))


# some_func = timer(arg)(func)
@timer("seconds")
def some_func(x):
    return x * 8


print(some_func(1234))
