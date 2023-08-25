T = int(input())
for t in range(1, T+1):
    n = int(input())

    stack = [1]
    print(f'#{t}')
    print(*stack)

    for i in range(n-1):
        tmp = [0] + stack + [0]
        stack = []

        pop1 = tmp.pop()
        while tmp:
            pop2 = tmp.pop()
            stack.append(pop1 + pop2)
            pop1 = pop2

        print(*stack)