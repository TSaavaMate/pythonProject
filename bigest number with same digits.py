import itertools


def next_bigger(n):
    for i in sorted(list(("".join(x)) for x in list(itertools.permutations(list(str(n)))))):
        if int(i) > n:
            return int(i)
    return -1


print(next_bigger(2017))
