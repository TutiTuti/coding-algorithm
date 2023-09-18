'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''
import sys; sys.stdin=open('./20230918_s11772_이진탐색_D3.py', encoding='utf-8'); qsdasqwd=input()

def binary_search(l, h, t):
    global cnt
    flag = 0

    while l <= h:

        mid = (l+h)//2

        if lista[mid] == t:
            cnt += 1
            return

        elif lista[mid] < t:
            if flag == 1:
                return

            l = mid + 1
            flag = 1
        else:
            if flag == -1:
                return
            h = mid - 1
            flag = -1

    return


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lista = list(map(int, input().split()));lista.sort()
    listb = list(map(int, input().split()))

    cnt = 0

    for t in listb:
        binary_search(0, N-1, t)
    print(f'#{t} {cnt}')