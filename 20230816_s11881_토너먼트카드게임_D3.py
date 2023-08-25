def division_find(arr):
    if len(arr) < 2:
        return arr[0]

    mid = ((len(arr)-1)//2) + 1

    low = division_find(arr[:mid])
    high = division_find(arr[mid:])

    # 1 가위 2 바위 3 보
    man1 = rcp_list[low]
    man2 = rcp_list[high]
    if (man1 == 1 and man2 == 2) or \
            (man1 == 2 and man2 == 3) or \
            (man1 == 3 and man2 == 1):
        return high
    else:
        return low

T = int(input())
for t in range(1,T+1):
    N = int(input())
    rcp_list = list(map(int, input().split()))
    man_num = [i for i in range(N)]

    winner = division_find(man_num)
    print(f'#{t}',winner+1)