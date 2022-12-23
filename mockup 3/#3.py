def sumOfMatrixDiagonal(list):
    # count=0
    # for i,j in zip(range(len(list)),reversed(range(len(list)))):
    #     count+=list[i][j]
    # return count
    return sum(list[i][j] for i,j in zip(range(len(list)),reversed(range(len(list)))))
print(sumOfMatrixDiagonal(
    [[1, 2, (3)],
     [4, (5), 6],
     [(7), 8, 9]]
))
