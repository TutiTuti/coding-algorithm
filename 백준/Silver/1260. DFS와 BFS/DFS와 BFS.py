from collections import deque
n, m, v = map(int, input().split())

dist = list([0] * (n + 1) for _ in range(n + 1))
for _ in range(m):
    s, e = map(int, input().split())
    dist[s][e] = dist[e][s] = 1
dfs_answer = []
vstd = [0] * (n + 1)


def dfs(now, depth):
    vstd[now] = 1
    dfs_answer.append(now)
    for i in range(1, n+1):
        if not vstd[i] and dist[now][i]:
            dfs(i, depth + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    vstd[start] = 1
    print(start, end=" ")
    while queue:
        now = queue.popleft()
        for i in range(1, n + 1):
            if not vstd[i] and dist[now][i]:
                vstd[i] = 1
                print(i, end=" ")
                queue.append(i)


dfs(v, 0)
print(*dfs_answer)
vstd = [0] * (n + 1)
bfs(v)