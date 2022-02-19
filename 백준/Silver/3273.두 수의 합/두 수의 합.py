from sys import stdin as s

n = int(s.readline())
array = list(map(int, s.readline().split()))
array.sort()
x = int(s.readline())
start = 0
end = n - 1
ans = 0
while start < end:
    a = array[start] + array[end]
    if a > x:
        end -= 1
    elif a < x:
        start += 1
    else:
        ans += 1
        start += 1
        end -= 1
print(ans)
