def find(n, v):
    global ans
    if not 0 <= v <= M:
        return
    if v == M:
        ans = n
        return
    find(n+1, v*2)
    find(n+1, int(str(v)+'1'))

N, M = map(int, input().split())
ans = -1
find(1, N)
print(ans)