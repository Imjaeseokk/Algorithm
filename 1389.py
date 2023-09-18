from collections import deque
n,m = map(int,input().split())

friend = [[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(start):
    q = deque([start])
    cnt = 0
    dest = [0 for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    visit[start] = True
    while q:
        i = q.popleft()
        # print(init,friend[init])
        for f in friend[i]:
            if not visit[f]:
                visit[f] = True
                dest[f] = dest[i]+1
                q.append(f)
    return dest

result = []
for j in range(1,n+1):
    result.append(sum(bfs(j)))

#     print(result)
#     if mn >= result:
#         mn = result
#         output = j
print(result.index(min(result))+1)
# print(output)
