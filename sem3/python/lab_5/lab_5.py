from time import time
from functools import wraps


def checked(*types):
    def decorator(func):
        code = func.__code__
        fname = func.__name__
        names = code.co_varnames[:code.co_argcount]

        @wraps(func)
        def decorated(*args, **kwargs):
            for argtype in types:
                argname = names[types.index(argtype)]
                try:
                    argval = args[names.index(argname)]
                except ValueError:
                    argval = kwargs.get(argname)
                if argval is None:
                    raise TypeError(
                        "{}(...): arg '{}' is null".format(
                            fname, argname))
                if not isinstance(argval, argtype):
                    raise TypeError(
                        "{}(...): arg '{}': type is {}, must be {}".format(
                            fname, argname, type(argval), argtype))
            return func(*args, **kwargs)
        return decorated
    return decorator


@checked(int)
def fib(n):
    f_0 = 1
    f_1 = 1
    if n <= 0:
        raise ValueError("n is smaller than zero")
    elif n == 1:
        return f_1
    else:
        for _ in range(2, n):
            f = f_0 + f_1
            f_0 = f_1
            f_1 = f
        return f_1


@checked(str, int)
def mult_string(s, n):
    return s * n


@checked(float, float)
def area(a, b):
    return a * b


def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        print('Execution time: {}'.format(format((te - ts), '.2f')))
        return result
    return timed


@timeit
def primes(maxn):
    '''Решето Эратосфена'''
    p = [False] * (maxn + 1)
    result = []
    for i in range(2, maxn + 1):
        if p[i] == False:
            for j in range(i * i, maxn + 1, i):
                p[j] = True
            result.append(i)
    return result

primes(10000000)
