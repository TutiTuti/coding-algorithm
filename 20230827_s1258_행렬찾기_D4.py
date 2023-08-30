def find_arr(r,c):
    global ans
    count = 0
    row = 0
    col = 0
    flag =1
    while flag:

        if 0 <= r + row < N and arr[r + row][c] != 0 and arr2[r + row][c] == 0:
            col = 0
            while True:
                if 0 <= r + row < N and 0 <= c + col < N and arr[r + row][c + col] != 0 and arr2[r+row][c+col] == 0:
                    arr2[r + row][c + col] = 1
                    count += 1
                    col += 1
                else:
                    if arr[r+row+1][c+col-1] == 0:flag=0
                    break
            row += 1
        else:

            break
    ans += 1
    ans_a.append((row*col,row,col))
    ans_in.append(ans)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = [[0 for _ in range(N)] for _ in range(N)]

    ans = 0
    ans_a = []
    ans_in = []


    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and arr2[i][j] == 0:
                find_arr(i, j)

    ans_a.sort(key=lambda x: (x[0], x[1]))
    print(f'#{t} {ans} ', end='')
    for i in ans_a:
        print(i[1], i[2], end=' ')
    print()