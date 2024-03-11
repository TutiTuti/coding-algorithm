T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    for a in A:
        for b in range(M):
            if B[b] >= a:
                break
            ans += 1
    print(ans)