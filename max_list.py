def max_list(lst):
    m = lst[0]
    for i in lst:
        if i >= m:
            m = i
    return m


def in_list(lst, value):
    exists = False
    for i in lst:
        if i == value:
            exists = True
            break
    return exists

if __name__ == '__main__':
    print(max_list(range(5)))
    print(max_list([3, 2, 1, 8]))
