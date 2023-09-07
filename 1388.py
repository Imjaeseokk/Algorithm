from collections import deque

n,m = map(int,input().split())
floor = [[] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
for f in range(n):
    floor[f] = list(input())

xd = [(1,0),(-1,0)]
yd = [(0,1),(0,-1)]

def bfs(ini,s):
    q = deque([ini])
    while q:
        ix,iy = q.popleft()
        if s == "-":
            for dx,dy in yd:
                nx = ix + dx
                ny = iy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visit[nx][ny]:
                        if floor[nx][ny] == s:
                            q.append((nx,ny))
                            visit[nx][ny] = 1
        else:
            for dx,dy in xd:
                nx = ix + dx
                ny = iy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visit[nx][ny]:
                        if floor[nx][ny] == s:
                            q.append((nx,ny))
                            visit[nx][ny] = 1
total = 0
for x in range(n):
    for y in range(m):
        if not visit[x][y]:
            visit[x][y] = 1
            bfs((x,y),floor[x][y])
            total += 1

print(total)