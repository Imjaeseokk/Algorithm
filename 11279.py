import sys
input = sys.stdin.readline

heap = []
n = int(input())

def pop(h):
    print(h.pop(0))
    if h:
        h.insert(0,h.pop(-1))
    rootIndex = 0
    while True:
        if len(h) <= (rootIndex*2)+1:
            break
        elif len(h) >= rootIndex*2 + 3:

            if h[(rootIndex*2)+1] >= h[(rootIndex*2)+2]:
                highIndex = (rootIndex*2)+1
            else:
                highIndex = (rootIndex*2)+2
        else:
            highIndex = rootIndex*2 +1

        if h[rootIndex] >= h[highIndex]:
            break
        else:
            h[rootIndex] , h[highIndex] = h[highIndex], h[rootIndex]
        rootIndex = highIndex



oper = []
for i in range(n):
    d = int(input())
    if not d:
        if heap:
            pop(heap)
        else:
            print(0)
    elif d:
        leafIndex = len(heap)
        heap.append(d)

        while heap[(leafIndex-1)//2] < heap[leafIndex]:
            heap[leafIndex], heap[(leafIndex-1)//2] = heap[(leafIndex-1)//2], heap[leafIndex]
            leafIndex = (leafIndex-1)//2

            if leafIndex == 0:
                break
