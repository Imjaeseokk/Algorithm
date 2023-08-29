n = int(input())

dp = [(1,0),(0,1)]
                            # 끝자리가 1의 개수, 끝자리가 0의 개수
for i in range(2,n):
    o = dp[i-1][1]
    z = sum(dp[i-1])
    dp.append((o,z))

print(sum(dp[n-1]))