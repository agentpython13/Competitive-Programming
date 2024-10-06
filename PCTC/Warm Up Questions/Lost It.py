money = []
for cash in range(5):
    x = int(input())
    money.append(x)
num = int(input())
money[num-1] = 0
print(f"${sum(money)}")