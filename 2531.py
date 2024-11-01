N, d, k, c = map(int, input().split())

sushis = []
for i in range(N):
    sushis.append(str(input()))

sushis.extend(sushis[:k - 1])

ate = []
for j in range(N):
    sushi = set(sushis[j:j + k].copy())
    sushi.add((str(c)))
    if not ate or len(ate[-1]) <= len(sushi):
        ate.append(sushi)
print(len(max(ate,key = lambda x:len(x))))