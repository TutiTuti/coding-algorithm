import bisect
from itertools import product

def solution(info, query):
    infoDic = {}
    cases = list(product([True, False], repeat=4))

    for i in info:
        info_lst = i.split()
        for case in cases:
            # 기존 코드: key = ""
            # 수정된 부분: 리스트 컴프리헨션 사용
            key = ''.join(info_lst[j] if case[j] else '-' for j in range(4))
            if key not in infoDic:
                infoDic[key] = []
            infoDic[key].append(int(info_lst[4]))

    # 정렬
    for k in infoDic.keys():
        infoDic[k].sort()

    answer = []
    for i in query:
        z,_,x,_,c,_,d,j = i.split()

        queryKey = ''.join([z,x,c,d])
        scoreLst = infoDic.get(queryKey, [])

        point = int(j)

        s = 0
        e = len(scoreLst)-1
        index = len(scoreLst)  # 기본값은 scoreLst의 길이로 초기화

        while s <= e:
            m = (s + e) // 2
            if scoreLst[m] < point:
                s = m + 1
            else:  
                index = m  
                e = m - 1

        answer.append(len(scoreLst) - index) 
    return answer

