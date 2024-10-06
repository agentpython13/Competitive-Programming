friends = [10,10,10,10,10]
for num in range(5):
    x = int(input())
    if num == 4:
        friends[4] -= x
        friends[0] += x
    else:
        friends[num] -= x
        friends[num+1] += x
print(max(friends))