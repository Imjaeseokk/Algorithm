import sys
stackA = list(sys.stdin.readline().rstrip())
length = len(stackA)
stackB = []

for i in range(int(input())):
    f = list(sys.stdin.readline().split())
    if f[0] == "L":
        if stackA:
            stackB.append(stackA.pop())

    elif f[0] == "D":
        if stackB:
            stackA.append(stackB.pop())

    elif f[0] == "B":
        if stackA:
            stackA.pop()
    else:
        char = f[1]
        stackA.append(char)


stackB.reverse()
print(*stackA,*stackB,sep="")



