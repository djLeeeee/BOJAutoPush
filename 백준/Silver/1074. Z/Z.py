from sys import stdin as s

N, x, y = map(int, s.readline().split())

def a(N, xx, yy):
	if N == 0:
		return 0     
	return 2 * (xx % 2) + (yy % 2) + 4 * a(N - 1, int(xx / 2), int(yy / 2))

print(a(N, x, y))
