def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    attack = 0
    for i in range(0, len(targets)):
        if attack > targets[i][0]:
            continue
        answer += 1
        attack = targets[i][1]
    
    return answer