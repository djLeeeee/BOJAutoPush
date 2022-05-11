from sys import stdin as s

n = int(s.readline())
my_dict = { }
for i in range(26):
    my_dict[chr(ord('A') + i)] = 0
for _ in range(n):
    x = s.readline().strip()
    l = len(x)
    for j in range(l):
        my_dict[ x[j] ] += 10 ** (l - j - 1)
my_list = list(my_dict.values())
my_list.sort(reverse = True)
ans = 0
for i in range(10):
    ans += (9 - i) * my_list [i]
print(ans)