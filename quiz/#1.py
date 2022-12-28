def maketouple(list):
    try:
        return max(num for num in list if num % 2 == 0), min(num for num in list if num % 2 == 1)
    except ValueError:
        if list[0]%2==0:
            return max(num for num in list if num % 2 == 0), None
        else:
            return None, min(num for num in list if num % 2 == 1)


print(maketouple([4, 2, 12 ]))
print(maketouple([3,5,7,-1 ]))
print(maketouple([3,5,8,10 ]))