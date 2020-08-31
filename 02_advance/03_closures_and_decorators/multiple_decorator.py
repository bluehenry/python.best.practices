def escape_unicode(f):
    # Using *args, **kwargs to accept any arguments
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    # Return wrap function, which call ascii(city())
    return wrap

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
@escape_unicode
def city():
    return '广州'

print(city())