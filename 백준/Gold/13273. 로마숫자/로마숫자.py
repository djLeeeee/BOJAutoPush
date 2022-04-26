from sys import stdin

input = stdin.readline


def trans(num):
    order = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]
    result = ''
    for char, value in order:
        result += char * (num // value)
        num %= value
    return result


def trans2(string):
    change = [('CM', 'DCD'), ('CD', 'C' * 4), ('XC', 'LXL'), ('XL', 'X' * 4), ('IX', 'VIV'), ('IV', 'I' * 4)]
    for x, y in change:
        string = string.replace(x, y)
    result = 0
    order = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(string)):
        result += order[string[i]]
    return result


for _ in range(int(input())):
    z = input()
    try:
        print(trans(int(z)))
    except ValueError:
        print(trans2(z.strip()))
