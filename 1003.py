tc = int(input())

for t in range(tc):
    dp = [(1, 0), (0, 1)]
    n = int(input())
    for i in range(2,n+1):
        dp.append((dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]))

    print(*dp[n])