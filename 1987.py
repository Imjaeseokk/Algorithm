from collections import deque

r, c = map(int, input().split())

board = [[] for _ in range(r)]
for i in range(r):
    board[i] = list(input())

visit = [[0 for _ in range(c)] for _ in range(r)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def backTrack(route, x, y,dist):
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:
            char = (board[nx][ny])
            if not char in route:
                route.add(char)
                dist = backTrack(route, nx, ny,dist)
                if len(route)>=2:
                    route.remove(board[nx][ny])

    dist = max(dist,len(route))
    return dist


dist = backTrack({board[0][0]}, 0, 0,0)
print(dist)

