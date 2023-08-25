pair = {
    '}' : '{',
    ')' : '(',
        }

T = int(input())
for t in range(1, T+1):
    stack = []
    arr = list(input())
    ans = 1
    for i in arr:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}' or i == ')':
            if len(stack) == 0:
                ans = 0
                break
            check = stack.pop(-1)
            if check != pair[i]:
                ans = 0
                break
    if stack:
        ans = 0
    print(f'#{t} {ans}')