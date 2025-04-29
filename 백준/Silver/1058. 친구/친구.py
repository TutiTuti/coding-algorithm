from collections import deque

N = int(input())

lst = list(input().strip() for _ in range(N))

answer = 0
queue = deque()
def bfs(index):
    vstd = [0] * N
    vstd[index] = 1
    value = 0
    queue.append([index, 0])
    while queue:
        tmp = queue.popleft()
        if tmp[1] == 2:
            continue
        for i, friend in enumerate(lst[tmp[0]]):
            if friend == 'Y' and not vstd[i]:
                value += 1
                vstd[i] = 1
                queue.append([i, tmp[1] + 1])
    return value

for i in range(N):
    answer = max(answer, bfs(i))

print(answer)