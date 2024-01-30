N = int(input())

friends = [[N for _ in range(N+1)] for _ in range(N+1)]

while True:
    a,b = map(int,input().split())
    if a == b == -1:
        break

    friends[a][b] = 1
    friends[b][a] = 1



for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            friends[i][j] = min(friends[i][j] , friends[i][k] + friends[k][j])
            if i == j:
                friends[i][j] = 0
candidates = [int(1e9) for _ in range(N+1)]
for i in range(1,N+1):
    candidates[i] = max(friends[i][1:])

leader_score = min(candidates)
print(leader_score,candidates.count(leader_score))
for i in range(1,N+1):
    if candidates[i] == leader_score:
        print(i,end=" ")

