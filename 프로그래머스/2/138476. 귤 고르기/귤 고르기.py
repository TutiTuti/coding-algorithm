def solution(k, tangerine):
    answer = 0
    lst = dict()
    for i in tangerine:
        tmp = lst.get(i, 0)
        lst[i] = tmp+1
    
    for i in sorted(lst.values(), reverse=True):
        answer += 1
        k -= i
        if k <= 0:
            break
    return answer