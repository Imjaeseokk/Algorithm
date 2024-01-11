import sys

sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
reps = [i for i in range(n)]


def find(x):
    if x != reps[x]:
        reps[x] = find(reps[x])
    return reps[x]


def union(x, y):
    rep1 = find(reps[x])
    rep2 = find(reps[y])
    if rep1 < rep2:
        reps[rep2] = rep1
    else:
        reps[rep1] = rep2


flag = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i + 1)
        flag = 1
        break
    union(a, b)

if not flag:
    print(0)