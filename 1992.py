N = int(input())
image = [[] for _ in range(N)]

for i in range(N):
    image[i] = list(input())


def quad(x,y,n):
    #print(x,y)
    recur = False
    dot = image[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if image[i][j] != dot:
                recur = True
    if not recur:
        print(dot,end= "")
    else:
        print("(",end="")
        n //= 2
        quad(x,y,n)
        quad(x,y+n,n)
        quad(x+n,y,n)
        quad(x+n,y+n,n)
        print(")",end="")

quad(0,0,N)