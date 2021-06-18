def add_logging(func):
    def logging_func(*args):
        print("The %s() function was called with %r" % (func.__name__, args))
        answer = func(*args)
        return answer
    return logging_func


@add_logging
def increment(x):
    return x+1

@add_logging
def add(x, y):
    return x+y

if __name__ == "__main__":
    increment(4)

    add(4, 5)
