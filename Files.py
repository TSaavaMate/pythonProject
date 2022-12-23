
with open("Nameofnewtextfile","r") as File1:
    list=File1.readlines()
    for line in list:
        line="".join(line.split(";"))
        with open("newFile","a") as File2:
            File2.write(line[0:15]+"\n")
