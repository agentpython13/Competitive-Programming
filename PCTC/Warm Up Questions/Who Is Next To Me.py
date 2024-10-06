string = input()
letters = []
for letter in string:
    x = letter+'me'
    y = 'me'+letter
    if x in string or y in string:
        letters.append(letter)
l = list(set(letters))
print("".join(l))