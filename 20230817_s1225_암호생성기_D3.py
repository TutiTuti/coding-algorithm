for t in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))


    queue = []

    rear = front = -1

    for i in range(8):
        rear += 1
        queue.append(arr[i])

    code = 1
    while front != rear:
        front += 1
        tmp = queue[front]
        tmp -= code

        code += 1
        rear += 1


        if tmp > 0:
            queue.append(tmp)
        else:
            queue.append(0)
            break


        if code == 6:
            code = 1


    print(f'#{T}', end=' ')

    for i in range(8):
        print(queue[front+1+i], end=' ')
    print()