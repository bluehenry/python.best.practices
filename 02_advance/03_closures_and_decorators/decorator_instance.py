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
def rotate_list(l):
    return l[1:] + [l[0]]


print(rotate_list([1,2,3]))

tracer.enabled = False

print(rotate_list([7,8,9]))