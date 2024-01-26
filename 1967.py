import sys
sys.setrecursionlimit(10**9)

N = int(input())

tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b,w = map(int,input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))


visited = [-1 for _ in range(N+1)]
def dfs(start,d):
    for i,w in tree[start]:
        if visited[i] == -1:
            visited[i] = d + w
            dfs(i,d+w)

visited[1] = 0
dfs(1,0)
d1 = visited.index(max(visited))

visited = [-1 for _ in range(N+1)]
visited[d1] = 0
dfs(d1,0)

print(max(visited))