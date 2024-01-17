import sys
input = sys.stdin.readline
N,M = map(int,input().split())

table = [[] for _ in range(N)]
dp  = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    table[i] = list(map(int,input().split()))
    if i == 0:
        dp[i][0] = table[i][0]

for x in range(N):
    for y in range(N):
        up = 0
        right = 0
        diag = 0
        if x > 0:
            up = dp[x-1][y]
        if y > 0:
            right = dp[x][y-1]
        if x > 0 and y >0:
            diag = dp[x-1][y-1]
        value = table[x][y] + up + right - diag
        dp[x][y] = value

for j in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    minus_up = 0
    minus_right = 0
    plus_diag = 0
    if x1 > 1:
        minus_up = dp[x1-2][y2-1]
    if y1 > 1:
        minus_right = dp[x2-1][y1-2]
    if x1 > 1 and y1 > 1:
        plus_diag = dp[x1-2][y1-2]
    print(dp[x2-1][y2-1]-minus_up-minus_right+plus_diag)
