for T in range(1, 11):
    n = int(input())
    m = list(map(int, input().split()))
    total_view = 0
    for i in range(n):
        left = True
        right = True

        tmp_left = 987654321
        tmp_right = 987654321

        # 옆 2개까지의 건물을 검사한다.
        for j in range(1,3):

            if (i - j) >= 0:
                # 옆 건물이 더 높다면 조망권의 수은 음수가 나온다.
                if (m[i] - m[i - j]) < 1:
                    left = False
                if tmp_left > (m[i] - m[i - j]):
                    tmp_left = (m[i] - m[i - j])
            
            if (i + j) < n:
                tmp_r1 = (m[i] - m[i + j])
                if tmp_right < 1:
                    right = False
                if tmp_right > (m[i] - m[i + j]):
                    tmp_right = (m[i] - m[i + j])
            
        if left and right:
            if tmp_right > tmp_left:
                total_view += tmp_left
            else:
                total_view += tmp_right

    print(f'#{T} {total_view}')