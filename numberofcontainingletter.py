def duplicate_count(text):
    text=text.lower()
    a = ("".join(set(text))).lower()
    c=0
    for i in a:
        b=text.count(i)
        if b>=2:
            c+=1
    return c
print(duplicate_count("abcdeaB"))

