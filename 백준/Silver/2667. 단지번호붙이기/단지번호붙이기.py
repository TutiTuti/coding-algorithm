def dfs(i, j, cnt):
    arr[i][j] = 0
    for k in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni = i + k[0]
        nj = j + k[1]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
            cnt = dfs(ni, nj, cnt+1)
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans.append(dfs(i, j, 1))

print(len(ans))
for i in sorted(ans):
    print(i)