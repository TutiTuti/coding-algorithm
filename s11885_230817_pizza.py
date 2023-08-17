def enq(data):
    global rear
    global front

    global inpz

    if (rear+1) % (size+1) == front:
        front = (front + 1) % (size+1)
    rear = (rear + 1) % (size+1)
    inpizza[rear] = data



def deq():
    global front
    front = (front+1)%(size+1)
    return inpizza[front]


T = int(input())
for t in range(1, T+1):
    rear = front = 0
    size, num = map(int,input().split())
    arr = list(map(int,input().split()))

    # 몆번 피자 들어갈 상태인가.
    inpz = 0

    # 오븐 상태
    inpizza = [0]*(size+1)

    # pizza input oven
    for i in range(size):
        enq(i)
        inpz += 1

    # 하나 남을 떄 까지 무한 반복 하자.
    while True:
        tmp = deq()
        if tmp != -1:
            arr[tmp] //= 2
            if arr[tmp] == 0:
                if sum(arr) == 0:
                    print(f'#{t}', tmp+1)
                    break
                if inpz < num:
                    enq(inpz)
                    inpz += 1
                else:
                    enq(-1)
            else:
                enq(tmp)
        else:
            enq(tmp)