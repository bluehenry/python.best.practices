def escape_unicode(f):
    # Using *args, **kwargs to accept any arguments
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    # Return wrap function, which call ascii(city())
    return wrap


@escape_unicode
def city():
    return '广州'


print(city())
