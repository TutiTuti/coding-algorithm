def preorder(n):
    global ans
    if n:
        ans += 1
        preorder(tree[n][0])
        preorder(tree[n][1])

T = int(input())
for t in range(1, T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))

    tree = [ [0] * 3 for _ in range(E+2)]

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if not tree[p][0] != 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

        tree[c][2] = p
    ans = 0
    preorder(N)
    # print(ans)
    print(f'#{t} {ans}')