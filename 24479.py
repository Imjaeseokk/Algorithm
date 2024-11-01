import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def dfs(R,i):
    visited[R] = i
    i += 1
    for c in graph[R]:
        if not visited[c]:
            i = dfs(c,i)

    return i

dfs(R,1)
for r in visited[1:]:
    print(r)
