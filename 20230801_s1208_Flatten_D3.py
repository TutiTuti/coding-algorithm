for t in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))

    while n+1:
        max = [0, 0]
        min = [arr[0], 0]
        for i in range(100):
            if arr[i] > max[0]:
                max[0] = arr[i]
                max[1] = i
            if arr[i] < min[0]:
                min[0] = arr[i]
                min[1] = i

        arr[max[1]] -= 1
        arr[min[1]] += 1
        n -= 1
    print(f'#{t} {max[0]-1 - min[0] + 1    }')

        
            
        
        