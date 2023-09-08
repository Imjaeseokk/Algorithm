tc = int(input())
for t in range(tc):
    k = int(input())
    n = int(input())
    apt = [[i for i in range(n+1)]for _ in range(k+1)]

    for f in range(1,k+1):
        for h in range(1,n+1):
            apt[f][h] = apt[f-1][h] + apt[f][h-1]

    print(apt[k][n])