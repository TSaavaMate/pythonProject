dicta = {"hi": [1, 3, 4, 6, 5, 2, 7], "no": [2, 4, 3, 6, 7, 8], "yes": [10, 34, 21, 34, 16], "done": [10, 7, 3, 4]}


def averageDictOf(Dict):
    newDict = {}
    for key, values in Dict.items():
        newDict[key] = sum(element for element in values) / len(values)  # if average should be floated
        # newDict[key]=int(sum(element for element in values)/len(values)) if average should be int
    return newDict

print(averageDictOf(dicta))
