H, W = map(int,input().split())

heights = list(map(int,input().split()))

water = 0

flatland = [[0 for _ in range(W)] for _ in range(H)]

for i, height in enumerate(heights):
    for j in range(height):
        flatland[H-j-1][i] = 1


summation = 0

for i in range(H):
    meet_wall = False
    cnt = 0
    for j in range(W):
        if (not meet_wall) and (flatland[i][j] == 1):
            meet_wall = True
        elif flatland[i][j] == 1:
            summation += cnt
            cnt = 0
        elif meet_wall and flatland[i][j] == 0:
            cnt += 1




print(summation)
