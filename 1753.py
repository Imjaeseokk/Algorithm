import heapq

INF = int(1e9)
V,E = map(int,input().split())
root = int(input())
graph = [[]for _ in range(V+1)]
visit = [0 for _ in range(V+1)]
distance = [(1e9) for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))


# print(graph)
# print(weight)

def daik(here):
    q = []
    heapq.heappush(q,(0,here))
    distance[here] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            wDist = dist + i[1]
            if wDist < distance[i[0]]:
                distance[i[0]] = wDist
                heapq.heappush(q,(wDist,i[0]))


visit = [0 for _ in range(V + 1)]
daik(root)

# print(distance)

for d in range(1,V+1):
    if distance[d] == INF:
        print("INF")
        continue
    print(distance[d])