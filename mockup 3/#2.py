def averageOfNegative(List):
    try:
        return sum(i for i in List if i < 0) / len([num for num in List if num < 0])
    except ZeroDivisionError:
        return 0


print(averageOfNegative([4, -6, 9, 8, -1]))
print(averageOfNegative([3, -1, -7, -9]))
print(averageOfNegative([4, 2, 6, 8]))
