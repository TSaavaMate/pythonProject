class Fraction:
    def __init__(self, num=3,den=5):
        self.num=num
        self.den=den
    def adD(self, r):
        self.num+=self.num+2
        self.den+=self.den+4
        return f'{self.num}/{self.den}'
F1=Fraction(2,9)
print(F1.adD(5))

