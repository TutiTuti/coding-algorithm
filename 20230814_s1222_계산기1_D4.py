for t in range(1, 11):
    N = int(input())
    arr = list(input())

    for i in range(1,N,2):
        arr[i], arr[i+1] = arr[i+1] , arr[i]

    stack = []
    for i in arr:
        if i != '+':
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a+b)
    print(f'#{t} {stack[0]}')