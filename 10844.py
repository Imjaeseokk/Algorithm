n = int(input())

dp = [[0 for j in range(10)]for i in range(n+1)]

dp[0] = [0,0,0,0,0,0,0,0,0,0]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for k in range(2,n+1):

    dp[k][0] = dp[k-1][1]
    for x in range(1,9):
        dp[k][x] = dp[k-1][x-1] + dp[k-1][x+1]
    dp[k][9] = dp[k-1][8]

print(sum(dp[n])%1000000000)