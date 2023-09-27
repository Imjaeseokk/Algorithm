from collections import deque
n,m = map(int,input().split())

jump = [0 for _ in range(n+m)]
visit = [0 for _ in range(101)]
step = [0 for _ in range(101)]
for i in range(n+m):
    jump[i] = list(map(int,input().split()))

move = [0 for _ in range(101)]

for x,y in jump:
    move[x] = y


def bfs(init):
    q = deque([init])
    while q:

        locate, distance = q.popleft()
        if locate >= 100:
            print(distance)
            exit()

        for d in range(1,7):
            go = locate+d
            if (go <= 100) and not visit[go]:
                if move[go]:
                    go = move[go]
                    if not visit[go]:
                        visit[go] = True
                        q.append((go,distance+1))
                else:
                    visit[go] = True
                    q.append((go,distance+1))


visit[1] = True
bfs((1,0))

