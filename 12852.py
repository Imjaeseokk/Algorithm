dp = [0,0]
n = int(input())
step = [0,0]
for i in range(2,n+1):
    comp = []
    if i%3 == 0:
        comp.append((dp[i//3],i//3))
    if i%2 == 0:
        comp.append((dp[i//2],i//2))
    comp.append((dp[i-1],i-1))

    x,y = min(comp)
    dp.append(x+1)
    step.append(y)

result = n
print(dp[n])
while n > 0:
    print(n,end=" ")
    n = step[n]