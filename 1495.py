N,S,M = map(int,input().split())
V = list(map(int,input().split()))

volumes = [[0 for _ in range(M+1)]for _ in range(N+1)]
volumes[0][S] = 1

for i in range(1,N+1):
    for j in range(M+1):
        if volumes[i-1][j]:
            if j - V[i-1] >= 0:
                volumes[i][j-V[i-1]] = 1
            if j + V[i-1] <= M:
                volumes[i][j+V[i-1]] = 1

result = -1
for i in range(M+1):
    if volumes[-1][i]:
        result = i

print(result)

