N = int(input())
ARR = list(map(int,input().split()))

accum = [0 for _ in range(N)]


for i,v in enumerate(ARR):
    if i == 0:
        accum[i] = v
        continue
    
    if accum[i-1] < 0:
        accum[i] = v
        continue
    
    accum[i] = v + accum[i-1]
    

print(max(accum))