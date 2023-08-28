n = int(input())
stair = [0 for _ in range(n+1)]
for i in range(1,n+1):
    stair[i] = int(input())

dp = [0]
for j in range(1,n+1):
    if j == 1:
        dp.append(stair[1])
    if j == 2:
        dp.append(stair[1]+stair[2])
    if j > 2:
        dp.append(max(dp[j-2]+stair[j],dp[j-3]+stair[j-1]+stair[j]))
print(dp[-1])