dicta = {"hi": [1, 3, 4, 6, 5, 2, 7], "no": [2, 4, 3, 6, 7, 8], "yes": [10, 34, 21, 34, 16], "done": [10, 7, 3, 4]}


def multipleOf3(Dict):
    Tuple = ()
    for values in Dict.values():
        for element in values:
            if element % 3 == 0:
                Tuple += element,
    return Tuple


print(multipleOf3(dicta))
