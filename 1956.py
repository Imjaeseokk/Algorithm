V,E = map(int,input().split())

town = [[int(1e9) for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    town[a][b] = c


for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            town[i][j] = min(town[i][j],town[i][k] + town[k][j])

result = int(1e9)
for i in range(1,V+1):
    result = min(result, town[i][i])

if result == int(1e9):
    print(-1)
else:
    print(result)