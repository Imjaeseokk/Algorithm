from collections import deque

n = int(input())
graph = [[]for _ in range(n)]
network = [[]for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

def bfs(start,end):
    q = deque([start])
    while q:
        init = q.popleft()
        for node in network[init]:
            if not visit[node-1]:
                visit[node-1] = 1
                if node-1 == end:
                    return 1
                q.append(node-1)
    return 0



for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            network[y].append(x+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        visit = [0 for _ in range(n)]
        print(bfs(i-1,j-1), end = " ")
    print()