from collections import deque

n,m = map(int,input().split())

ind = [0 for _ in range(n)]
outd = [[] for _ in range(n)]
visit = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    outd[a-1].append(b)
    ind[b-1] += 1

def topo(start):
    q = deque(start)
    arr = []
    while q:
        base = q.popleft()
        visit[base] = True
        arr.append(base)
        for k in outd[base-1]:
            ind[k-1] -= 1
            if ind[k-1] == 0:
                q.append(k)
    print(*arr)

start = []
for j in range(n):
    if ind[j] == 0:
        start.append(j+1)

topo(start)
