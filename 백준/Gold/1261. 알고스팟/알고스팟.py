
from collections import deque
INF = 1e8
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
N, M = map(int, input().split())

# 공백 없으면 strip
miro = [list(map(int, input().strip())) for _ in range(M)]
dist = [[INF] * N for _ in range(M)]
dist[0][0] = 0
q = deque()
q.append([0, 0])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            cost = miro[ny][nx]
            if dist[y][x] + cost < dist[ny][nx]:
                dist[ny][nx] = dist[y][x] + cost
                if cost:
                    q.append([nx, ny])
                else:
                    q.appendleft([nx, ny])
print(dist[M-1][N-1])