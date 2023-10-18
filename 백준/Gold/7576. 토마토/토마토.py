import sys;
from collections import deque;
# sys.stdin=open('./Test.py', encoding='utf-8')
# _ = input()

# sys.stdin=open('./input.txt', encoding='utf-8')
# T = int(input())


dx = [0,0,-1,1]
dy = [1,-1,0,0]

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
Q = deque()
day = [[0]*n for _ in range(m)]


for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            Q.append((i,j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and arr[xx][yy] == 0:
            arr[xx][yy] = 1
            day[xx][yy] = day[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))

max = 0

flag = True

for i in range(m):
    for j in range(n):
        if day[i][j] > max:
            max = day[i][j]

        if arr[i][j] == 0:
            flag = False

if flag:
    print(max)
else:
    print(-1)