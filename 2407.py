n,m = map(int,input().split())

def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

print(factorial(n)//(factorial(n-m)*factorial(m)))