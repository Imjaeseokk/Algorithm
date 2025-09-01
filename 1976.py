N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
group = [-1 for _ in range(N+1)]


def find(u):
    if group[u] < 0:
        return u
    return find(group[u])

def union(u,v):
    gu = find(u)
    gv = find(v)

    if gu == gv:
        return
    elif gu < gv:
        group[gv] = gu
    else:
        group[gu] = gv


for i in range(1,N+1):
    for idx, j in enumerate(list(map(int,input().split()))):
        if j:
            union(i,idx+1)


city = list(map(int,input().split()))
p_city = [find(p) for p in city]

if len(set(p_city)) == 1:
    print("YES")

else:
    print("NO")

