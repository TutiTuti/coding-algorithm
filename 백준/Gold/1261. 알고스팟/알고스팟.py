import heapq

INF = 1e8
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
N, M = map(int, input().split())
# 공백 없으면 strip
miro = [list(map(int, input().strip())) for _ in range(M)]

def Dijkstra():
    dist_Dstra = [[INF] * N for _ in range(M)]
    dist_Dstra[0][0] = 0
    h = []
    # cost, row ,col
    heapq.heappush(h, [0, 0, 0])
    while h:
        cost, r, c = heapq.heappop(h)
        if cost > dist_Dstra[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < M and 0 <= nc < N:
                new_cost = cost + miro[nr][nc]
                if dist_Dstra[nr][nc] > new_cost:
                    dist_Dstra[nr][nc] = new_cost
                    heapq.heappush(h, [new_cost, nr, nc])
    print(dist_Dstra[M-1][N-1])

Dijkstra()