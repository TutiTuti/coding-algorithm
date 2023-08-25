T = int(input())
for t in range(1, T+1):
    arr = list(input())
    stack = []
    pop = -1
    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
            pop += 1
        else:
            if stack[pop] != arr[i]:
                stack.append(arr[i])
                pop += 1
            else:
                stack.pop(pop)
                pop -= 1
    print(f"#{t} {len(stack)}")