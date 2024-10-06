profit = 0
current = int(input())
for x in range(30):
    price = int(input())
    if price >= current:
        profit += price-current
        current = price
    else:
        profit += price-current
        print(profit)
        exit()
    