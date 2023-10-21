# 터치 X
import sys;
import heapq
input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]
dis = [INF] * (V+1)
# vstd = [0] * (V+1)


for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

def find(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dis[start] = 0
    while Q:
        now_c, now_n = heapq.heappop(Q)

        if dis[now_n] < now_c:
            continue

        for next_n, next_c in adj[now_n]:
            cost = now_c + next_c
            if cost < dis[next_n]:
                dis[next_n] = cost
                heapq.heappush(Q, (cost, next_n))
find(start)

for i in range(1, V+1):
    if dis[i] == INF:
        print('INF')
    else:
        print(dis[i])
