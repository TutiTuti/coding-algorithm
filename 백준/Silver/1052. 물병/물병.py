N, K = map(int,input().split())

bottle_num = N

buy = 0

dept = 1
while bottle_num > K:

    sum_bottle = bottle_num // 2
    rest_bottle = bottle_num % 2

    tmp = 0
    tmp_b = sum_bottle
    while tmp_b > 1:
        if tmp_b % 2:
            tmp_b - 1
            tmp += 1
        tmp_b //= 2
    if tmp_b + tmp + rest_bottle <= K:
        break

    if rest_bottle != 0:
        buy += 2**(dept) - 2**(dept-1)
        sum_bottle += 1

    bottle_num = sum_bottle

    dept += 1

print(buy)