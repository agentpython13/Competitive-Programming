names = []
for name in range(5):
    x = input()
    names.append(x)
if names.index("Ellie") == 0:
    print("1st")
elif names.index("Ellie") == 1:
    print("2nd")
elif names.index("Ellie") == 2:
    print("3rd")
elif names.index("Ellie") == 3:
    print("4th")
else:
    print("5th")
    