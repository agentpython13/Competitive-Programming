x = int(input())
y = int(input())

for row in range(10):
    if row == y:
        print("#"*x+"X"+"#"*(10-(x+1)))
    else:
        print("##########")