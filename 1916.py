import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
distance = [int(1e9) for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))

base, destination = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        d, city = heapq.heappop(q)
        if distance[city] < d:
            continue
        for next_city, next_d in bus[city]:
            new_d = next_d + d
            if distance[next_city] > new_d:
                distance[next_city] = new_d
                heapq.heappush(q,(new_d,next_city))


dijkstra(base)
print(distance[destination])