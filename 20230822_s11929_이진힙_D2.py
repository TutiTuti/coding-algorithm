T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    heap = [0] * (N+1)
    a =1
    while a != N+1:
        heap[a] = arr[a-1]
        if heap[a] < heap[a//2]:
            c = a
            while c:
                if heap[c] < heap[c // 2]:
                    heap[c], heap[c//2] = heap[c//2], heap[c]
                    c//=2
                else:
                    break
        a+=1
    ans = 0
    b = N
    while b:
        b//=2
        ans += heap[b]
    print(f'#{t}',ans)