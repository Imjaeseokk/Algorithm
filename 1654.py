k,n = map(int,input().split())

lengths = [0 for _ in range(k)]
for i in range(k):
    lengths[i] = int(input())

start = max(lengths)
begin = start
end = 0

while True:
    cnt = 0
    # print(begin, start, end)
    for j in range(k):
        cnt += lengths[j] // start
    if cnt < n:
        begin = start
        start = (begin + end) // 2
    elif cnt >= n:
        end = start
        start = (end + begin) // 2
    if (end) == start or (begin) == start:
        print(start)
        break


