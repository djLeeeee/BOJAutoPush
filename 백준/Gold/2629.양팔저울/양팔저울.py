from sys import stdin as s

n = int(s.readline())
chuu = map(int, s.readline().split())
possible = {0}
for chu in chuu:
    new = set()
    for i in possible:
        new.add(abs(i - chu))
        new.add(abs(i + chu))
    possible = possible.union(new)
s.readline()
for j in s.readline().split():
    if int(j) in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
