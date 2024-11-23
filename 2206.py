from collections import deque

N,M = map(int,input().split())

maze = [[] for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = [1]

distance = [[[0,0]for _ in range(M)] for _ in range(N)]

for i in range(N):
    maze[i] = list(map(int,list(input())))


move = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(point):
    q = deque([point])
    while q:
        x,y,broke = q.popleft()
        for v,h in move:
            move_x , move_y = x+v,y+h
            if 0 <= move_x < N and 0 <= move_y < M:
                if maze[move_x][move_y] and not broke:
                    distance[move_x][move_y][1] = distance[x][y][0] + 1
                    visited[move_x][move_y][1] = True
                    q.append((move_x,move_y,1))

                elif not maze[move_x][move_y] and not visited[move_x][move_y][broke]:
                    distance[move_x][move_y][broke] = distance[x][y][broke] + 1
                    visited[move_x][move_y][broke] = True
                    q.append((move_x,move_y,broke))



bfs((0,0,0))


if distance[N-1][M-1][0] == 0 and distance[N-1][M-1][1] == 0:
    if N == M == 1:
        print(1)
    else:
        print(-1)
elif min(distance[N-1][M-1]) == 0:
    print(max(distance[N-1][M-1])+1)
else:
    print(min(distance[N-1][M-1])+1)



