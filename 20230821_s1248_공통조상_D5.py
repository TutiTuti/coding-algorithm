def count_father(n):
    global father_number
    if n:
        father_number += 1
        count_father(tree[n][0])
        count_father(tree[n][1])


def first(son1):
    f1 = tree[son1][2]

    if father_list[f1] == 0 and f1 != 0:
        father_list[f1] = 1
        first(f1)
        
        
def second(son2):
    f2 = tree[son2][2]
    ans = 0
    if f2 != 0:
        if father_list[f2] == 1:
            return f2
        else:
            ans = second(f2)
    return ans


T = int(input())
for t in range(1, T+1):
    N,E,F,S = map(int,input().split())
    arr = list(map(int,input().split()))
    tree = [[0]*3 for _ in range(N+1)]


    for i in range(E):
        p, c  = arr[i*2], arr[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            if tree[p][0] > c:
                tree[p][0], tree[p][1] = c, tree[p][0]
            else:
                tree[p][1] = c
        tree[c][2] = p

    father_list = [0] * (N+1)
    first(F)
    a = second(S)
    father_number = 0
    count_father(a)
    print(f'#{t} {a} {father_number}')