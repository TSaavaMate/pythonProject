dicta = {"hi": [1, 3, 4, 6, 5, 2, 7], "no": [2, 4, 3, 6, 7, 8], "yes": [10, 34, 21, 34, 16], "done": [10, 7, 3, 4]}


def keyWithBiggestValue(Dict):
    biggestValue = 0
    biggestKeys = []
    for key in Dict.keys():
        if len(Dict[key]) > biggestValue:
            biggestValue = len(Dict[key])
    for key in Dict.keys():
        if biggestValue == len(Dict.get(key)):
            biggestKeys.append(key)
    return biggestKeys


print(keyWithBiggestValue(dicta))
