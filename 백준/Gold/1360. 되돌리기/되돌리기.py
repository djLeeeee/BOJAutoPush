from sys import stdin

input = stdin.readline

n = int(input())
order = [[] for _ in range(n)]
for i in range(n):
    s, c, t = input().split()
    state = 0 if s == 'type' else 1
    if state:
        c = int(c)
    order[i] = [state, c, int(t)]
result = ''
while order:
    state, status, t = order.pop()
    if state:
        while order and order[-1][-1] >= t - status:
            order.pop()
    else:
        result = status + result
print(result)
