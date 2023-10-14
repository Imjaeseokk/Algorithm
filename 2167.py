n,m = map(int,input().split())

array = [[] for _ in range(n)]
for i in range(n):
    array[i] = list(map(int,input().split()))

tc = int(input())
for t in range(tc):
    total = 0
    i,j,x,y = map(int,input().split())
    for q in range(i-1,x):
        for w in range(j-1,y):
            total += array[q][w]

    print(total)