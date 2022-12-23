def sumOfMatrixDiagonal(List):
    # count=0
    # for i in range(len(list)):
    #     count+=list[i][i]
    # return count
    return sum(List[i][i] for i in range(len(List)))


print(sumOfMatrixDiagonal([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 2]]
))
