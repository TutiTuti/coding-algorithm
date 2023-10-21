import sys, heapq
input = sys.stdin.readline

INF = int(1e9)                     # 무한 의미(10억)
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]   # 노드의 정보를 담을 리스트
distance = [INF] * (V+1)           # 최단 거리 테이블 무한으로 초기화

# 간선 정보 입력 받기
for _ in range(E):
    a, b, c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))


def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))  # 시작노드로 가기 위한 최단경로를 0하여 Q에 삽입
    distance[start] = 0

    while Q:
        cur_cost, now = heapq.heappop(Q)  # 현재 최단 거리가 가장 짧은 노드 정보 꺼내기

        if distance[now] < cur_cost:      # 계산된 거리보다 현재 거리가 더 크면 볼 필요X
            continue

        for next, next_cost in graph[now]:       # b번 노드, 비용 c
            cost = cur_cost + next_cost          # 현재 거리 + 다음에 갈 거리

            if cost < distance[next]:            # 현재 노드를 거쳐서 이동하는게 더 짧은 경우
                distance[next] = cost            # 최단 거리 갱신
                heapq.heappush(Q, (cost, next))  # 비용 기준으로 최소힙에 삽입


dijkstra(start)


# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])