from collections import deque
n = int(input())

rgb_paint= [[]for _ in range(n)]
rb_paint = [[]for _ in range(n)]
for p in range(n):
    rgb = input()
    rgb_paint[p] = list(rgb)
    rb_paint[p] = list(rgb.replace("G","R"))

paints = [rgb_paint,rb_paint]

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(ini,c,paint):
    q = deque([ini])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and paint[nx][ny] == c:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    pass


result = []
for p in paints:
    cnt = 0
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visit[x][y]:
                visit[x][y] = 1
                color = p[x][y]
                bfs((x,y),color,p)
                cnt +=1
    result.append(cnt)
print(" ".join(map(str,result)))