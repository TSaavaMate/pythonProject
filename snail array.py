array = [[1, 2, 3,   4],
         [12, 13, 14,5],
         [11, 16, 15,6],
         [10, 9, 8,  7]] #00,01,02,03,13,23,33,
list = []
list2 = []
for i in range(len(array[0])):
    list.append(array[0][i])
for i in range(len(array[0])):
    list.append(array[i][len(array[0])-1])
for i in reversed(range(len(array[0]))):
    list.append(array[len(array[0])-1][i])
for i in reversed(range(len(array[0]))):
    list.append(array[i][0])
for i in range(len(array[0])):
    if i%2==0:
        for b in reversed(range(len(array[0]))):
            list.append(array[i][b])
    else:
        for b in range(len(array[0])):
            list.append(array[i][b])
for i in list:
    if i not in list2:
        list2.append(i)






















# for i in range(3):
#     list.append(array[0][i])
# for i in range(1,3):
#     list.append(array[i][2])
# for i in reversed(range(2)):
#     list.append(array[2][i])
# for i in reversed(range(1,2)):
#     list.append(array[i][0])
# list.append(array[1][1])


