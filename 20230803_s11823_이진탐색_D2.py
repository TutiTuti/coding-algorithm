def binary(n, key):
    count = 0
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if key == mid:
            return count
        elif mid > key:
            end = mid
        else:
            start = mid
        count += 1
    return -99


T = int(input())
for t in range(1, T+1):
    p, a, b = map(int,input().split())
    a1 = binary(p, a)
    b1 = binary(p, b)
    if a1 > b1:
        win='B'
    elif a1<b1:
        win='A'
    else:
        win='0'

    print(f'#{t} {win}')