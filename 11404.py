N = int(input())
M = int(input())

cities = [[int(1e9) for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    cities[a][b] = min(c, cities[a][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            cities[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cities[i][j] = min(cities[i][j], cities[i][k] + cities[k][j])

for x in range(1, N + 1):
    for y in range(1, N + 1):
        if cities[x][y] == int(1e9):
            print(0, end=" ")
        else:
            print(cities[x][y], end=" ")
    print()
