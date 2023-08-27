from collections import deque

m,n,k = map(int,input().split())

mesh = [[1 for _ in range(n)]for _ in range(m)]
visit = [[0 for _ in range(n)]for _ in range(m)]
for i in range(k):
    lx,ly,rx,ry = map(int,input().split())
    for y in range(ly,ry):
        y = m-y-1
        for x in range(lx,rx):
            mesh[y][x] = 0

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(ini):
    area = 1
    q = deque([ini])
    while q:
        ix,iy = q.popleft()
        for dx,dy in d:
            nx = ix + dx
            ny = iy + dy
            if 0 <= nx < m and 0 <= ny < n:
                if not visit[nx][ny] and mesh[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    area+=1
    return area



cnt = 0
result = []
for jx in range(m):
    for jy in range(n):
        if not visit[jx][jy] and mesh[jx][jy]:
            visit[jx][jy] = 1
            result.append(bfs((jx,jy)))
            cnt +=1
print(cnt)
result.sort()
print(" ".join(map(str,result)))