
T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [ list(input()) for _ in range(N)]

    ans = ''

    for i in range(N):
        for j in range(N):
            row_word = ''
            col_word = ''

            if 0 <= i+M-1 < N :
                for k in range(M):
                    col_word += arr[i+k][j]

            if 0 <= j+M-1 < N :
                for k in range(M):
                    row_word += arr[i][j+k]
            if row_word:    
                flag = True
                for k in range(M//2):
                    if row_word[k] != row_word[-k - 1]:
                        flag = False
                if flag:
                    ans = row_word

            if col_word:
                flag = True
                for k in range(M // 2):
                    if col_word[k] != col_word[-k - 1]:
                        flag = False
                if flag:
                    ans = col_word
    print(f'#{t} {ans}')