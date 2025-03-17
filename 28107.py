import heapq

N, M = map(int,input().split())

guest = [0 for _ in range(N)]
sushi_guest = [[] for _ in range(200001)]

for i in range(N):
    orders = list(map(int,input().split()))
    k = orders[0]
    sushi_order = orders[1:]

    for sushi in sushi_order:
        sushi_guest[sushi].append(i)

sushi_cooked = list(map(int,input().split()))
for sc in sushi_cooked:
    hq = sushi_guest[sc]
    if not hq:
        continue
    g = heapq.heappop(hq)
    guest[g] += 1

print(*guest)