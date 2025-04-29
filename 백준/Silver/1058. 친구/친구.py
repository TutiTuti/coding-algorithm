N = int(input())
lst = list(input().strip() for _ in range(N))

INF = 999999999999
dist = list([INF] * N for _ in range(N))
# 거리 측정
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        elif lst[i][j] == 'Y':
            dist[i][j] = 1

# 중간 지점
for k in range(N):
    # 시작 지점
    for i in range(N):
        # 도착 지점
        for j in range(N):
            # 시작 - 도착 VS 시작 - 중간 - 도착 : 크기 비교
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
answer = 0
for i in range(N):
    tmp = 0
    for j in dist[i]:
        if 0 < j <= 2:
            tmp += 1
    answer = max(answer, tmp)
print(answer)
