import sys
input = sys.stdin.readline
heap = []

n = int(input())


def heappop(h):
    print(h.pop(0))
    if not h:
        return []

    h.insert(0,h.pop())
    pIndex = 0
    cIndex = 2*pIndex + 1
    smallIndex = cIndex
    while True:
        if len(h) < (cIndex+1):
            return h
        elif len(h) == cIndex+1:
            smallIndex = cIndex
        else:
            if abs(h[cIndex]) < abs(h[cIndex+1]):
                smallIndex = cIndex
            elif abs(h[cIndex]) == abs(h[cIndex+1]):
                if h[cIndex] < 0:
                    smallIndex = cIndex
                elif h[cIndex+1] < 0:
                    smallIndex = cIndex + 1
                else:
                    smallIndex = cIndex
            else:
                smallIndex = cIndex + 1

        if (abs(h[pIndex]) > abs(h[smallIndex])) or ((abs(h[pIndex]) == abs(h[smallIndex])) and h[smallIndex] < 0 ):
            h[pIndex] ,h[smallIndex] = h[smallIndex], h[pIndex]
            pIndex = smallIndex
            cIndex = 2 * pIndex + 1
        else:
            return h
        if pIndex >= len(h):
            return h



def push(h,x):
    h.append(x)
    xIndex = len(h) - 1
    while True:
        pIndex = (xIndex-1)//2
        if (abs(h[pIndex]) > abs(h[xIndex])) or ((abs(h[pIndex]) == abs(h[xIndex])) and h[xIndex] < 0 ):
            h[pIndex], h[xIndex] = h[xIndex], h[pIndex]
        xIndex = pIndex
        if xIndex <= 0:
            break
    return h

for i in range(n):
    order = int(input())
    if not order:
        if not heap:
            print(0)
        else:
            heap = (heappop(heap))

    else:
        heap = push(heap,order)




