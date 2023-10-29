def binary_tree(node):
    global index
    if node<(2**N):
        binary_tree(node*2)
        ans[node] = arr[index]
        index += 1
        binary_tree((node*2) + 1)


N = int(input())
ans = [0] * (2 ** N)
arr = list(map(int, input().split()))
index = 0
binary_tree(1)

for i in range(1,N+1):
    for j in range(int(2**(i-1)), int(2**i)):
        print(ans[j], end=' ')
    print('')