a,b,c = map(int,input().split())

result = 0

cnt = 0
k = (a%b)
while True:
    result = (k*10)//b
    k = (k*10)%b
    cnt +=1
    if cnt == c:
        print(result)
        break