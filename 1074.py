n,r,c = map(int,input().split())

result = 0
for i in range(n,0,-1):

    bitR = r//(2**(i-1))
    bitC = c//(2**(i-1))

    bin = bitR*2 + bitC*1
    result += bin * (2**(2*i-2))
    #print("bit:",bitR, bitC,"pt:",r,c, result)

    if bitR: r -= (2**(i-1))
    if bitC: c -= (2**(i-1))
print(result)