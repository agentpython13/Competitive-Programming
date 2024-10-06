n = int(input())
if n == 0:
    print(8)
    exit()
elif n % 8 <= 4:
    print((n//8)*8)
else:
    print(((n//8)+1)*8)