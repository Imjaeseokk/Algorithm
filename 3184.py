from collections import deque

r, c = map(int, input().split())

field = [[] for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]

for f in range(r):
    field[f] = list(input())

d = [(0,0),(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(ini):
    q = deque([ini])
    sheep = 0
    wolf = 0
    while q:
        fx, fy = q.popleft()
        for dx,dy in d:
            nx = fx + dx
            ny = fy + dy
            if 0 <= nx < r and 0 <= ny < c:
                if (field[nx][ny] != "#") and (not visit[nx][ny]):
                    if field[nx][ny] == "o":
                        sheep += 1
                    if field[nx][ny] == "v":
                        wolf += 1
                    visit[nx][ny] = 1
                    q.append((nx, ny))
    return sheep, wolf

total_s = 0
total_w = 0
for x in range(r):
    for y in range(c):
        if not visit[x][y] and field[x][y] != "#":
            s, w = bfs((x, y))
            if s > w:
                total_s += s
            else:
                total_w += w

print(total_s, total_w)