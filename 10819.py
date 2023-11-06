n = int(input())

numbers = list(map(int,input().split()))
index = [k for k in range(n)]
results = []
def summary(arr):
    l = []
    array = []
    for z in arr:
        array.append(numbers[z])
    for j in range(len(array)-1):
        l.append(abs(array[j]-array[j+1]))
    return (sum(l))
def backtrack(arr):
    if len(arr) == n:
        results.append(summary(arr))
        return

    for i in index:
        if not i in arr:
            arr.append(i)
            backtrack(arr)
            arr.pop()

backtrack([])
print(max(results))