import sys;
sys.setrecursionlimit(10000)
def find_ss(arr, r, c, count):
    count += 1
    arr[r][c] = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        if 0<= r+dx[i] < N and 0 <= c+dy[i] < M:
            if arr[r+dx[i]][c+dy[i]] == 1:
                count = find_ss(arr, r+dx[i], c+dy[i], count)
    return count

N, M, K = map(int,input().split())

arr = [[0]*M for _ in range(N)]
for i in range(K):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1


max = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            aa = find_ss(arr, i, j, 0)

            if aa > max:
                max = aa

print(max)