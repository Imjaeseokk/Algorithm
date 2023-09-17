n = int(input())

# sq = []
dp = [0]
# i = 1
# while True:
#     if i**2 > n:
#         break
#     sq.append(i**2)
#     i += 1
# print(sq)
for j in range(1,n+1):
    if (j**0.5)%1 == 0:
        dp.append(1)
    else:
        mini = 4
        jInt = int((j**0.5)//1)
        for k in range(1,jInt+1):
            # print(dp,j,k**2)
            mini = min(mini,1+dp[j-k**2])
        dp.append(mini)
print(dp[n])



