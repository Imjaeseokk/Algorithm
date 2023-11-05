k = int(input())
compare = list(input().split())
numbers = [n for n in range(10)]
results = []


def backtrack(arr):
    if len(arr) == (k+1):
        for z in range(k):
            if compare[z] == "<":
                if arr[z] >= arr[z+1]:
                    return
            else:
                if arr[z] <= arr[z+1]:
                    return
        results.append(str("".join(map(str,arr))))
        return
    for i in numbers:
        if not i in arr:
            arr.append(i)
            backtrack(arr)
            arr.pop()


for j in numbers:
    backtrack([j])

print(results[-1],results[0],sep="\n")