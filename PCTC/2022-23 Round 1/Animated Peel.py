string = input()
x = (len(string)//2)-1
peeled = string[x] + string[:x] + string[x+2:] + string[x+1]
print(peeled)
while peeled != string:
    peeled = peeled[x] + peeled[:x] + peeled[x+2:] + peeled[x+1]
    print(peeled)
    