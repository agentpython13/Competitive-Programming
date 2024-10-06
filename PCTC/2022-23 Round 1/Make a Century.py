a = int(input())
b =int(input())
nums = [abs(100-(a+b)),abs(100-(a-b)),abs(100-(b-a))]
print(min(nums))