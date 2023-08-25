for T in range(int(input())):
    n = int(input())
    room = list(map(int, input().split()))

    max = 0
    for i in range(n):
        tmp = i
        for j in range(i,n):
            if room[i] <= room[j]:
                tmp += 1
        if max < n - tmp:
            max = n - tmp

    print(f'#{T+1} {max}')