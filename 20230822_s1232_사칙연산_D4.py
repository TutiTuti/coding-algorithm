def find_sum(n):

    if type(arr[n][3]) == type(10):
        return arr[n][3]
    else:
        if arr[n][3] == '-':
            return find_sum(arr[n][0]) - find_sum(arr[n][1])
        elif arr[n][3] == '/':
            return find_sum(arr[n][0]) // find_sum(arr[n][1])
        elif arr[n][3] == '*':
            return find_sum(arr[n][0]) * find_sum(arr[n][1])
        elif arr[n][3] == '+':
            return find_sum(arr[n][0]) + find_sum(arr[n][1])

for t in range(1, 11):
    N = int(input())
    # 0=L , 1=R , 2=P, 3=V
    arr = [[0]*4 for _ in range(N+1)]
    for i in range(N):
        # 0=N, 1=V, 2=L, 3=R
        tmp = list(input().split())
        if tmp[1] in '/*-+':
            arr[int(tmp[0])][3] = tmp[1]
            arr[int(tmp[0])][0] = int(tmp[2])
            arr[int(tmp[0])][1] = int(tmp[3])
            arr[int(tmp[2])][2] = int(tmp[0])
            arr[int(tmp[3])][2] = int(tmp[0])
        else:
            arr[int(tmp[0])][3] = int(tmp[1])
    a = find_sum(1)
    print(f'#{t} {a}')