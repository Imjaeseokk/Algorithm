import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())

relation = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)

arrive = False

def dfs(i,length):
    global arrive
    visited[i] = True
    if length == 5:
        arrive = True
        return
    for next in relation[i]:
        if not visited[next]:
            dfs(next,length+1)
            visited[next] = False

for init in range(N):
    visited = [0 for _ in range(N + 1)]
    dfs(init,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

