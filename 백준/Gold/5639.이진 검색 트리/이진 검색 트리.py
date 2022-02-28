import sys
sys.setrecursionlimit(10 ** 6)

array = []
while True:
    try:
        array.append(int(input()))
    except EOFError:
        break


def transform(start, end):
    if start > end:
        return
    for i in range(start, end + 1):
        if array[i] > array[start]:
            break
    else:
        i = end + 1
    transform(start + 1, i - 1)
    transform(i, end)
    print(array[start])


transform(0, len(array) - 1)
