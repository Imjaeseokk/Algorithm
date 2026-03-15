N = int(input())

ARR = list(map(int,input().split()))

d = [0 for _ in range(N)]

for i,v in enumerate(ARR):
    d[i] = 1
    for j in range(i):
        if ARR[j] > ARR[i]:
            d[i] = max(d[i], d[j]+1)

print(N-max(d))