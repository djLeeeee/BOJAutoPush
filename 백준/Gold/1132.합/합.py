from sys import stdin as s

n = int(s.readline())
my_dict = {}
started = set()
for i in range(10):
    my_dict[chr(ord('A') + i)] = 0
for _ in range(n):
    x = s.readline().strip()
    length = len(x)
    started.add(x[0])
    for j in range(length):
        my_dict[x[j]] += 10 ** (length - j - 1)
my_list = []
for key, value in my_dict.items():
    if value:
        my_list.append([value, key])
my_list.sort()
ans = 0
if len(my_list) == 10:
    for i in range(10):
        if my_list[i][1] not in started:
            zero_idx = i
            break
    j = 1
    for k in range(10):
        if k == zero_idx:
            continue
        else:
            ans += j * my_list[k][0]
            j += 1
else:
    for i in range(len(my_list)):
        ans += (9 - i) * my_list[- i - 1][0]
print(ans)
