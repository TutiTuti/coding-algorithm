import heapq
N, M = map(int, input().split())

A = list(map(int, input().split()))
INF = int(1e18)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [[INF] * 11 for _ in range(N + 1)]
dist[1][1 % A[0]] = 0 # 자기 자신은 0
h = []
for i, j in graph[1]:
    tmp = i % A[0]  # A[i - 1]로 나눈 나머지
    if dist[i][tmp] > j:
        dist[i][tmp] = j
        heapq.heappush(h, (j, i, 1))  # cost, now, prev
while h:
    cost, now, prev = heapq.heappop(h)
    mode_base = A[now - 1]
    prev_remain = prev % mode_base
    if dist[now][prev_remain] < cost:
        continue
    for n, c in graph[now]:
        next_remain = n % A[now - 1]
        if prev_remain == next_remain:
            new_cost = cost + c
            if new_cost < dist[n][now % A[n - 1]]:
                dist[n][now % A[n - 1]] = new_cost
                heapq.heappush(h, (new_cost, n, now))

print(-1 if min(dist[N]) == INF else min(dist[N]))
