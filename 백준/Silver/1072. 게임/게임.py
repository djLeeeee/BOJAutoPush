x, y = map(int, input().split())
z = int(y * 100 / x)
ex = -1
start = 1
end = x
while start <= end:
    mid = (start + end) // 2
    if int((y + mid) * 100 / (x + mid)) != z:
        ex = mid
        end = mid - 1
    else:
        start = mid + 1
print(ex)
