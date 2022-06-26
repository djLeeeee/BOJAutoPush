def f(a, b, c):
    return 3600 * a + b * 60 + c


def rf(t):
    h = t // 3600
    h = '0' + str(h)
    h = h[-2:]
    t %= 3600
    m = t // 60
    m = '0' + str(m)
    m = m[-2:]
    t %= 60
    t = '0' + str(t)
    t = t[-2:]
    return f'{h}:{m}:{t}'


t1 = f(*map(int, input().split(":")))
t2 = f(*map(int, input().split(":")))
if t1 < t2:
    print(rf(t2 - t1))
else:
    print(rf(t2 - t1 + 24 * 3600))
