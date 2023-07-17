'''
창용마을에는 N명의 사람이 살고 있다.
사람은 1번부터 N번까지 번호가 있다.
두 사람은 서로를 알고 있는 관계일 수도, 아닐 수도 있다.
두 사람이 서로 아는 관계거나 몆 사람을 거쳐서 알 수있는 관계라면,
이러한 살마들을 모두 다 묶어서 하나의 무리라고 한다.
몆개의 무리가 있는지 구하여라

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
같은 관계는 반복해서 주어지지 않는다.
'''

''' input 파일 가져오기 코딩 '''
import sys
inputversion = "5"
sys.stdin = open(".\input\input"+inputversion+".txt", "r")

print("START")
for T in range(int(input())):
    n, m = map(int,input().split())
    muri = set([])
    for i in range(m):
        man1, man2 = map(int,input().split())
        for muri_detail in muri:
            if man1 in muri_detail or man2 in muri_detail:
                print(man1)
