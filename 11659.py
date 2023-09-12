import sys


n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
prefix = [0]
for i in range(1,n+1):
    prefix.append(prefix[i-1]+numbers[i-1])

for x in range(m):
    j,k = map(int,sys.stdin.readline().split())
    print(prefix[k]-prefix[j-1])
