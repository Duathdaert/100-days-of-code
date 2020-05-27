g = 'global'


def outer(p='param'):
    l = 'local'

    def inner():
        print(g, p, l)
    inner()


def enclosing():

    def local_func():
        print('local func')
    return local_func()
