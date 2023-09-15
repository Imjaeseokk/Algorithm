import sys
input = sys.stdin.readline
n = int(input())
heap = []

def heappush(x,h):
    index = len(h) # heap에 [0,1,2] 있으면 3, push한 값의 현재 위치
    h.append(x)     # heap 맨 아래 왼쪽에 x push, index는 3,
    while h[(index-1)//2] > h[index]:
        #print("change",h)
        if h[(index-1)//2] > x: # x의 부모노드(3,4면 1, 5,6이면 2)보다 작으면
            h[(index-1)//2] , h[index] = h[index], h[(index-1)//2]
        index = (index-1)//2
        if not index:
            break

def heappop(h):
    print(h.pop(0))
    if not heap:
        return
    h.insert(0,h.pop())
    root = 0
    while True:
        if len(h) <= ((root*2)+1): # heap에 root의 자식노드가 없을때
            break
        elif len(h) > ((root*2)+2): # heap에 root의 자식노드가 둘 다 있을 때
            if h[(root*2)+1] > h[(root*2)+2]:
                nextRoot = (root*2)+2
            else:
                nextRoot = (root*2)+1
        elif len(h) == (root*2)+2:
            nextRoot = (root*2)+1
        if h[root] <= h[nextRoot]:
            break
        else:
            h[root], h[nextRoot] = h[nextRoot], h[root]
        root = nextRoot



for i in range(n):
    inp = int(input())
    if not inp:
        if not heap:
            print(0)
        else:
            heappop(heap)
            # print(heap.pop(0))
    else:
        heappush(inp,heap)
    #print(heap)