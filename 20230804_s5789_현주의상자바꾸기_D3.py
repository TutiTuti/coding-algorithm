T = int(input())
for t in range(1, T + 1):
    n, q = map(int,input().split())
    arr = [0 for i in range(n)]
    for i in range(1, q+1):
        l, r = map(int,input().split())
        for j in range(n):
            if l <= j+1 <= r:
                arr[j] = i
    print(f'#{t}', *arr)