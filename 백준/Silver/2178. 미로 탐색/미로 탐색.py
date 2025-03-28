from collections import deque
n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]
vstd = list([0] * m for _ in range(n))
vstd[0][0] = 1
queue = deque()
dx = [1, 0 ,0, -1]
dy = [0, 1, -1, 0]
queue.append([0,0])
while queue:
    tmp = queue.popleft()
    for i in range(4):
        tx = tmp[0] + dx[i]
        ty = tmp[1] + dy[i]
        if 0 <= tx < m and 0 <= ty < n and maze[ty][tx] == 1 and not vstd[ty][tx]:
            vstd[ty][tx] = vstd[tmp[1]][tmp[0]] + 1
            queue.append([tx, ty])

print(vstd[n-1][m-1])