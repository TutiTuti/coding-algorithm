import heapq
def solution(operations):
    tmp = []
    for i in operations:
        tmp2 = i.split(" ")
        if tmp2[0] == "I":
            heapq.heappush(tmp, int(tmp2[1]))
        else:
            if tmp:
                if tmp2[1].startswith("-"):
                    heapq.heappop(tmp)
                else:
                    tmp.sort()
                    tmp.pop()

    answer = []
    tmp.sort()
    if len(tmp) == 1:
        answer.append(tmp[0])
        answer.append(tmp[0])
    elif len(tmp) > 1:
        answer.append(tmp[-1])
        answer.append(tmp[0])
    else:
        answer.append(0)
        answer.append(0)
    return answer