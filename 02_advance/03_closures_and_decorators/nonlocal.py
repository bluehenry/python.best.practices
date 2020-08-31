message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print(f'enclosing message: {message}')
    local()
    print(f'enclosing message: {message}')


print(f'global message: {message}')
enclosing()
print(f'global message: {message}')