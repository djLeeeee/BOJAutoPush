order = {
    'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'RB': (1, -1), 'LB': (-1, -1), 'LT': (-1, 1)
}
p1, p2, n = input().split()
x, y = ord(p1[0]) - ord('A'), int(p1[1]) - 1
z, w = ord(p2[0]) - ord('A'), int(p2[1]) - 1
for _ in range(int(n)):
    dx, dy = order[input()]
    nx, ny = x + dx, y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == z and ny == w:
            nz, nw = z + dx, w + dy
            if 0 <= nz < 8 and 0 <= nw < 8:
                x, y = nx, ny
                z, w = nz, nw
        else:
            x, y = nx, ny
print(chr(ord('A') + x) + str(y + 1))
print(chr(ord('A') + z) + str(w + 1))
