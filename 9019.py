from collections import deque

tc = int(input())

def bfs(dict):
    outDict = {}
    for k,v in dict.items():
        if not visit[k]:
            visit[k] = True
            dValue = (k*2)%10000
            sValue = k-1 if k>0 else 9999
            kStr = str(k).zfill(4)
            lValue = int(kStr[1:]+kStr[0])
            rValue = int(kStr[-1] + kStr[:-1])
            outDict[dValue] = v+"D"
            outDict[sValue] = v + "S"
            outDict[lValue] = v + "L"
            outDict[rValue] = v + "R"

    return outDict



for t in range(tc):
    visit = [0 for _ in range(10000)]
    a,b = map(int,input().split())
    d = {a:""}
    while not b in d.keys():
        d = bfs(d)

    print(d[b])