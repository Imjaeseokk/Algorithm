tc = int(input())

for t in range(tc):
    d = {}
    n = int(input())
    for p in range(n):
        item,cate = input().split()
        if not cate in d.keys():
            d[cate] = 2
        else:
            d[cate] += 1
    output = 1
    for k in d.keys():
        output = output * d[k]
    print(output-1)
