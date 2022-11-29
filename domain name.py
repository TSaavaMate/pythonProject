def pig_it(text):
    text = text.split(" ")
    for i in range(len(text)):
        if len(text[i])==1 and text[i].isalpha() :
            text[i] +=  "ay"
        else:
            text[i] += text[i][0] + "ay"
            text[i] = text[i][1:]
    text = " ".join(text)
    return text


print(pig_it('Pig latin is cool'))
