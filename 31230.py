import sys
import heapq
import math

input = sys.stdin.readline

N,M,A,B = map(int,input().split())

dist = [math.inf for i in range(N+1)]
info = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    info[a].append((b,c))
    info[b].append((a,c))

def bfs(city):
    q = []
    heapq.heappush(q,(0,city))
    dist[city] = 0
    while q:
        d,now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in info[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dist[A] = 0
bfs(A)
distA = dist[:]

distance = distA[B]

dist = [math.inf for i in range(N+1)]
visit = [0 for _ in range(N+1)]
dist[B] = 0
bfs(B)
distB = dist[:]

result = []
for node in range(1,N+1):
    if distA[node] + distB[node] == distance:
        result.append(node)

# print(distA)
# print(distB)

print(len(result))
print(*result)
