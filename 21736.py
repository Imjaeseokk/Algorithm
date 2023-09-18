from collections import deque

n,m = map(int,input().split())
campus = [[] for _ in range(n)]
visit = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    campus[i] = list(input())
    if "I" in campus[i]:
        DoYeon = (i,campus[i].index("I"))


d = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(ini):
    cnt = 0
    q = deque([ini])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    if campus[nx][ny] == "O":
                        q.append((nx,ny))
                    elif campus[nx][ny] == "P":
                        q.append((nx, ny))
                        cnt +=1
    if cnt:
        print(cnt)
    else:
        print("TT")


bfs(DoYeon)