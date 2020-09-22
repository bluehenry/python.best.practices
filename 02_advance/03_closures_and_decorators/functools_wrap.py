import functools


def decorator(f):
    @functools.wraps(f)
    def wrapper():
        return (f)

    return wrapper


@decorator
def hello():
    """Print a message."""
    print('Hello Python!')


print(hello.__name__)
print(hello.__doc__)
