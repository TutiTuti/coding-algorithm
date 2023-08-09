import sys
sys.stdin = open(".\input\input8.txt", "r")

for T in range(1, 11):
    n = int(input())
    m = list(map(int, input().split()))
    total_view = 0
    for i in range(n):
        left = True
        right = True

        tmp_l1 = m[i]   
        tmp_l2 = 987654321

        tmp_r1 = m[i]
        tmp_r2 = 987654321

        # 옆 2개까지의 건물을 검사한다.
        for j in range(1, 3):

            if i - j >= 0:
                # 옆 건물이 더 높다면 조망권의 수은 음수가 나온다.
                tmp_l1 = m[i] - m[i - j]
                if tmp_l1 < 1:
                    left = False
                if tmp_l2 > tmp_l1:
                    tmp_l2 = tmp_l1

            if i + j < n:
                tmp_r1 = m[i] - m[i + j]
                if tmp_r1 < 1:
                    right = False
                if tmp_r2 > tmp_r1:
                    tmp_r2 = tmp_r1

        if left and right:
            if tmp_r2 > tmp_l2:
                total_view += tmp_l2
            else:
                total_view += tmp_r2

    print(f'#{T} {total_view}')