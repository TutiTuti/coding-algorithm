'''
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
최빈수는 8이 된다.
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "1"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    dict = {}

    for i in arr:
        value = dict.get(i,0)
        if value == 0:
            dict[i] = 1
        else:
            dict[i] = value + 1
    max=0
    key = list(dict.keys())
    for i in range(len(key)):
        if dict.get(key[i])==dict.get(max):
            max = max if max > key[i] else key[i]
        else:
            max = (max if dict.get(key[i]) < dict.get(max)  else key[i])
    print("#{} {}".format(n,max))
