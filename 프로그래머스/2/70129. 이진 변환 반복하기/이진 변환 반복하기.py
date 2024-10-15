def solution(s):
    answer = []
    cycleCnt = 0
    zeroCnt = 0
    while len(s) != 1:
        cycleCnt += 1
        oneCnt = ""
        for i in s:
            if i == '1':
                oneCnt += '1'
            else:
                zeroCnt += 1
        tmp = ""
        tmp2 = len(oneCnt)

        # for i in range(tmp2//2, -1, -1):
        #     print(i)
        #     if tmp2 >= 2 ** i:
        #         for j in range(i, -1, -1):
        #             if 2 ** j <= tmp2:
        #                 tmp += '1'
        #                 tmp2 -= 2 ** i
        #             else:
        #                 tmp += '0'
        #         break
        #     else:
        #         print("N")
        # print(tmp)

        for i in range(tmp2//2, -1, -1):
            if 2 ** i <= tmp2:
                tmp += '1'
                tmp2 -= 2 ** i
            else:
                tmp += '0'
        s = tmp.lstrip('0')


    return [cycleCnt, zeroCnt]