def first_non_repeating_letter(string):
    if len(string) == 0:
        return ""
    for i in string:
        if i.isupper():
            newstring = string.upper()
            if newstring.count(i) == 1:
                return i
        elif i.islower():
            newstring = string.lower()
            if newstring.count(i) == 1:
                return i
        elif i.isnumeric():
            if string.count(i) == 1:
                return i
        elif len(string) == 0:
            return ""
        elif not i.isalnum():
            if string.count(i) == 1:
                return i
    return ""


print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('abba'))
