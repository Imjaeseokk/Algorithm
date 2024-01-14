n = int(input())

def prime(x):
    y = int(x**0.5)
    for i in range(2,y+1):
        if x % i == 0:
            return False
    return True

i = 2
result = []
while len(result) < n:
    if prime(i):
        result.append(i)
    i+=1

print(*result)
