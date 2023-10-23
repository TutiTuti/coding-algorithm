from collections import deque
Q = deque()
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
INF = int(1e9)
brr = [[INF] * N for _ in range(N)]

# r, c, 좌표를 넣는다.
Q.append((0, 0))
brr[0][0] = 0
while Q:
    r, c = Q.popleft()
    if r == N-1 and c == N-1:
        continue
    elif 0 <= r < N-1 and 0 <= c < N-1:
        for ar, ac in [[0, 1], [1, 0]]:
            nr = r + ar
            nc = c + ac
            if brr[nr][nc] <= brr[r][c]:
                continue
            cost = brr[r][c]
            if arr[r][c] <= arr[nr][nc]:
                cost += (arr[nr][nc] - arr[r][c] + 1)
            if cost < brr[nr][nc]:
                brr[nr][nc] = cost
                Q.append((nr, nc))

    elif r == N-1 and 0 <= c < N:
        nr = r
        nc = c + 1
        if brr[nr][nc] <= brr[r][c]:
            continue
        cost = brr[r][c]
        if arr[r][c] <= arr[nr][nc]:
            cost += (arr[nr][nc] - arr[r][c] + 1)
        if cost < brr[nr][nc]:
            brr[nr][nc] = cost
            Q.append((nr, nc))

    elif 0 <= r < N and c == N-1:
        nr = r + 1
        nc = c
        if brr[nr][nc] <= brr[r][c]:
            continue
        cost = brr[r][c]
        if arr[r][c] <= arr[nr][nc]:
            cost += (arr[nr][nc] - arr[r][c] + 1)
        if cost < brr[nr][nc]:
            brr[nr][nc] = cost
            Q.append((nr, nc))

print(brr[N-1][N-1])
