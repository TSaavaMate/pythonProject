with open("Countries.txt","r")as file:
    a=file.readlines()
    b=[]
    for i in range(len(a)-1):
        letter = ""
        for element in a[i]:
            if element != " ":
                letter += element
            else:
                break

        b.append(letter)
with open("newFile","a") as file2:
    c=[]
    for item in range(len(b)):
        if item%7==0:
            file2.write(f'"{b[item]}",\n')
        else:
            file2.write(f'"{b[item]}",')
