dict={5:{6:3}, "hi":{18:12},"no":{100:"go"}, 50:{2:20}}
def improvedict(dict):
    listelements=[]
    for values in dict.values():
        for element1,element2 in values.items():
            listelements.append(element1)
            listelements.append(element2)
    try:
        return max(listelements)
    except TypeError:
        for item in listelements:
            if type(item)==str:
                listelements.remove(item)
        return max(listelements)

print(improvedict(dict))