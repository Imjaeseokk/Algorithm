import sys

input = sys.stdin.readline

N, Q = map(int,input().split())

array = list(map(int,input().split()))
prefix = [0]

array = sorted(array)

for i in range(N):
    prefix.append(prefix[i]+array[i])

for i in range(Q):
    l, r = map(int,input().split())
    print(prefix[r]-prefix[l-1])