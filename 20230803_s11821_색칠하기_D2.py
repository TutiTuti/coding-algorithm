T = int(input())
for t in range(1, T+1):
    ans = 0
    arr = [[0 for _ in range(10)] for _ in range(10)]
    n = int(input())
    for _ in range(n):
        color = list(map(int, input().split()))
        for i in range(color[1], color[3]+1):
            for j in range(color[0], color[2]+1):
                if arr[i][j] != 0 and arr[i][j] != color[4] and arr[i][j] != 3:
                    arr[i][j] = 3
                    ans += 1
                else:
                    arr[i][j] = color[4]
    print(f'#{t} {ans}')
