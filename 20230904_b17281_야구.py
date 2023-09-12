import sys; sys.stdin=open('./t5.txt');import time;start = time.time();


'''─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────'''


# iterable에서 원소 개수가 r개인 순열 뽑기
from itertools import permutations;


def game(lst):
    print(lst)

    score = 0
    # 1번 타자 인덱스 : 0을 값으로 가지고 있는 8번 인덱스가 4번 타자니까 5번 인덱스가 무족건 1번 타자이다.
    # attack은 지금 타석에 서야하는 번호를 의미하기도 한다.
    attack = 5

    # 게임 이닝 수 만큼 반복
    for i in range(N):
        base = 0    # 베이스 초기화
        out = 0     # 아웃카운트 초기화
        while out < 3:  # 3아웃까지 반복
            cur = lst[attack]   # 현재 타자 번호
            if not hit[i][cur]: # 게임[이닝수][타자번호] 의 값이 0이라면
                out += 1    # 아웃 카운트 + 1
            else:
                base <<= hit[i][cur]    # 필드에 있는 선수 먼저 이동
                base |= 1 << (hit[i][cur]-1)    # 타자 이동
                home = base & ~7  # ~7 > 000 & base 해서 3루 이상의 값을 뽑아온다.
                while home:
                    score += 1 # 점수 + 1
                    home -= home & -home # 자릿수 8만 빼기 (이거 진짜 신기)
                base &= 7 #  들어온 사람들 다 빼주고 n루 선수들만 남기기
            attack += 1 # 다음 선수 타자석 이동
            attack %= 9 # %9해서 10번선수 못나오게 하기 (후보인가?)
    return score # 점수 리턴

# 게임 이닝수 받기
N = int(sys.stdin.readline().strip())
# 이닝당 선수들이 낼 수 있는 점수를 입력 받는다.
hit = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 최대 점수 ans
ans = 0

# permutations 순열 함수를 사용하여 만든 순열 리스트를 순환한다.
for case in permutations((1, 2, 3, 4, 5, 6, 7, 8), 8):
    # 순열 끝에 0을 붙이고 game 함수를 실행한다.
    temp = game(list(case) + [0]) # 지금 순서로 점수 구하기
    ans = max(ans, temp) # 지금 구한 최대수랑 기존 촤대수 비교
print(ans)

'''─────────────────────────────────────────────────────────────d────────────────────────────────────────────────────────────────────────────────────────────'''

print( start - time.time())