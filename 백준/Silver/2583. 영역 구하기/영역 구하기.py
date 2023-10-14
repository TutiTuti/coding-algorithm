import sys
sys.setrecursionlimit(10**6)
def dfs(r, c, cnt):
    arr[r][c] = 1
    for i in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr = r+i[0]
        nc = c+i[1]
        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
            cnt = dfs(nr, nc, cnt+1)
    return cnt

M, N, K = map(int,input().split())
arr = [[0]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1, x2):
            arr[i][j] = 1

ans = 0
ans_l = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            ans += 1
            ans_l.append(dfs(i, j, 1))

print(ans)
for i in sorted(ans_l):
    print(i, end=' ')
