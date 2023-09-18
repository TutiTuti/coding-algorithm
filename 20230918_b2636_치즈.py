'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
import sys; sys.stdin=open('./20230918_b2636_치즈.py', encoding='utf-8'); qsdasqwd=input()

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c): # 0인 테두리 값을 -1로 바꿔줌
    time[r][c] = -1
    for k in range(4):
        drr = r + dr[k]
        dcc = c + dc[k]
        if 0 <= drr < N and 0 <= dcc < M:
            if arr[drr][dcc] == 0 and time[drr][dcc] != -1:
                dfs(drr, dcc)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = [[0]*M for _ in range(N)]
Q = deque()
hour = 1

dfs(0, 0)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            for k in range(4):
                drr = i + dr[k]
                dcc = j + dc[k]
                if 0 <= drr < N and 0 <= dcc < M:
                    if time[drr][dcc] == -1: # 치즈의 4방향중에 -1(빈공간)이 있다는 것은 테두리 라는 뜻
                        Q.append([i, j])
                        time[i][j] = 1 # 테두리라는 표시
                        break

while True:
    tmp = deque()
    while Q:
        i, j = Q.popleft()
        if time[i][j] == 0:
            time[i][j] = hour
        for k in range(4):
            drr = i + dr[k]
            dcc = j + dc[k]
            if 0 <= drr < N and 0 <= dcc < M:
                if arr[drr][dcc] != 0 and time[drr][dcc] == 0:
                    tmp.append([drr, dcc])
    if tmp:
        print(time)
        Q = tmp
        hour += 1
    else:
        break


print(arr)
print(time)