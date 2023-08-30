def check(n, k):

    if n < 3:
        return 0
    else:
        counting = [0] * 11
        for i in k:
            counting[i] += 1

        if 3 in counting:
            return 1

        for i in range(9):
            if counting[i] != 0 and counting[i+1] != 0 and counting[i+2] != 0:
                return 1
        return 0


T = int(input())
for t in range(1, T+1):

    arr = list(map(int,input().split()))

    ans =0
    player1 = []
    player2 = []
    for i in range(12):

        if i%2 ==0:
            player1.append(arr[i])
            ans = check((i//2) + 1, player1)

        else:
            player2.append(arr[i])
            ans = check((i//2) + 1, player2)

        if ans:
            if i%2==1:
                ans = 2
            break

    print(f'#{t} {ans}')