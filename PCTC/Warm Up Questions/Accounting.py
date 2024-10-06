positive = True
total = 0
count = 0

while positive:
    x = int(input())
    if x < 0:
        positive = False
    else:
        total += x
        if x > 100:
            count += 1
print(total)
print(count)
    
    