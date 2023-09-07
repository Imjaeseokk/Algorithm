import sys
n = int(sys.stdin.readline())


queue = []
for i in range(n):
    fn = list(sys.stdin.readline().split())
    if len(fn) == 2:
        x = int(fn[1])
        fn = fn[0]
    else:
        x = 0
        fn = fn[0]
    if fn == 'push':
        queue.append(x)
    elif fn == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif fn == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif fn == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif fn == 'size':
        print(len(queue))
    elif fn == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

