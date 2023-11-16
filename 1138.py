n = int(input())
high = list(map(int,input().split()))

lane = [man for man in range(1,n+1)]

for i in range(n):
    pointer = lane.index(i+1)
    count = high[i]
    for j in range(count):
        for k in range(pointer+1,n):
            if lane[pointer] < lane[k]:
                lane[pointer],lane[k] = lane[k], lane[pointer]
                pointer = k
                break
print(*lane)