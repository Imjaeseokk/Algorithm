N, M = map(int,input().split())
D = int(input())

vertex = [(0,0),(0,M-1),(N-1,0),(N-1,M-1)]
cnt = 0

for i in range(N):
    for j in range(M):
        distances = []
        for vy, vx in vertex:
            distance = abs(i-vy) + abs(j-vx)
            distances.append(distance)
            # print(f"y:{vy}, x:{vx}, d:{distance}")
        if max(distances) < D:
            cnt += 1

print(cnt)
