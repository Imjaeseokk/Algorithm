n = int(input())
tri = [[] for _ in range(n)]
for i in range(n):
    tri[i] = list(map(int,input().split()))


pathTri = [tri[0]]
for j in range(1,n):
    path = []
    for k in range(j+1):
        if k == 0:
            path.append(tri[j][0] + pathTri[j-1][0])
        elif k == j:
            path.append(tri[j][k] + pathTri[j-1][k-1])
        else:
            path.append(tri[j][k] + max(pathTri[j-1][k-1],pathTri[j-1][k]))
    pathTri.append(path)
print(max(pathTri[n-1]))