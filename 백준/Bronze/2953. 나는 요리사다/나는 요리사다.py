ans = 0
mx = 0
for i in range(1, 6):
    s = sum(map(int, input().split()))
    if s > mx:
        mx = s
        ans = i
print(ans, mx)