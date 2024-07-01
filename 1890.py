N = int(input())

board = []
dp = []
for i in range(N):
    board.append(list(map(int,input().split())))
    dp.append([0 for j in range(N)])
dp[N-1][N-1] = 1



for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        for k in range(1,i+1):
            if board[i-k][j] == k:
                dp[i-k][j] += dp[i][j]
        for l in range(1,j+1):
            if board[i][j-l] == l:
                dp[i][j-l] += dp[i][j]

print(dp[0][0])