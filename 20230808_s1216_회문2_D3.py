for _ in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]

    ans = -1
    size = 100
    while size > 0:
        for i in range(100):
            for j in range(100-size+1):
                flag  = 1
                for k in range(size):
                    if arr[i][j+k] != arr[i][j+size-k-1]:
                        flag = 0
                        break
                if flag:
                    ans = size
                    break
        for i in range(100):
            for j in range(100-size+1):
                flag = 1
                for k in range(size):
                    if arr[j+k][i] != arr[j+size-k-1][i]:
                        flag = 0
                        break
                if flag:
                    ans = size
                    break
        if ans != -1:
            break
        size -= 1

    print(f'#{T}', ans)