tc = int(input())

for t in range(tc):
    m,n,x,y = map(int,input().split())
    k = 0
    result = 1
    for k in range(x,(m*n)+1,m):
        a = (k%n) + int(not(k%n))*n
        if a == y:
            result = k
            break

    if result == k:
        print(result)
    else:
        print(-1)


