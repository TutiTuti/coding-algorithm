
def find(n, count):
    for i in arr[n]:
        if not vstd[i]:
            vstd[i]= 1
            count = find(i, count + 1)

    return count

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())

    arr = [[] for _ in range(N+1)]
    vstd=[0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    ans = find(1, -1)
    print(min(ans, M))
