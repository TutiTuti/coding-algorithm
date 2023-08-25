def bfs(r,c):

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]


    queue = []
    queue.append((r,c))

    while queue:
        tmp = queue.pop(-1)
        rr = tmp[0]
        cc = tmp[1]
        if arr[rr][cc] == 3:
            return 1
        visited[rr][cc]=1
        for i in range(4):
            nx = rr + dx[i]
            ny = cc + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and arr[nx][ny]!=1:
                    queue.append((nx,ny))

    return 0


# T = int(input())
for t in range(1, 11):
    qweqw = int(input())
    N = 100
    arr = [ list(map(int,input())) for _ in range(N)]
    visited = [[ 0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                a = bfs(i,j)
                print(f'#{t} {a}')