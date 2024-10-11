def solution(k, tangerine):
    answer = 0
    lst = dict()
    for i in tangerine:
        tmp = lst.get(i, 0)
        lst[i] = tmp+1
    lst = dict(sorted(lst.items(), key=lambda item: (item[1], item[0]), reverse=True))
    cnt = 0
    # print(list(lst.keys()))
    for i in lst.keys():
        cnt += lst[i]
        answer += 1
        if cnt >= k:
            break
    return answer