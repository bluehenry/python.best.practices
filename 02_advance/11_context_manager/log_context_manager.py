import contextlib
import sys


class LogContextManager:

    def __enter__(self):
        print('__enter__')
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('__exit__')
        else:
            print('__exit__ Exception detected: {exc_type}, {exc_val}, {exc_tb}')
        return


@contextlib.contextmanager
def logging_context_manager():
    print('enter')
    try:
        yield 'you are in a with-block'
    except Exception:
        print('exceptional exit', sys.exc_info())
        raise


def main():
    with LogContextManager() as l:
        print(l)

    with logging_context_manager() as l:
        raise ValueError('Something went wrong.')


if __name__ == '__main__':
    main()
