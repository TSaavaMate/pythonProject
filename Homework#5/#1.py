def gcd(a,b):
    for i in reversed(range(min(a,b) + 1)):
        if a % i == 0 and b % i == 0:
            return i
def gcd1(x,y):
  return x if y == 0 else gcd1(y, x % y)

print(gcd(6,12))
print(gcd(7,13))
print(gcd(6,16))
print(gcd(6,128))
print(gcd(19,7))
print(gcd(3912,50))
print(gcd(1235430,753310))