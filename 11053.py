n = int(input())
array = list(map(int,input().split()))
dp = [1]

for i in range(1,n):
    number = array[i]
    increase = [1]
    for j in range(i):
        if number > array[j]:
            increase.append(dp[j]+1)
    dp.append(max(increase))

print(max(dp))
