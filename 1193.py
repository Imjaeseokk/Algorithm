n = int(input())

sum = 0
i = 1
for i in range(1,n+1):
    sum += i
    if n <= sum:
        break
# i는 i번째 행에 있음
k = n - (sum-i)
# k는 i번째 행의 k번째 떨어짐


if i%2 == 0:
    a = 1
    b = i
    for j in range(1,k):
        a += 1
        b -= 1
else:
    a = i
    b = 1
    for j in range(1,k):
        a -= 1
        b += 1
print(a,"/",b,sep="")
