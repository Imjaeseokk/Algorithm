import sys

n,m = map(int,input().split())

def find(x):
    if x != reps[x]:
        reps[x] = find(reps[x])
    return reps[x]

def union(x,y):
    rep1 = find(x)
    rep2 = find(y)
    reps[rep2] = rep1

reps = [i for i in range(n+1)]
for j in range(m):
    func,a,b = map(int,sys.stdin.readline().split())
    if func:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)


