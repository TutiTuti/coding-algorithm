T = int(input())
for t in range(1, T+1):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0


    for i in range(n):
        j = 0
        while j < n:
            if arr[i][j] == 1:
                s = 0
                ccc = 0
                while 0<= j+s < n and arr[i][j+s] == 1:
                    s += 1
                    ccc += 1
                if ccc == k:
                    ans += 1
                j += s
            else:
                j += 1

    for q in range(n):
        w = 0
        while w < n:
            if arr[w][q] == 1:
                s = 0
                ccc = 0
                while 0 <= w+s < n and arr[w+s][q] == 1:
                    s += 1
                    ccc += 1
                if ccc == k:
                    ans += 1
                w += s
            else:
                w += 1


    print(f'#{t}',ans)