# Positional argument
def arg(*args):
    for i in args:
        print(i)
    print(args)
    print(type(args))


arg(1, 2, 3)


# Key word arguments
def kwargs(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'key={key}, value={value}')


kwargs('img', src='moment.jpg', boarder=1)


# Forward arguments
def fun1(*args, **kwargs):
    print('--forward args--')
    print(args)
    print(kwargs)


def forward_args(fun, *args, **kwargs):
    fun(*args, **kwargs)


forward_args(fun1, 1, arg='hello')
