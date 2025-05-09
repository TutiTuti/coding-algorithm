N, S, M = map(int , input().split())
songs = list(map(int, input().split()))
lst = [set() for _ in range(N + 1)]

if 0 <= S + songs[0] <= M:
    lst[0].add(S + songs[0])
if 0 <= S - songs[0] <= M:
    lst[0].add(S - songs[0])

for i in range(1, N):
    for j in lst[i-1]:
        if 0 <= j + songs[i] <= M:
            lst[i].add(j + songs[i])
        if 0 <= j - songs[i] <= M:
            lst[i].add(j - songs[i])

if not lst[N-1]:
    print(-1)
else:
    print(max(lst[N-1]))
