def market_cap(filename):
    with open("stocks","r") as file:
        text=file.readlines()
        properlist=[]
        for row in text:
            try:
                if float(row.split()[1]) < float(600):
                    properlist.append(row)
            except ValueError:
                continue
    with open(filename,"a") as file2:
        for i in properlist:
            file2.write(i)
market_cap("testfile")
