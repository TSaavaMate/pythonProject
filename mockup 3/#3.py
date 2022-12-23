def sumOfMatrixDiagonal(List):
    # count=0
    # for i,j in zip(range(len(list)),reversed(range(len(list)))):
    #     count+=list[i][j]
    # return count
    return sum(List[i][j] for i, j in zip(range(len(List)), reversed(range(len(List)))))


print(sumOfMatrixDiagonal(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
))
