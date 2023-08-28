from collections import deque

m,n = map(int,input().split())

canvas = [[]for _ in range(m)]
visit = [[0 for _ in range(n)]for _ in range(m)]

for c in range(m):
    canvas[c] = list(map(int,input().split()))


d = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(start):
    q = deque([start])
    area = 1
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny] and canvas[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    area += 1

    return area


cnt = 0
result = [0]
for i in range(m):
    for j in range(n):
        if not visit[i][j] and canvas[i][j]:
            visit[i][j] = 1
            cnt += 1
            result.append(bfs((i,j)))
print(cnt, max(result),sep = "\n")