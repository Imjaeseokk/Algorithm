a,b,c = map(int,input().split())

def dac(b):
    if b == 1:
        return a%c
    if b%2 == 0:
        part = dac(b//2)
        return (part*part)%c
    else:
        part = dac(b//2)
        return part*part*a%c

print(dac(b))