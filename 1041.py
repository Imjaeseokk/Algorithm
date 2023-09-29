n =int(input())

a,b,c,d,e,f = map(int,input().split())

dice = [a,b,c,d,e,f]

if n == 1:
    area = sum(sorted(dice)[:-1])
else:
    smallNum = []
    smallNum.append(min(dice[0],dice[5]))
    smallNum.append(min(dice[1],dice[4]))
    smallNum.append(min(dice[2],dice[3]))
    smallNum = sorted(smallNum)

    area = 0
    area += smallNum[0] * ((n-1)*(n-2)*4 + (n-2)**2)
    area += sum(smallNum[:2]) * ((n-1)*4 + (n-2)*4)
    area += sum(smallNum[:3]) * 4
print(area)