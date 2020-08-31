def enclosing():
    str = 'closed over'

    def local_func():
        print(str)

    return local_func

lf = enclosing()
lf()
print(lf.__closure__)