price = float(input())
change = int(input())

if price < 10:
    new = round((price * (100-change))/100, 2)
    if new < 1:
        if str(price)[-1] != "0":
            price = str(price) + '0'
        if str(price)[len(str(price))-2] == ".":
            price = str(price) + '0' 
        print(f"${price}")
    else:
        if str(new)[-1] != "0":
            new = str(new) + '0'
        if str(new)[len(str(new))-2] == ".":
            new = str(new) + '0'
        print(f"${new}")
else:
    new = round((price * (100+change))/100, 2)
    if new > 100:
        if str(price)[-1] != "0":
            price = str(price) + '0'
        if str(price)[len(str(price))-2] == ".":
            price = str(price) + '0' 
        print(f"${price}")
    else:
        if str(new)[-1] != "0":
            new = str(new) + '0'
        if str(new)[len(str(new))-2] == ".":
            new = str(new) + '0' 
        print(f"${new}")
