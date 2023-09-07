from collections import deque

n,m = map(int,input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
safe_dis = [[0 for _ in range(m)] for _ in range(n)]
sea = [[]for _ in range(n)]
for s in range(n):
    sea[s] = list(map(int,input().split()))


d = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]


def bfs(ini):
    dis = 0
    output = 0
    q = deque([ini])
    while q:
        ix,iy = q.popleft()
        for dx,dy in d:
            nx = ix + dx
            ny = iy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    safe_dis[nx][ny] = safe_dis[ix][iy] + 1
                    q.append((nx,ny))
                    if sea[nx][ny]:
                        return safe_dis[nx][ny]
    return output

result_list = []
for x in range(n):
    for y in range(m):
        if not sea[x][y]:
            visit = [[0 for _ in range(m)] for _ in range(n)]
            safe_dis = [[0 for _ in range(m)] for _ in range(n)]
            visit[x][y] = 1

            result_list.append(bfs((x,y)))

print(max(result_list))

