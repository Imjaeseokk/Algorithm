N = int(input())
M = int(input())

fixed = []
seats = []
for i in range(M):
    fixed.append(int(input()))

seat = []
for i in range(1,N+1):
    if not i in fixed:
        seat.append(i)
    else:
        seats.append(seat)
        seat = []

if seat:
    seats.append(seat)

fibo = [1,1]
for i in range(2,N+1):
    fibo.append(fibo[i-1]+fibo[-2])
# print(fibo)

cnt = [len(s) for s in seats]

result = 1
for i in cnt:
    result*=fibo[i]

print(result)
