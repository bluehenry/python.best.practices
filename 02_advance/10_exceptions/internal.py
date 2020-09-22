def modules_three(n):
    r = n % 3
    if r == 0:
        print('Multiple of 3')
    elif r == 1:
        print('Remainder 1')
    else:  # r == 2
        assert r == 2, 'Remainder id not 2'
        print('Remainder 2')


def modules_four(n):
    r = n % 4
    if r == 0:
        print('Multiple of 4')
    elif r == 1:
        print('Remainder 1')
    else:  # r == 2
        assert r == 2, 'Remainder id not 2'
        print('Remainder 2')
