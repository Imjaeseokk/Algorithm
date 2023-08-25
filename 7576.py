from collections import deque

m,n=map(int,input().split())
tomato_box = [[] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
zero_cnt = 0
for box_row in range(n):
    tomato_box[box_row] = list(map(int,input().split()))
    zero_cnt += tomato_box[box_row].count(0)

move = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(ini,end_day,z_cnt):
    q = deque(ini)
    while q:
        tx,ty,day = q.popleft()
        visit[tx][ty] = 1
        for mx,my in move:
            cx = tx + mx
            cy = ty + my
            if (cx >= 0 and cx < n) and (cy >= 0 and cy < m):
                if not visit[cx][cy]:
                    if not tomato_box[cx][cy]:
                        z_cnt -=1
                        tomato_box[cx][cy] = 1
                        visit[cx][cy] = 1
                        q.append((cx,cy,day+1))
                        end_day = max(day+1,end_day)
    if z_cnt == 0:
        return end_day
    else:
        return -1

day = 0
end_day=0
start_t = []
for x in range(n):
    for y in range(m):
            if not visit[x][y] and tomato_box[x][y] == 1:
                start_t.append((x,y,day))
print(bfs(start_t,end_day,zero_cnt))