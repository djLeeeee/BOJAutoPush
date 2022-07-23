n = int(input())
arr = list(map(int, input().split()))
my_arr = [(arr[i], i) for i in range(n)]
my_arr.sort()
ans = [0] * n
for i in range(n):
    ans[my_arr[i][1]] = i
print(*ans)
