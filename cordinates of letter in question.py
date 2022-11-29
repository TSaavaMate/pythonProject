def findletter(s, l):
    res = []
    count = 0
    s = s.split(" ")
    for i in range(len(s)):
        for a in range(len(s[i])):
            if s[i][a] == l:
                res.append(i)
                res.append(a)
                count += 1
                if count > 0:
                    print(res)
                    res = []
    if count == 0:
        print(-1)


findletter("winadadeba stringi da sityva", "a")
