import sys
input = sys.stdin.readline

V,E = map(int,input().split())

edges = []
heads = [i for i in range(V+1)]
for i in range(E):
    edges.append(tuple(map(int,input().split())))


def find(x):
    if heads[x] != x:
        heads[x] = find(heads[x])
    return heads[x]


def union(x,y):
    rep1 = find(x)
    rep2 = find(y)
    heads[rep2] = rep1

edges = sorted(edges, key = lambda x:x[2])
weight = 0

for x,y,c in edges:
    if find(x) == find(y):
        continue
    else:
        weight += c
        union(x,y)

print(weight)