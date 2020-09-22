store = []


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    store.append(last_letter)

    # print last_letter() address
    print(last_letter)

    # sorted key is a function
    print(sorted(strings, key=last_letter))


sort_by_last_letter(['ghi', 'def', 'abc'])
print(store)
