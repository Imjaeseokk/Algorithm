from collections import deque
n = int(input())
parents = list(map(int,input().split()))
d = int(input())
visit = [ 0 for _ in range(n+1)]

node = [[_] for _ in range(n)]
root = []
for p in range(len(parents)):
    if not p == d:
        if not parents[p] == -1:
            node[parents[p]].append(p)
        else:
            root.append(p)



def bfs(ini,d):
    cnt = 0
    q = deque([ini])
    while q:
        i = q.popleft()
        for nd in node[i]:
            if nd != d:
                if not visit[nd]:
                    visit[nd] = 1
                    if len(node[nd]) == 1:
                        cnt +=1
                    else:
                        q.append(nd)
    return cnt
answer = 0
node[d] = []

for r in root:
    answer += (bfs(r,d))
print(answer)