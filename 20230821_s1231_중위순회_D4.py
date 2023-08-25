def preorder(n):
    if n <= N:
        preorder(n*2)
        print(tree2[n], end='')
        preorder(n*2+1)

for t in range(1, 11):
    N = int(input())

    tree2 = ['']*(N+1)

    for i in range(N):
        tmp = list(input().split())
        tree2[int(tmp[0])] = tmp[1]
    print(f'#{t} ',end='')
    preorder(1)
    print()