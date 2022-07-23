n = int(input())
n = (n // 100) * 100
m = int(input())
for i in range(100):
    if not (n + i) % m:
        ans = '0' + str(i)
        break
print(ans[-2:])
