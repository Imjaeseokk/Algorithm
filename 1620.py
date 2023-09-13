import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pocket = dict()
for i in range(n):
    mon = input().rstrip()
    pocket[mon] = i

k = list(pocket.keys())
for j in range(m):
    t = (input().rstrip())
    if t.isdigit():
        t = int(t)
        print(k[t-1])
    else:
        print(pocket[t]+1)
