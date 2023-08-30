def perm(n, k):
    global flag
    if n == k:
        baby = 0
        card1 = []
        card2 = []
        for i in range(6):
            if i <= 2:
                card1.append(p[i])
            else:
                card2.append(p[i])
        if card1[0] == card1[1] == card1[2]:
            baby += 1
        elif card1[0]+2 == card1[1]+1 == card1[2]:
            baby += 1

        if card2[0] == card2[1] == card2[2]:
            baby += 1
        elif card2[0]+2 == card2[1]+1 == card2[2]:
            baby += 1

        if baby == 2:
            flag = 1
        return # 체크
    else:
        for i in range(n):
            if vstd[i] == 0:
                vstd[i] = 1
                p[k] = arr[i]
                perm(n, k+1)
                vstd[i] = 0


T = int(input())
for t in range(1, T+1):
    flag = 0
    arr = list(map(int,input()))
    N = len(arr)
    p = [0] * N
    vstd = [0] * N
    perm(N, 0)
    print(f'#{t} {flag}')