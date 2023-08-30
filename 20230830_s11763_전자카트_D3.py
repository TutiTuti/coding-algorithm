def perm(n, k):
    global ans
    if n == k:
        tmp = 0
        # print(p)
        for i in range(0,len(p)-1):
            tmp += arr[p[i]][p[i+1]]
        if ans > tmp:
            ans = tmp
        return
    else:
        for i in range(n):
            if vstd[i] == 0:
                vstd[i] = 1
                p[k] = arr2[i]
                perm(n, k+1)
                vstd[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # arr = s, e >>
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [ x for x in range(N)]
    p = [0] * (N + 1)
    p[0] = p[N] = arr2[0]
    vstd = [0]*N
    vstd[0] = 1

    ans = 98765431
    perm(N, 1)
    print(f'#{t} {ans}')