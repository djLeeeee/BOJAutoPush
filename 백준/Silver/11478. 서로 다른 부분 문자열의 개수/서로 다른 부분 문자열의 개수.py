from sys import stdin

input = stdin.readline

target = input().rstrip()
l = len(target)
my_set = set()
for i in range(l):
    for j in range(i, l):
        my_set.add(target[i:j + 1])
print(len(my_set))