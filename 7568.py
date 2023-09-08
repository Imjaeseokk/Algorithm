n = int(input())

men = [[] for _ in range(n)]
for m in range(n):
    men[m] = tuple(map(int,input().split()))


for i in range(n):
    w,h = men[i]
    cnt = 1
    for j in range(n):
        if i != j:
            cw,ch = men[j]
            if cw > w and ch > h:
                cnt +=1
    print(cnt, end= " ")
