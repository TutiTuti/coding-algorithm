def dfs(v):
    visited[v] = 1
    # print(v, end=' ')

    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

T = int(input())
for t in range(1, T+1):
    V, E = map(int,input().split())
    temp = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s, e = temp[i][0], temp[i][1]
        adj[s][e]  = 1

    dfs(S)
    flag = 0
    if visited[G]==1:
        flag = 1

    print(f'#{t} {flag}')