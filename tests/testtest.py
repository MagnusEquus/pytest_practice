a = [1, 3, 2, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]


def remove_duplicates(a:list) -> list:
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    return res


print(remove_duplicates(a))