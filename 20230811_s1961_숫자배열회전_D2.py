for T in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr90 = [ [0]*n for _ in range(n) ]
    arr180 = [ [0]*n for _ in range(n) ]
    arr270 = [ [0]*n for _ in range(n) ]
    for i in range(n):
        for k in range(n):
            #90도
            arr90[i][n-1-k] = arr[k][i]
            #180도
            arr180[n-1-i][n-1-k] = arr[i][k]
            #270도
            arr270[n-1-k][i] = arr[i][k]

    print("#{}".format(T+1))
    for i in range(n):
        a90 = a180 = a270 = ""
        for k in range(n):
            a90 = a90 + str(arr90[i][k])
            a180 = a180 + str(arr180[i][k])
            a270 = a270 + str(arr270[i][k])
        print(a90,a180,a270)