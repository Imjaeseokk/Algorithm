from collections import deque

n = int(input())
mesh = [[] for _ in range(n)]
rain_max = 0
for i in range(n):
    mesh[i] = list(map(int,input().split()))
    rain_max = max(rain_max,max(mesh[i]))

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(ix,iy,h):
    q = deque([(ix,iy)])
    visit[ix][iy] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    if mesh[nx][ny] > h:
                        q.append((nx,ny))
result = 0
for height in range(rain_max):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if not visit[j][k] and mesh[j][k] > height:
                bfs(j,k,height)
                cnt +=1
    result = max(cnt,result)
print(result)