def find_sum():
    for i in range(N, 0, -1):
        if i == K:
            return
        if i % 2 == 0:
            arr[i // 2] += arr[i]
        else:
            arr[(i-1)//2] += arr[i]


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int,input().split())

    arr = [0]*(N+1)

    for i in range(M):
        s, e = map(int,input().split())
        arr[s] = e


    find_sum()
    print(f'#{t} {arr[K]}')