def gcd(a,b):
    for i in reversed(range(min(a,b) + 1)):
        if a % i == 0 and b % i == 0:
            return i             #with for loop
def gcd1(x,y):
  return x if y == 0 else gcd1(y, x % y) #with recursion

print(gcd(6,12))
print(gcd(7,13))
print(gcd(6,16))
print(gcd1(6,128))
print(gcd1(19,7))
print(gcd1(3912,50))
print(gcd1(1235430,753310))
