T = int(input())
for t in range(1, T+1):
    m, n = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(m)]

    max_v = 0
    for i in range(m):
        max = 0
        for j in range(n):
            if arr[i][j] == 1:
                max += 1
                if max_v < max:
                    max_v = max
            else:
                max = 0

    for i in range(n):
        max = 0
        for j in range(m):
            if arr[j][i]:
                max += 1
                if max_v < max:
                    max_v = max
            else:
                max = 0


    print(f'#{t}',max_v)
