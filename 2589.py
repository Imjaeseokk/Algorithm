from collections import deque

r,c = map(int,input().split())
m = [[]for _ in range(r)]
pt = [[0 for _ in range(c)]for _ in range(r)]



for row in range(r):
    m[row] = list(input())

d = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(ini):
    q = deque([ini])
    cnt_list = [0]
    while q:
        ix,iy, cnt = q.popleft()
        for dx,dy in d:
            nx = dx + ix
            ny = dy + iy
            if 0 <= nx < r and 0 <= ny < c and not visit[nx][ny]:
                if m[nx][ny] == "L":
                    visit[nx][ny] = 1
                    q.append((nx,ny,cnt+1))
                    cnt_list.append(cnt+1)
    return cnt_list



mx = [0]
for x in range(r):
    for y in range(c):
        visit = [[0 for _ in range(c)] for _ in range(r)]
        if m[x][y] == "L":
            visit[x][y] = 1
            mx.append(max(bfs((x,y,0))))

print(max(mx))


