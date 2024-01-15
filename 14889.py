import sys
input = sys.stdin.readline

N = int(input())
powers = [list(map(int,input().split())) for _ in range(N)]

visited = [0 for _ in range(N)]
minPowerDiff = 1e9

def team(depth,idx):
    global minPowerDiff
    if depth == N//2:
        powerA = 0
        powerB = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    powerA += powers[i][j]
                elif not visited[i] and not visited[j]:
                    powerB += powers[i][j]
        minPowerDiff = min(abs(powerA-powerB),minPowerDiff)
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            team(depth+1,i+1)
            visited[i] = False

team(0,0)
print(minPowerDiff)
