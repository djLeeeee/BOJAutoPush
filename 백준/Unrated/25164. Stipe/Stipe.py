from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
person = [list(map(int, input().split())) + [-i] for i in range(1, n + 1)]
person.sort(reverse=True)
max_i = 0
for _, _, _, i in person[:m]:
    max_i = max(max_i, -i)
print(max_i - m)
