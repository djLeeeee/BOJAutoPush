x=int;o,r=[input().split() for _ in range(x(input()))],''
while o:
    s,c,t=o.pop()
    if 'u' in s:
        while o and x(o[-1][-1])>=x(t)-x(c):o.pop()
    else:r = c + r
print(r)