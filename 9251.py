string1 = ["0"]+list(input())
string2 = ["1"]+list(input())

dp = [[0 for _ in range(len(string1))]for _ in range(len(string2))]


for i in range(1,len(string2)):
    for j in range(1,len(string1)):
        if string1[j] == string2[i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])


print(dp[i][j])