end = int(input())
n = int(input())


if n > 0:
    broke = list(map(str, input().split()))
else:
    broke = []

onlyBtn = abs(end - 100)
ableChannel = []

for i in range(1000001):
    able = True
    for s in str(i):
        if s in broke:
            able = False
            break
    if able:
        ableChannel.append(len(str(i))+abs(i-end))

if n == 10:
    print(onlyBtn)
else:
    print(min(min(ableChannel),onlyBtn))




