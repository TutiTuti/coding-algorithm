T = int(input())

for t in range(1, T+1):
    n = int(input())
    cards = list(map(int,input()))
    count = [0] * 10

    max_i = 0
    max = 0
    for c in cards:
        count[c] += 1

        if count[c] >= max:
            if max == count[c]:
                if max_i < c:
                    max_i = c
            else:
                max_i = c
                max = count[c]

    print(f'#{t} {max_i} {max}')
