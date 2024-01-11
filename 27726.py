n = int(input())
m = list(map(int,input().split()))
groups = [[i for i in range(n+1)] for _ in range(3)]
agree = [[] for _ in range(3)]
def find(x,idx):
    if x != groups[idx][x]:
        groups[idx][x] = find(groups[idx][x],idx)
    return groups[idx][x]

def union(x,y,idx):
    rep1 = find(groups[idx][x],idx)
    rep2 = find(groups[idx][y],idx)
    if rep1 < rep2:
        groups[idx][rep2] = rep1
    else:
        groups[idx][rep1] = rep2

for j in range(3):
    for k in range(1,m[j]+1):
        a,b = map(int,input().split())
        x = max(a,b)
        y = min(a,b)
        agree[j].append([y,x])


for j in range(3):
    for x,y in sorted(agree[j]):
        union(x,y,j)


groupsCopy = [[i for i in range(n+1)] for _ in range(3)]

for j in range(3):
    for k in range(1,n+1):
        groupsCopy[j][k] = find(k,j)

group = []
for i in range(1,n+1):
    ggg = []
    for j in range(3):
        ggg.append(groupsCopy[j][i])
    group.append(tuple(ggg))


d = dict.fromkeys(group)

for i in range(n):
    if not d[group[i]]:
        d[group[i]] = [i+1]
    else:
        d[group[i]].append(i+1)

cnt = 0
result = []


for gnum,member in d.items():
    if len(member) > 1:
        cnt += 1
        result.append(sorted(member))

print(cnt)
for r in result:
    print(*r)
