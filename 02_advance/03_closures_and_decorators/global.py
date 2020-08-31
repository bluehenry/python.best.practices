message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print(f'enclosing message: {message}')
    local()


print(f'global message: {message}')
enclosing()
print(f'global message: {message}')