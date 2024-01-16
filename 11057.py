N = int(input())

numbers = {}
newNumbers = {}
for i in range(10):
    numbers[i] = 1
    newNumbers[i] = 0


for i in range(N-1):
    for j in range(10):
        for k in range(j+1):
            newNumbers[j] += numbers[k]

    for v in range(10):
        numbers[v] = newNumbers[v]
        newNumbers[v] = 0


print(sum(numbers.values())%10007)