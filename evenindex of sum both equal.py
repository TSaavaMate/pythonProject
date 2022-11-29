def find_even_index(arr):
    count = 0
    for i in range(len(arr)):
        for b in range(i):
            count += arr[b]
            if count == (sum(arr) - arr[i]) / 2:
                return i
            else:
                count = 0
        if count == 0:
            return -1


def find_even_index2(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1



print(find_even_index([10, -80, 10, 10, 15, 35, 20]))
