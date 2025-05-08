
def find(comb, len):
    if len == T:
        ans.append(comb[:])
        return
    for i in range(N):
        if not vstd[i]:
            vstd[i] = 1
            comb.append(lst[i])
            find(comb, len + 1)
            comb.pop()
            vstd[i] = 0

N, T = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
vstd = [0] * N
ans = []
find([], 0)

for i in ans:
    print(*i)
