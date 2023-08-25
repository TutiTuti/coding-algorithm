for T in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max = arr[0]
    min = 987654321
    for i in range(n - m + 1):
        tmp_sum = 0
        for j in range(m):
            tmp_sum += arr[i+j]
        if max < tmp_sum:
            max = tmp_sum
        if min > tmp_sum:
            min = tmp_sum
    print(f'#{T+1} {max-min}')