n,m = map(int,input().split())

times = sorted(list(map(int,input().split())),reverse = True)
powers = [0 for _ in range(m)]

if n <= m:
    print(max(times))
else:
    for t in times:
        early = min(powers)
        charge = powers.index(early)
        powers[charge] += t
    print(max(powers))