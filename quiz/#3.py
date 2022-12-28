def matrixDiagonal(list):
    return tuple(list[i][i] for i in range(len(list))),\
           tuple(list[i][j] for i, j in zip(range(len(list)), reversed(range(len(list)))))
print(matrixDiagonal(
[[1,2,(3)],
 [4,(5),6],
 [(7),8,9]]))