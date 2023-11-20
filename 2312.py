tc = int(input())

def func(x):
    d = dict()
    for i in range(2,x+1):
        while x%i == 0:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
            x = x//i
    return d

for t in range(tc):
    n = int(input())
    d = func(n)
    for y,z in d.items():
        print(y,z)