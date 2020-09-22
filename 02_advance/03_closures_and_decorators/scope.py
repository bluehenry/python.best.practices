global_str = 'global'


def outer(param_str='param'):
    local_str = 'local'

    def inner():
        print(global_str, param_str, local_str)

    inner()


outer()
