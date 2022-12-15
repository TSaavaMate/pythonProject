def move_zeros(lst):
    for i in range(lst.count(0)):
        lst.remove(0)
        lst.append(0)
    return lst
print(move_zeros([1,0,0,0,0,0,4,7,0]))