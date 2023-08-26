from collections import deque

m,n,h = map(int,input().split())

t_map = [[[]for _ in range(n)]for _ in range(h)]
none_tomato = 0
tomato = []
for i in range(h):
    for j in range(n):
        t_map[i][j] = list(map(int,input().split()))
        none_tomato += t_map[i][j].count(0)
        for k in range(m):
            if t_map[i][j][k]==1:
                tomato.append((i,j,k))


# moving up down left right forw back
dir = [[1,0,0],[-1,0,0],[0,0,-1],[0,0,1],[0,1,0],[0,-1,0]]

def bfs(t):
    end_day = 0
    tomato_cnt = 0
    q = deque(t)
    while q:
        i,j,k = q.popleft()
        for dz,dy,dx in dir:
            z = i + dz
            y = j + dy
            x = k + dx
            if 0 <= z < h and 0 <= y < n and 0 <= x < m:
                if not t_map[z][y][x]:
                    t_map[z][y][x] = t_map[i][j][k] + 1
                    tomato_cnt +=1
                    q.append((z,y,x))
                    end_day = max(end_day,t_map[z][y][x])

    return end_day, tomato_cnt


end_day,tomato_cnt = bfs(tomato)
end_day = max(end_day-1,0)

if tomato_cnt == none_tomato:
    print(end_day)
else:
    print(-1)