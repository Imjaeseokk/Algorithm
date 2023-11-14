from collections import deque

n,m = map(int,input().split())

inDegree = [0 for _ in range(n)]
outDegree = [[] for _ in range(n)]
visit = [0 for _ in range(n+1)]


for i in range(m):
    schedules = list(map(int,input().split()))
    for j in range(schedules[0]-1):
        a,b = schedules[j+1:j+3]
        inDegree[b-1] += 1
        outDegree[a-1].append(b)


def topo(start):
    q = deque(start)
    arr = []
    while q:
        base = q.popleft()
        visit[base] = True
        arr.append(base)
        for o in outDegree[base-1]:
            inDegree[o-1] -= 1
            if inDegree[o-1] == 0:
                q.append(o)
    if sum(visit) == n:
        print("\n".join(map(str,arr)))
    else:
        print(0)
start = []
for k in range(n):
    if inDegree[k] == 0:
        start.append(k+1)

topo(start)