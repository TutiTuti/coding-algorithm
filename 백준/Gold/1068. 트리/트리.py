n = int(input())
leaf = list(map(int, input().split()))
delete = int(input())

def dfs(now):
    leaf[now] = -2
    for i in range(n):
        if now == leaf[i]:
            dfs(i)
dfs(delete)
ans = 0
for i in range(n):
    if leaf[i] != -2 and i not in leaf:
        ans += 1
print(ans)