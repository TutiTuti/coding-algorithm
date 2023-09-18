'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
import sys; sys.stdin=open('./20230918_s11770_퀵정렬_D3.py', encoding='utf-8'); qsdasqwd=input()

def quick_sort(a, l, h):
    p = a[l]
    i, j = l, h
    while i <= j:
        while i <= j and a[i] <= p:i += 1
        while i <= j and a[j] >= p:j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[j], a[l] = a[l], a[j]
    return j


def quick_sort1(a,l,h):
    if l < h:
        s = quick_sort(a, l, h)
        quick_sort1(a, l, s-1)
        quick_sort1(a, s+1, h)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quick_sort1(arr, 0, N-1)
    print(f'#{t} {arr[N//2]}')