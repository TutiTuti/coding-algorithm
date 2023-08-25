T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    pattern = 2
    r = c = 0
    arr[r][c] = 1
    while pattern < ((n * n) + 1):
        for i in range(4):
            while 0 <= r + dx[i] < n and 0 <= c + dy[i] < n and arr[r + dx[i]][c + dy[i]] == 0 and pattern < ((n * n) + 1):
                    r += dx[i]
                    c += dy[i]
                    arr[r][c] = pattern
                    pattern += 1

    print(f'#{t}')
    for i in arr:
        print(*i)