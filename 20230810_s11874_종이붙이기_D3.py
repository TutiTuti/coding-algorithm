papers = [('|',10),('=',20),("ㅁ",20)]

# TestCase 수
T = int(input())
for t in range(1, T+1):
    # 직사각형 테이프 길이 20*N 길이
    N = int(input())

    a = [['|'], ['='], ['ㅁ']]
    b = [10, 20, 20]
    # N길이 안에 들어갈 수 있는 모든 패턴
    # ans =find_pattern(a, b)


    return_len_n = []
    while True:
        arr = a
        lens = b
        return_pattern = []

        # 패턴의 길이를 담을 리스트
        return_len = []

        # 길이가 n인 리스트 들을 담는 리스트
        # return_len_n = []

        # 길이가 N인 패턴을 카운트
        count = 0

        # arr을 순환
        for i in range(len(arr)):

            # arr 에서 꺼낸 i 패턴의 현재 길이를 구한다.
            now_len = lens[i]

            # 현재 길이가 N 이라면
            if now_len == N:
                count += 1
                # 길이가 충족되서 바로 반환 리스트에 넣어준다.
                return_len_n.append(arr[i])
                # return_len.append(lens[i])
            else:
                # 붙일 수 있는 종이 순환
                for j in papers:

                    # 현재길이에서 종이 하나를 붙였을 때 N길이 이하라면
                    if now_len + j[1] <= N:
                        # 종이를 붙여준다. -> New 패턴
                        a = arr[i] + [j[0]]
                        b = lens[i] + j[1]
                        # 반환 리스트에 추가된 패턴을 넣어준다.
                        return_pattern.append(a)
                        return_len.append(b)
        # 반환 리스트가 전부 N 길이가 아니라면
        if count != len(return_pattern):
            # N길이가 전부 나올 때 까지 돌린다.
            a = return_pattern
            b = return_len
            # return_pattern = find_pattern(return_pattern, return_len)
        else:
            a = return_pattern + return_len_n
            break


    # 모든 패턴의 개수 출력

    print(f'#{t}',len(a))