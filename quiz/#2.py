def negative(list):
    try:
        return tuple(num for num in list if num < 0 and num % 2 == 0)
    except:
        return None
print(negative([4, -6, 9, -8, -1]))