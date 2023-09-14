n = int(input())

paper = [[]for _ in range(n)]
for p in range(n):
    paper[p] = list(map(int,input().split()))

def scan(checkPaper,wcnt,bcnt):
    l = len(checkPaper)
    blueCount = bcnt
    whiteCount = wcnt
    color = checkPaper[0][0]
    for x in range(l):
        for y in range(l):
            if checkPaper[x][y] != color:
                cd = l//2
                d = [(0, cd, 0, cd), (cd, l, 0, cd),(0, cd, cd, l), (cd, l, cd, l)]
                for a,b,c,d in d:
                    subPaper = [row[a:b] for row in checkPaper[c:d]]
                    whiteCount,blueCount = scan(subPaper,whiteCount,blueCount)
                return whiteCount,blueCount
    if color:
        return whiteCount, blueCount+1
    else:
        return  whiteCount+1, blueCount,

print("\n".join(map(str,scan(paper,0,0))))

