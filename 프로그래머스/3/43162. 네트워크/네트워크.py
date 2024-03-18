def solution(n, computers):
    arr = [-1] * (n + 1)
    for a in computers:
        tmp = []
        ccc = -1
        for i in range(n):
            if a[i]:
                tmp.append(i)
                if ccc == -1 and arr[i] == -1:
                    ccc = i
                elif ccc == -1 and arr[i] != -1:
                    ccc = arr[i]
        for i in tmp:
            if arr[i] != ccc and arr[i] != -1:
                bbb = arr[i]
                for j in range(n):
                    if arr[j] == bbb:
                        arr[j] = ccc
            arr[i] = ccc
        
    ans = len(set(arr)) - 1
    return ans