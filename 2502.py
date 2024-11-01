import sys

D, K = map(int, sys.stdin.readline().split())

for i in range(1,100000):
    for j in range(1,100000):
        pibo = [0] * (D+1)
        pibo[1] = i
        pibo[2] = j

        for k in range(3,D+1):
            pibo[k] = pibo[k-1] + pibo[k-2]

        if pibo[-1] == K:
            print(pibo[1])
            print(pibo[2])
            exit()