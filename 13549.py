from collections import deque

n,k = map(int,input().split())
visit = [0 for _ in range(1000001)]
sec = [0 for _ in range(1000001)]

def bfs(l):
    q = deque(l)
    output = []
    while q:
        i = q.popleft()
        if (i*2) < 1000001 and not visit[i*2]:
            visit[i*2] = 1
            sec[i*2] = sec[i]
            output.append(i*2)
        if (i-1) < 1000001 and not visit[i-1] :
            visit[i-1] = 1
            sec[i-1] = sec[i]+1
            output.append(i-1)
        if  (i+1) < 1000001 and not visit[i+1]:
            visit[i+1] = 1
            sec[i+1] = sec[i] + 1
            output.append(i+1)

    return output

pts = [n]
while True:
    if k in pts:
        print(sec[k])
        break
    pts = bfs(pts)
