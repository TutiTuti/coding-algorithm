
from collections import deque
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(y, x):
    global ans
    flag = 1
    cur = graph[y][x]
    vstd[y][x] = 1
    q = deque()
    q.append([y, x])
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == cur and not vstd[nr][nc]:
                vstd[nr][nc] = 1
                q.append([nr, nc])
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] > cur:
                flag = 0
    if flag:
        ans += 1


N, M = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
vstd = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] and not vstd[i][j]:
            bfs(i, j)
print(ans)