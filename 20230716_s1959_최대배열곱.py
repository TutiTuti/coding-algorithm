'''
마주보는 두 배열의 곱의 최대값을 구하라
예시
[0][0][ 1][5][3]
 X  X   X  X  X
[3][6][-7][5][4]
 0  0  -7  25 12 -> 30

가장 첫 줄에는 테스트케이스 개수 T, 그 아래로 각 테스트케이스가 주어지며
첫 번쨰 줄 N, M
두 번쨰  줄 Ai
세 번쨰 줄 Bj 가 주어진다
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "2"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

# TestCase T를 입력받아 T회 반복
for T in range(int(input())):
    # 배열 A B의 크기 n,m을 입력받음
    n, m = map(int,input().split())
    #배열 a, b를  공백으로 split() 하여 입력받아 list에 저장
    arr_a = list(map(int,input().split()))
    arr_b = list(map(int,input().split()))
    # 곱의 최대값 ans를 0으로 초기화
    ans = 0
    #긴 배열은 arr_long 짧은 배열은 arr_short로 설정
    arr_long = arr_a if len(arr_a) > len(arr_b) else arr_b
    arr_short = arr_a if len(arr_a) < len(arr_b) else arr_b
    '''
         [3][6][7][2][4]
    1 :  [1][2][3]
    2 :     [1][2][3]
    3 :        [1][2][3]
       ( 크기5 - 크기3 + 1 ) 회 만큼 마주볼 수 있음
    '''
    # 긴배열길이 - 짧은배열 길이 + 1 회 만큼 반복
    for i in range(len(arr_long) - len(arr_short) + 1):
        # 임시로 저장할 곱의합 max 변수를 0으로 초기화
        max=0
        # 짧은 배열의 크기 만큼 반복
        for j in range(len(arr_short)):
            # max 값을 각 마주보는 칸에 합한다.
            max += (arr_long[j+i] * arr_short[j])
        # 기존의 ans와 max중 큰값을 ans에 저장한다.
        ans = ans if ans > max else max
    # 테스트케이스 번호와 곱의 최대값 ans를 출력한다.
    print(f"#{T+1} {ans}")
