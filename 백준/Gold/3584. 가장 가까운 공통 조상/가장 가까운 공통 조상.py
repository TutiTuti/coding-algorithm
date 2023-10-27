import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    T = int(input())
    tree = [[0]*3 for _ in range(T+1)]
    for _ in range(T-1):
        a, b = map(int, input().split())
        tree[b][2] = a
        if tree[a][0]:
            tree[a][1] = b
        else:
            tree[a][0] = b

    t1, t2 = map(int, input().split())
    ans = 0

    findparent = [t1]
    target = t1
    while tree[target][2]:
        if tree[target][2] == t2:
            ans = t2
            break
        findparent.append(tree[target][2])
        target = tree[target][2]
    target = t2

    while not ans:
        if tree[target][2] in findparent:
            ans = tree[target][2]
            break
        target = tree[target][2]
    print(ans)