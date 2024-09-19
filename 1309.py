N = int(input())

xor_dp = [2]
null_dp = [1]

# 이전 cell layer의 xor * 2 + null * 3이 number of cases
# xor layer의 next layer는 xor 1개 null 1개임
# null layer의 next layer는 xor 2개 null 1개임

for i in range(1, N):
    xor_dp.append((xor_dp[i-1]+null_dp[i-1]*2)%9901)
    null_dp.append((xor_dp[i-1]+null_dp[i-1])%9901)
    #print(xor_dp, null_dp)


print((xor_dp[-1] + null_dp[-1])%9901)