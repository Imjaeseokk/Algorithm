tc = int(input())

prime = [x for x in range(2,10000)]

for i in range(2,10000):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            prime.remove(i)
            break

for t in range(tc):
    n = int(input())
    answer = []
    goldBH = [p for p in prime if p <= n//2]
    for g in goldBH:
        if (n-g) in prime:
            answer.append([g,n-g])
    print(*answer[-1])