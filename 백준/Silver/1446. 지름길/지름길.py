N, D = map(int, input().split())
distance = [i for i in range(D+1)]
shortcuts = [list(map(int, input().split())) for _ in range(N)]

for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    for s, e, shortcut in shortcuts:
        if i == s and e <= D and distance[e] > distance[i] + shortcut:
            distance[e] = distance[i] + shortcut
print(distance[D])