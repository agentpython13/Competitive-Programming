total = 0
count = 0
for repeat in range(100):
    num = int(input())
    total += num
    count += 1
    if total == 20:
        print(count)
        exit()
    elif total > 20:
        total = 0
    