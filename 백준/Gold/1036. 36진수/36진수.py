n = int(input())
my_dic = {chr(ord('A') + i): 10 + i for i in range(26)}
for i in range(10):
    my_dic[str(i)] = i
table = [0] * 36
ans = 0
for _ in range(n):
    target = input()
    for i in range(len(target)):
        j = my_dic[target[-(i + 1)]]
        table[j] += 36 ** i
        ans += j * (36 ** i)
ex = []
for i in range(36):
    ex.append((35 - i) * table[i])
ex.sort()
k = int(input())
if k:
    ans += sum(ex[-k:])
result = ''
while ans > 0:
    r = ans % 36
    if r < 10:
        now = str(r)
    else:
        now = chr(ord('A') + r - 10)
    result += now
    ans //= 36
if result:
    print(result[::-1])
else:
    print(0)