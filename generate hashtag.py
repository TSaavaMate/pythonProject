def generate_hashtag(s):
    output = "#"
    for i in s.split(" "):
        output += i.capitalize()
    return output


print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))  # CodewarsIsNice
