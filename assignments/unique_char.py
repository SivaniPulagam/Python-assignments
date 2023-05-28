myString = input()

uniqueChars = []

for ch in myString:
    if ch not in uniqueChars:
        uniqueChars.append(ch)

for ch in uniqueChars:
    print(ch, end="")