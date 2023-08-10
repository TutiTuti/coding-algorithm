def dfs(v):
    visited[v] = 1
    for w in range(1, 100):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)


for t in range(1, 11):
    T, E = map(int,input().split())
    temp = list(map(int,input().split()))


    adj = [[0] * (100) for _ in range(100)]
    visited = [0] * (100)

    for i in range(E):
        s, e = temp[i*2], temp[i*2+1]
        adj[s][e]  = 1

    dfs(0)
    flag = 0
    if visited[99]:
        flag = 1

    print(f'#{t} {flag}')