from math import factorial

n = 4
a = list(range(n))
res = []


def add(i, arr):
    if i < 1:
        for el in arr:
            print(el, end=" ")
        print()
        return
    for el in a:
        if arr.count(el) < 1:
            arr2 = list(arr)
            arr2.append(el)
            add(i - 1, arr2)


add(n, res)
