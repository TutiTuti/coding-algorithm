def find(n, case):
    global ans
    if n == N:
        tmp = 0
        for i in range(N-1):
            tmp += abs(case[i] - case[i+1])
        ans = max(ans, tmp)
    else:
        for i in range(N):
            case[n], case[i] = case[i], case[n]
            find(n+1, case)
            case[n], case[i] = case[i], case[n]


N = int(input())
arr = list(map(int, input().split()))
ans = 0
find(0, arr)
print(ans)