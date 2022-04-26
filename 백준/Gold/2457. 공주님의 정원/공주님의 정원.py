from sys import stdin

input = stdin.readline

n = int(input())
flower = [tuple(map(int, input().split())) for _ in range(n)]
flower.sort()
start = (1, 1)
end = (3, 1)
ans = 0
pointer = 0
while pointer < n and end <= (11, 30):
    if end < flower[pointer][:2]:
        break
    max_end = end
    while pointer < n and flower[pointer][:2] <= end:
        max_end = max(max_end, flower[pointer][2:])
        pointer += 1
    ans += 1
    end = max_end
if end > (11, 30):
    print(ans)
else:
    print(0)
