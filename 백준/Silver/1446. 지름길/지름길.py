
N, D = map(int, input().split())
dist = [i for i in range(D+1)]
shortcuts = [list(map(int, input().split())) for _ in range(N)]

for i in range(D+1):
    dist[i] = min(dist[i], dist[i-1]+1)

    for s, f, l in shortcuts:
        if i == s and f <= D:
            d =dist[i] + l
            if dist[f] > d:
                dist[f] = dist[i] + l
print(dist[D])