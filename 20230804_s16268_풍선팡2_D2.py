T = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for t in range(1, T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max =0
    for i in range(n):
        for j in range(m):
            sum = arr[i][j]
            for k in range(4):
                if 0<= i+dx[k] < n and 0<= j+dy[k] < m:
                    sum += arr[i+dx[k]][j+dy[k]]
            if max < sum:
                max = sum
    print(f'#{t} {max}')