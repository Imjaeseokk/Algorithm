n = int(input())

target = [0 for _ in range(n)]
for t in range(n):
    target[t] = int(input())
used = [0 for _ in range(n+1)]

stack = []
result = []

def push(stack,k):
    s = 0 if not stack else stack[-1]
    for i in range(s,k):
        if not used[i+1]:
            result.append("+")
            stack.append(i+1)
            used[i+1] = 1
    return stack

while True:
    for t in range(n):
        # print("stack:", stack)
        s = 0 if not stack else stack[-1]
        cursur = target[t]
        if s == cursur:
            result.append("-")
            stack.pop()
            #print(stack.pop())
        elif s < cursur:
            stack = push(stack,cursur)
            result.append("-")
            stack.pop()
            #print(stack.pop())
        else:
            print("NO")
            result = []
            break
    break

if result:
    print("\n".join(result))