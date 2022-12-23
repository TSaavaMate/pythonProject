def sumOfEven(List):
    # count=0
    # for i in list:
    #     if i%2==0:
    #         count+=i
    # if count==0:
    #     return -1
    # return count
    return -1 if sum(i for i in List if i % 2 == 0) == 0 else sum(i for i in List if i % 2 == 0)


print(sumOfEven([4, 2, 12]))
print(sumOfEven([3, -1, -7, -9]))
print(sumOfEven([4, -6, 9, 8, 1]))
