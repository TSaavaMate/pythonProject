dicta = {"hi": [1, 3, 4, 6, 5, 2, 7], "no": [2, 4, 3, 6, 7, 8], "yes": [10, 34, 21, 34, 16], "done": [10, 7, 3, 4]}


def sumOfValues(Dict):
    Sum = 0
    for value in Dict.values():
        for element in value:
            Sum += element
    return Sum
    # return sum(element  for value in dict.values() for element in value) in oneline


print(sumOfValues(dicta))
