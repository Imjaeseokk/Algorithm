n,m = map(int,input().split())
r = n-m

def cntFive(x,number):
    five = 0
    while x:
        x //= number
        five += x

    return five

print(min((cntFive(n,5)-cntFive(m,5)-cntFive(r,5)),(cntFive(n,2)-cntFive(m,2)-cntFive(r,2))))
