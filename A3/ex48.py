
directions = ("south", "north", "west", "east", "center")
verbs = ("go", "kill", "eat", "run", "tell", "shoot", "sing", "love")
stops = ("the", "in", "of", "to", "via")
nouns = ("bear", "princess", "MissHei", "tiger", "dragon")

stuff = input("> ")
words = stuff.split()
sentence = []

for word in words:
    if word in directions:
        sentence.append(word)

    elif word in verbs:
        sentence.append(word)

    elif word in stops:
        sentence.append(word)

    elif word in nouns:
        sentence.append(word)


if not sentence:
    print("输入错误！")

else:
    print(sentence)
