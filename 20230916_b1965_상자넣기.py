'''
8
1 6 2 5 7 3 5 6

ans = 5
'''
import sys; sys.stdin=open('./20230916_b1965_상자넣기.py', encoding='utf-8'); qsdasqwd=input()

N = int(input())
arr = list(map(int,input().split()))

dp = [1]*(N)
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))