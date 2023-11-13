import sys
sys.setrecursionlimit(10**6)

n = int(input())

result = 1
for x in range(1,n+1):
    result *= x
    check = str(result)
    while check[-1] == "0":
        check = check[:-1]
    if len(check) > 12:
        check = check[-12:]
    result = int(check)
    #print(result)

print(str(result)[-5:])