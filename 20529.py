tc = int(input())
for t in range(tc):
    n = int(input())
    mbtis = list(input().split())
    type = list(set(mbtis))
    if n > (2*len(type)):
        print(0)

    else:
        close = 99
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    dis = 0
                    if (a!=b) and (b!=c) and (a!=c):
                        first = mbtis[a]
                        second = mbtis[b]
                        third = mbtis[c]
                        for f in range(4):
                            if first[f] != second[f]:
                                dis += 1
                            if second[f] != third[f]:
                                dis += 1
                            if first[f] != third[f]:
                                dis +=1
                        close = min(close,dis)
        print(close)





