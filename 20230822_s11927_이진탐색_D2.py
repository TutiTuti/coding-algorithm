def inorder(n):
    global V
    if n <= N:
        inorder(n * 2)
        heap[n] = V
        V += 1
        inorder(n * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = [0] * (N + 1)
    V = 1
    inorder(1)
    print(f'#{tc} {heap[1]} {heap[N // 2]}')