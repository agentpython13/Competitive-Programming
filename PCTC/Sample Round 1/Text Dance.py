x = input()
dance = x
moves = ["<","+","&",">"]
current = moves.index(x)
while len(dance) != 8:
    current += 1
    if current > 3:
        current = 0
    dance += moves[current]
print(dance)
    
