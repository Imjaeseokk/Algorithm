n = int(input())
costTable = [[] for _ in range(n)]
for i in range(n):
    costTable[i] = list(map(int,input().split()))


costs = [costTable[0]]
for j in range(1,n):
    red = costTable[j][0] + min(costs[j-1][1],costs[j-1][2])
    green = costTable[j][1] + min(costs[j-1][0], costs[j-1][2])
    blue = costTable[j][2] + min(costs[j-1][0], costs[j-1][1])
    costs.append([red,green,blue])
print(min(costs[-1]))
