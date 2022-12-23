def isprime(n):
    a=0
    for i in range(2,n):
        if n%i==0:
            a+=1
    return True if a==0 else False
print(isprime(111))
