n,k = map(int,input().split())

goods = [0 for _ in range(n)]
for i in range(n):
    w,v = map(int,input().split())
    goods[i] = [w,v]

goods = sorted(goods)
goods.insert(0,[0,0])

table = [[0 for _ in range(k+1)]for _ in range(n+1)]

for i in range(n+1):
    for W in range(k+1):
        if i == 0 or W == 0:
            table[i][W] = 0
            continue

        if goods[i][0] > W:
            table[i][W] = table[i-1][W]
        else:
            table[i][W] = max((goods[i][1] + (table[i-1][W-goods[i][0]])),table[i-1][W])


print(table[n][k])
