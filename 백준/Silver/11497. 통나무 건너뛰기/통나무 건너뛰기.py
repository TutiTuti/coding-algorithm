T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    listA = []
    listB = []
    for i in range(0, N, 2):
        listA.append(arr[i])
    for i in range(1, N, 2):
        listB.append(arr[i])
    listA += sorted(listB, reverse=True)
    ans = 0
    for i in range(N-1):
        ans = max(ans, abs(listA[i] - listA[i+1]))
    print(ans)