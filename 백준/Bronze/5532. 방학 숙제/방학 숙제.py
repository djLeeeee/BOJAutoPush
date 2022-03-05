from math import ceil

a = [int(input()) for _ in range(5)]
print(a[0] - max(ceil(a[1] / a[3]), ceil(a[2] / a[4])))
