from math import floor

d, h, w = map(int, input().split())
r = (h * h + w * w) ** 0.5
print(floor(h * d / r), floor(w * d / r))
