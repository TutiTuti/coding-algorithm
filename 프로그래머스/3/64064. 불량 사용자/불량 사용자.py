def solution(user_id, banned_id):
    vstd = ['n' for _ in range(len(user_id))]
    dic = dict()
    dic2 = set()
    def dfs(loc):
        nonlocal vstd
        nonlocal dic
        nonlocal dic2
        # print("LOC " , loc)
        if loc == len(banned_id):
            # print("".join(vstd))
            dic2.add("".join(vstd))
            return
        # print("HERE")
        for i in range(len(user_id)):
            banTmp = banned_id[loc]
            userId = user_id[i]
            # print(banTmp, userId)
            if vstd[i] == 'n' and len(banTmp) == len(userId):

                flag = True
                for j in range(len(banTmp)):
                    if banTmp[j] != '*' and banTmp[j] != userId[j]:
                        flag = False
                        break
                # print("answer " , loc ,flag)
                if flag:
                    vstd[i] = 'y'
                    dfs(loc + 1)
                    vstd[i] = 'n'
        return
    dfs(0)
    answer = 0
    # print(dic2)
    return len(dic2)