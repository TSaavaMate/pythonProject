def sumOfMatrixDiagonal(list):
    # count=0
    # for i in range(len(list)):
    #     count+=list[i][i]
    # return count
    return sum(list[i][i] for i in range(len(list)))
print(sumOfMatrixDiagonal([
    [1,2,(3)],
    [4,5,6],
    [7,8,2]]
))