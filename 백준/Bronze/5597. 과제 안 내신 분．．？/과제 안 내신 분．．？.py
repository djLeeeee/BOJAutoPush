a = set(range(1, 31))
for _ in range(28):
    a.remove(int(input()))
a = list(a)
a.sort()
print(*a, sep='\n')