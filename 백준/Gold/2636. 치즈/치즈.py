from collections import deque
N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]

remain = 0
for i in range(N):
    for j in range(M):
        if cheese[i][j]:
            remain += 1

surface = []
q = deque()
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def melt():
    for i, j in surface:
        cheese[i][j] = 0

def bfs():
    q.append([0, 0])
    vstd[0][0] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not vstd[nr][nc]:
                vstd[nr][nc] = 1
                if cheese[nr][nc]:
                    surface.append([nr, nc])
                else:
                    q.append([nr, nc])


hour = 1
while True:
    vstd = [[0] * M for _ in range(N)]
    bfs()
    melt()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j]:
                cnt += 1
    if cnt == 0:
        print(hour)
        print(remain)
        break
    remain = cnt
    hour += 1