import sys
n,m,b = map(int,input().split())

blocks = [[]for _ in range(n)]
height = []
for i in range(n):
    blocks[i] = list(map(int,sys.stdin.readline().split()))
#    height.extend(blocks[i])

#height = sorted(list(set(height)),reverse = True)

  #올려야됨
  #빼야됨
#result = []
result = 99999999
for h in range(257):
    putBlock = 0
    getBlock = 0
    time = 0
    for x in range(n):
        for y in range(m):
            if blocks[x][y] > h:
                getBlock += blocks[x][y] - h
            else:
                putBlock += h - blocks[x][y]
    time = getBlock*2 + putBlock*1
    if b+getBlock < putBlock:
        continue
    # else:
    #     result.append((time,h))

    if time <= result:
        result = time
        result_height = h
#result = sorted(result,key = lambda x:(x[0],-x[1]))

print(result,result_height)