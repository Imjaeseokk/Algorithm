from collections import deque

tc = int(input())
result = [0 for _ in range(tc)]

d = [(0,0),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def bfs(start,end):
    q = deque([start])
    turn = 0
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < l and 0 <= ny < l:
                if not chess_map[nx][ny]:
                    chess_map[nx][ny] = chess_map[x][y] + 1
                    q.append((nx,ny))
                    if (nx,ny) == end:
                        turn = chess_map[nx][ny]-1
    return turn


for t in range(tc):
    l = int(input())                    # chess_map length
    chess_map = [[0 for _ in range(l)] for _ in range(l)]
    x,y = map(int,input().split())
    tx,ty = map(int,input().split())
    print(bfs((x,y),(tx,ty)))
