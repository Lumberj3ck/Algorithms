def timer(func):
    def inner(*args, **kwargs):
        import time
        start = time.time()
        result = func()
        end = time.time()
        print("Elapsed time ", end - start)
        return result

    return inner


def coroutine(func):
    def inner(*args, **kwargs):
        generator = func(*args, **kwargs)
        generator.send(None)
        return generator
    return inner


# coroutine(average)()  almost the same as average()
@timer
# @coroutine
def average():
    sum = 0
    count = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print("Cycle is done by throwing exception")
        else:
            sum += x
            count += 1
            average = round(sum / count, 2)


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print("Message", message)
    return "Returned from subgen"


def delegetor(subgen):
    result = yield from subgen
    print(result)


def reader(file_path: str):
    file = open(file_path, "r")
    for i in file.readlines():
        yield i
