n = int(input())
now = list(map(int,input().split()))
hope = list(map(int,input().split()))

mx = max(max(now),max(hope))

cnt = [0 for _ in range(mx+1)]

for i in now:
    cnt[i] +=1

result = 0


for j in hope:
    if cnt[j] > 0:
        cnt[j] -= 1
    else:
        result +=1

print(result)


