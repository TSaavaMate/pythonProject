from math import sqrt, floor


def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0):
        return False
    return True
print(isPerfect(49))
print(floor(4.9))