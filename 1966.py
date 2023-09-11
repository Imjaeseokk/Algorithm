from collections import deque

tc = int(input())

def printer(p,m):
    cursur = 0
    l = len(p)
    output = [0 for _ in range(len(p))]
    cnt = 1
    k = 0
    while p:
        # print(output, cursur,"p",p)
        if not (0 in output):
            break
        while output[cursur]:
            cursur = (cursur + 1) % l

        is_out = 1
        i = p[0]
        for j in p:
            if j > i:
                p.append(i)
                p.pop(0)
                is_out = 0
                break
        if is_out:
            p.pop(0)
            output[cursur] = cnt
            cnt += 1
        cursur = (cursur + 1) % l
    print(output[m])

for t in range(tc):
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    printer(p,m)