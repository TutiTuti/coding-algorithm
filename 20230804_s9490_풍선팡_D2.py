T = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max = 0
    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            for w in range(1, arr[i][j]+1):
                for k in range(4):
                    if 0<=i+(dx[k]*w) < N and 0<= j+(dy[k]*w) < M:
                        sum += arr[i+(dx[k]*w)][j+(dy[k]*w)]
            if max < sum:
                max = sum
    print(f'#{t} {max}')