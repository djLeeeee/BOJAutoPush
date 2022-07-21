p = list(map(int, input().split()))
x, *_ = map(int, input().split())
print(p.index(x) + 1 if x in p else 0)