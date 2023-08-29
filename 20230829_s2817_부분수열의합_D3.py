def find_a(n, sum):
    global ans
    if sum > K:
        return

    if n == N:
        if sum == K:
            ans += 1
        return

    visit[n] = 0
    find_a(n+1, sum)

    visit[n] = 1
    sum += arr[n]
    find_a(n+1, sum)



T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    visit = [0] * (N)
    ans = 0
    find_a(0, 0)

    print(f'#{t}',ans)