import sys
sys.setrecursionlimit(10000)
def section(g,a,b,rgb):
    if 0<=a<N and 0<=b<N and g[b][a]==rgb:
        g[b][a]=0
        section(g,a-1,b,rgb)
        section(g,a,b-1,rgb)
        section(g,a+1,b,rgb)
        section(g,a,b+1,rgb)
N=int(sys.stdin.readline())
RGB=[]
RB=[]
for _ in range(N):
    x=sys.stdin.readline().rstrip()
    y=x.replace('G', 'R')
    RGB.append([i for i in x])
    RB.append([j for j in y])
result1=0
result2=0
for i in range(N):
    for j in range(N):
        if RGB[i][j]:
            section(RGB,j,i,RGB[i][j])
            result1+=1
        if RB[i][j]:
            section(RB,j,i,RB[i][j])
            result2+=1
print(result1)
print(result2)