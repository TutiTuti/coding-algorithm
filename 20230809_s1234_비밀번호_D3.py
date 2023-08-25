for t in range(1, 11):
    stack = []
    a, n = map(int, input().split())

    n = list(str(n))

    flag = 1
    i = 0
    check = 1
    while flag:
        if i+1 < len(n):
            if n[i] == n[i+1]:
                n.pop(i+1)
                n.pop(i)
                check = 0
        if i == len(n):
            if check:
                break
            else:
                check = 1
                i = -1
        i += 1
    print(f'#{t}',int(''.join(n)) )