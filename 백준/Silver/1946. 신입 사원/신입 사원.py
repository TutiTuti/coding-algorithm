import sys;
input = sys.stdin.readline
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key= lambda x: (x[0], x[1]))
    ans = N

    min_v = arr[0][1]
    for i in range(N):
        if arr[i][1] > min_v:
            ans -= 1

        if arr[i][1] < min_v:
            min_v = arr[i][1]

    print(ans)