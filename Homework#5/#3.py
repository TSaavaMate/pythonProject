def gcd(a,b):
    for i in reversed(range(min(a,b) + 1)):
        if a % i == 0 and b % i == 0:
            return i
def fun3(tuplee):
    list=[]
    for toupleinside in tuplee:
        if toupleinside[1][0]=="l":
            list.append(toupleinside[0])
    return tuple(list),gcd(min(list),max(list))
print(fun3(((20,"hi"),(40,"like"),(60,"lock"),(80,"look"))))