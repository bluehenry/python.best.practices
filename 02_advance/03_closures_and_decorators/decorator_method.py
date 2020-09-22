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


class AddSuffix:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def add_suffix(self, name):
        return name + self.suffix


im = AddSuffix(' Python')
print(im.add_suffix('Hello'))
