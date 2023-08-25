T = int(input())
for t in range(1, T+1):
    stack = []
    ans =0
    arr = input()
    for i in range(len(arr)):
        if arr[i] == '(':
            if arr[i+1] == '(':
                stack.append(arr[i])
            else:
                ans += len(stack)
        elif arr[i] == ')':
            if arr[i-1] == ')':
                stack.pop(-1)
                ans += 1
    print(f'#{t} {ans}')