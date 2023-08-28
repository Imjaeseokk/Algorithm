from collections import deque

f,s,g,u,d = map(int,input().split())

visit = [0 for _ in range(f+1)]

def bfs(f,s,g,u,d):
    q = deque([(s,0)])
    visit[s] = 1
    result = "use the stairs"
    while q:
        cur_f, step = q.popleft()
        if cur_f == g:
            result = step
            return result
        up_f = cur_f + u
        dn_f = cur_f - d
        if up_f <= f and not visit[up_f]:
            visit[up_f] = 1
            q.append((up_f,step+1))
        if dn_f > 0 and not visit[dn_f]:
            visit[dn_f] = 1
            q.append((dn_f,step+1))

    return result


print(bfs(f,s,g,u,d))
