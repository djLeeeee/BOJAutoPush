stack = []
for i in range(1, 6):
    if 'FBI' in input():
        stack.append(i)
print(*stack if stack else ['HE', 'GOT', 'AWAY!'])
