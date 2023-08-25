import math;

T = int(input())
for t in range(1, T+1):
    n = float(input())
    i = 0
    list_n = ''
    while i != 13:
        n *= 2
        # print('1 ',n)
        list_n += (str(int(n//1)))
        # print('2 ', int(n//1))
        n %= 1
        if math.isclose(n, 0):
            break
        i += 1
    if i == 13:
        ans = ('overflow')
    else:
        ans = (list_n)
    print(f'#{t} {ans}')