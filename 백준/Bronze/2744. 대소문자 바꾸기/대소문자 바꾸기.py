ans = ''
target = input()
for c in target:
    if 'a' <= c <= 'z':
        ans += c.upper()
    else:
        ans += c.lower()
print(ans)