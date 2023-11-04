n,k = map(int,input().split())

numbers = list(map(int,input().split()))
ref = sum(numbers[:k])
maximum = ref
for i in range(k,n):
    ref = ref - numbers[i-k] + numbers[i]
    #print(ref)
    maximum = max(ref,maximum)
print(maximum)
