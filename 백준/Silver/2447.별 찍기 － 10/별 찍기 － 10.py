def make_a_hole(n):
    if n==3:
        return ['***','* *','***']
    else:
        x=make_a_hole(n//3)
        y=[' '*(n//3)]*(n//3)
        a=[x[i]*3 for i in range(n//3)]
        b=[x[i]+y[i]+x[i] for i in range(n//3)]
        return a+b+a
n=int(input())
a=make_a_hole(n)
for i in range(n):
    print(''.join(a[i]))