import sys

input = sys.stdin.readline

n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array)

lower = 0
upper = 0
solution = 2000000001
while (lower < n) and (upper < n):
    distance = array[upper] - array[lower]
    if distance < m:
        upper += 1
    elif distance == m:
        solution = distance
        break
    elif distance > m:
        solution = min(solution,distance)
        lower +=1

print(solution)