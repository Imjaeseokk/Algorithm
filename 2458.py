N, M = map(int,input().split())

compare = [[int(1e9) for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    compare[a][b] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            compare[i][j] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            compare[i][j] = min(compare[i][j], compare[i][k] + compare[k][j])

degree = [0 for _ in range(N+1)]
for k in range(1,N+1):
    cnt_row = 0
    cnt_column = 0
    for i in range(1,N+1):
        if not compare[k][i] in [int(1e9),0]:
            cnt_row += 1
        if not compare[i][k] in [int(1e9),0]:
            cnt_column += 1

    degree[k] = cnt_row+cnt_column

result = 0
for i in degree:
    if i == N-1:
        result += 1

print(result)