def romanToInt(s):
    count=4*s.count("IV")+9*s.count("IX")+40*s.count("XL")+90*s.count("XC")+400*s.count("CD")+900*s.count("CM")
    s=s.replace("IV","").replace("IX","").replace("XL","").replace("XC","").replace("CD","").replace("CM","")
    return count+s.count("I")+5*s.count("V")+10*s.count("X")+50*s.count("L")+100*s.count("C")+500*s.count("D")+1000*s.count("M")
print(romanToInt("MCMXCIV"))
# IV
# IX
# XL
# XC
# CD
# CM