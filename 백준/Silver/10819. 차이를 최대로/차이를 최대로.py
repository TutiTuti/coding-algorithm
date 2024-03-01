def find(n, case):
    global ans
    if n == N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(case[i] - case[i+1])
        ans = max(ans, tmp)
    else:
        tmpCase = case[:]
        for i in range(N):
            tmp = tmpCase[n]
            tmpCase[n] = tmpCase[i]
            tmpCase[i] = tmp
            find(n+1, tmpCase)

N = int(input())
arr = list(map(int, input().split()))

ans = 0

find(0, arr)

print(ans)