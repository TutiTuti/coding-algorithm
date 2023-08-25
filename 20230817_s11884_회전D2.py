T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [0] + list(map(int,input().split()))
    
    front = 1
    back = 0
    
    for i in range(M):
        arr[back] = arr[front]
        front = (front+1)%(N+1)
        back =  (back+1)%(N+1)
    print(f'#{t} {arr[front]}')