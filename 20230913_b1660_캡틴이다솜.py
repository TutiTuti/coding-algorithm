'''
5
ans=3
'''
import sys; sys.stdin=open("./20230913_b1660_캡틴이다솜.py", encoding="utf-8");asvcds=input()

N = int(input())

arr = [0]*(N+1)
arr[0] = 0
arr2=[0]*(N+1)
for i in range(1, N+1):
    arr[i] = i + arr[i-1]
    arr2[i] = arr[i] + arr2[i-1]

dp  = [987654321]*(N+1)
for i in range(1, N+1):
    for b in arr2:
        if b >= i:
            if b == i:
                dp[i] = 1
            break
        dp[i] = min(dp[i],1 + dp[i-b])#포탄이 n개 일 때 b만큼의 포탄을 가진 사면체 + 1

print(dp[N])

ans = 0
