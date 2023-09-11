import sys
n = int(input())

diff = [0 for _ in range(n)]
for i in range(n):
    diff[i] = int(sys.stdin.readline())

diff = sorted(diff)
result = 0
if n > 0:
    trim = ((int(n*0.15))//1) + int(((n*0.15)%1) >= 0.5)

    if trim > 0:
        diff = diff[trim:-trim]

    result = sum(diff)/(len(diff))
    result = (int(result//1) + int((result%1) >= 0.5 ))
print(result)
