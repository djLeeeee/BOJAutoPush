n = int(input())
nums = list(map(int, input().split())) + [0]
nums.sort()
m = int(input())
x, y = 0, 0
for i in range(n):
    if nums[i] < m < nums[i + 1]:
        x, y = m - nums[i], nums[i + 1] - m
        break
if x and y:
    print(x * y - 1)
else:
    print(0)