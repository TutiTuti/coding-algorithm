import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):

    money = 0

    N = int(input())
    stock_list = list(map(int,input().split()))
    max_sv = stock_list[N - 1]
    for _ in range(N-1,-1,-1):
        tmp = stock_list.pop()
        if max_sv < tmp:
            max_sv = tmp
        elif tmp < max_sv:
            money += (max_sv - tmp)
    print(money)
