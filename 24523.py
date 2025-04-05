N = int(input())
array = list(map(int,input().split()))

result = [-1]

for i in range(N): # 1,2,3,4,5 # -2,-3, -4, -5, -6
    if i == 0:
        continue
    j = -i-1

    if array[j] == array[j+1]:
        result.append(result[i-1])
        continue
    result.append(N+j+2)

print(*result[::-1])