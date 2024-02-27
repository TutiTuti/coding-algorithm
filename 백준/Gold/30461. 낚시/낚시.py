import sys;
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = arr[i][j]
        nr = i-1
        nc = j
        if 0 <= nr < N and 0 <= nc < M:
            dp[i][j] += dp[nr][nc]
        nr = i-1
        nc = j-1
        if 0 <= nr < N and 0 <= nc < M:
            dp[i][j] += dp[nr][nc]
        nr = i-2
        nc = j-1
        if 0 <= nr < N and 0 <= nc < M:
            dp[i][j] -= dp[nr][nc]

for _ in range(K):
    r, c = map(int, input().split())
    print(dp[r-1][c-1])