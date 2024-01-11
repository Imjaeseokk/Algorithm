n = int(input())

primes = list(map(int,input().split()))
k = int(input())

result = 0
for prime in primes:
    i = 1
    while True:
        if prime ** i > k:
            break
        result += (k//(prime**i))
        i += 1

print(result)