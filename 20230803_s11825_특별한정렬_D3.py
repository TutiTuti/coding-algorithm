T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(0, n):
        tmp = i
        for j in range(i, n):
            if i%2 == 0:
                if arr[tmp] < arr[j]:
                    tmp = j

            else:
                if arr[tmp] > arr[j]:
                    tmp = j
        arr[i], arr[tmp] = arr[tmp], arr[i]
    print(f'#{t}',end=' ')
    for i in range(10):
        print(arr[i],end=' ')
    print()