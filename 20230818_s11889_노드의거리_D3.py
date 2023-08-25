def bfs(s, e):

    Q = [s]
    visited[s] = 1

    while Q:
        tmp = Q.pop(0)
        if tmp == e:
            return visited[tmp] - 1

        for w in range(1, V+1):
            if adj[tmp][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[tmp] + 1
    return 0



T = int(input())
for t in range(1, T+1):

    V, E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)

    for i in range(E):
        s, e = map(int,input().split())
        adj[s][e] = 1
        adj[e][s] = 1

    start_n, end_n = map(int,input().split())
    ans = bfs(start_n, end_n)

    print(f'#{t} {ans}')