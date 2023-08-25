T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max = 0
    for i in range(0, n - m + 1):
        for j in range(0, n - m+ 1):
            tmp = 0
            for k in range(i, i + m):
                for w in range(j, j + m):
                    tmp += arr[k][w]

            if tmp > max:
                max = tmp
    print(f'#{t} {max}')