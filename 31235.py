n = int(input())
arr = list(map(int,input().split()))


result = [0]
key = arr[0]
cnt = 0
for i in range(1,len(arr)):
    if key > arr[i]:
        cnt += 1
    else:
        result.append(cnt)
        cnt = 0
        key = arr[i]
    result.append(cnt)

print(max(result)+1)