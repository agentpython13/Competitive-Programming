field1 = ["H", ".",".",".",".",".",".",".",".",".",".","|"]
field2 = ["H", ".",".",".",".",".",".",".",".",".",".","|"]

h1 = 0
h2 = 0

for num in range(22):
    x = int(input())
    if x == 0:
        if h1 == 0:
            field1[h1] = "|"
            field1[h1+1] = "H"
        else:
            field1[h1] = "."
            field1[h1+1] = "H"
        h1 += 1
    else:
        if h2 == 0:
            field2[h2] = "|"
            field2[h2+1] = "H"
        else:
            field2[h2] = "."
            field2[h2+1] = "H"
        h2 += 1
    if field1[11] == "H" or field2[11] == "H":
        f1 = ""
        f2=""
        print(f1.join(field1))
        print(f2.join(field2))
        exit()

        
        
            

