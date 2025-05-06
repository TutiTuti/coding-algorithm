import math
import heapq

def cal_dist(a, b):
    ax, ay = loc[a]
    bx, by = loc[b]
    return math.sqrt((ax-bx)**2 + (ay - by)**2)

N, W = map(int, input().split())
limit = float(input())
INF = 200_000.1

# 노드 간거리 계산 저장

# 각 노드 좌표 저장
loc = []
for _ in range(N):
    x, y = map(int, input().split())
    loc.append([x, y])

# 노드간 거리 저장
matrix = list([INF] * N for _ in range(N))
for _ in range(W):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 0
    matrix[b-1][a-1] = 0
# 제한 범위 안에서 연결 가능한 범위 계산 저장
for i in range(N):
    for j in range(N):
        if i != j and matrix[i][j] == INF:
            matrix[i][j] = matrix[j][i] = cal_dist(i, j)

def Dijkstra():
    # 0부터 각 노드까지 거리 기록 
    dist = [INF] * N
    dist[0] = 0
    h = []
    # 시작 지점 -> 해당 노드까지 계산된 거리
    heapq.heappush(h, [0, 0])
    while h:
        now, cost = heapq.heappop(h)
        if dist[now] < cost:
            continue
        for i in range(N):
            if i != now and dist[i] > cost + matrix[now][i]:
                dist[i] = cost + matrix[now][i]
                heapq.heappush(h, [i, dist[i]])
                
    return dist[N-1]

ans = Dijkstra()
print(int(ans * 1000))