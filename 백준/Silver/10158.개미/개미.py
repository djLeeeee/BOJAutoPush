from sys import stdin as s

w, h = map(int, s.readline().split())
x, y = map(int, s.readline().split())
t = int(s.readline())
x = x + t
y = y + t
xa = x // w
ya = y // h
xb = x % w
yb = y % h
if xa % 2:
    xb = w - xb
if ya % 2:
    yb = h - yb
print(xb, yb)