n,m = map(int,input().split())
maze = [[]for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int,input().split()))

dp = [[0 for _ in range(m)]for _ in range(n)]   # dp 2중 리스트, 해당 칸까지 가져갈 수 있는 사탕 개수가 저장됨
dp[0][0]= maze[0][0]    # 출발점 사탕 개수는 더해질 수 없으니 기존과 동일

for y in range(n):
    for x in range(m):
        candyL = candyU = candyD = maze[y][x]   # 왼쪽, 위, 대각선의 사탕 개수를 더하기 위한 변수
        l = x-1
        u = y-1
        if l >= 0:              # 해당 방의 왼쪽이 미로 안이면
            candyL += dp[y][l]
        if u >= 0:              # 해당 방의 위쪽이 미로 안이면
            candyU += dp[u][x]
        if u >= 0 and l >= 0:   # 해당 방의 좌상 대각선이 미로 안이면
            candyD += dp[u][l]  # 해당 위치의 기존 미로 사탕 개수와 dp 사탕 개수 합
        dp[y][x] = max(candyL,candyU,candyD)    # 그 중 가장 큰 개수가 dp 미로의 사탕 개수

print(dp[n-1][m-1]) # n,m칸까지 가면서 가져갈 수 있는 사탕의 최대값
