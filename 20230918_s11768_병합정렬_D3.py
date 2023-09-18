'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
import sys; sys.stdin=open('./20230918_s11768_병합정렬_D3.py', encoding='utf-8'); qsdasqwd=input()

def merge_sort(a):
    global cnt

    if len(a) < 2:
        return a

    mid = len(a) // 2

    left = []
    for x in range(mid):
        left.append(a[x])

    right = []
    for x in range(mid, len(a)):
        right.append(a[x])

    left = merge_sort(left)
    right = merge_sort(right)


    if left[len(left)-1] > right[len(right)-1]:
        cnt += 1

    tmp = []
    l = r = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] < right[r]:
                tmp.append(left[l])
                l += 1
            else:
                tmp.append(right[r])
                r += 1
        elif l < len(left):
            for x in range(l, len(left)):
                tmp.append(left[x])
            l = len(left)
        else:
            for x in range(r, len(right)):
                tmp.append(right[x])
            r = len(right)

    return tmp



T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0

    sortArr = merge_sort(arr)
    print(f'#{t} {sortArr[N//2]} {cnt}')