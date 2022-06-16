from sys import stdin as s

def cut_line(t, h):
    result = 0
    for i in t:
        result += i // h
    return result

num, wanted = map( int, s.readline().split() )

line = []

for _ in range(num):
    line.append(int(s.readline()))

start = 0
end = 2 ** 31
n = 1
r = False

while end - start > 1:
    length = (start + end) // 2
    if cut_line(line, length) >= wanted:
        start = length
    else:
        end = length

if cut_line(line, end) < wanted:
    print(start)
else:
    print(end)
