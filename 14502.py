from collections import deque

N,M = map(int,input().split())

visited = [[0 for _ in range(M)] for _ in range(N)]
move = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(visited):
    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue = deque([(i,j)])
                while queue:
                    x,y = queue.popleft()
                    for mx,my in move:
                        nx = x + mx
                        ny = y + my
                        if (0 <= nx < N) and (0 <= ny < M):
                            if (not visited[nx][ny]) and (not lab[nx][ny]):
                                visited[nx][ny] = True
                                queue.append((nx,ny))
                                cnt +=1

    result = max(result,safe-3-cnt)



lab = [[] for _ in range(N)]
safe = 0
for i in range(N):
    lab[i] = list(map(int,input().split()))
    safe += lab[i].count(0)
result = 0

def make_walls(count):
    if count == 3:
        visited = [[0 for _ in range(M)] for _ in range(N)]
        bfs(visited)
        # print(result)
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_walls(count+1)
                lab[i][j] = 0

make_walls(0)
print(result)
