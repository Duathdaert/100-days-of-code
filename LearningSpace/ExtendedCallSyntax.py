def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


# t = (11, 12, 13, 14)
# print_args(*t)
# arg1 = 11, arg2 = 12, args = 13,14


def colour(red, green, blue, **kwargs):
    print("r =", red)
    print("g =", green)
    print("b =", blue)
    print(kwargs)


# k = {'red':21, 'green':68, 'blue':120, 'alpha' :52 }
# OR k = dict(red=21, green=68, blue=120, alpha=52)
# colour(**k)
# r = 21, g = 68, b = 120, {'alpha': 52}


def trace(f, *args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result =", result)
    return result


# ExtendedCallSyntax.trace(int, "ff", base=16)
# args = ('ff',)
# kwargs =  {'base': 16}
# result = 255
# 255
