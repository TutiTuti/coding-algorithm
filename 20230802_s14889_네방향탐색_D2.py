T = int(input())
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
for t in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i - x[k] < N and 0 <= j - y[k] < N: 
                    tmp = arr[i][j] - arr[i-x[k]][j-y[k]]
                    ans += tmp * (1 if tmp >= 0 else -1)
    print(f'#{t} {ans}')