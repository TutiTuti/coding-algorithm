num_dict = {  # 일의 자릿수 규칙 딕셔너리에 대입
    0: [0], 1: [1], 5: [5], 6: [6],  # 주기 1인 숫자들
    2: [2, 4, 8, 6],  
    3: [3, 9, 7, 1],  
    4: [4, 6],  
    7: [7, 9, 3, 1],  
    8: [8, 4, 2, 6],  
    9: [9, 1]
}

t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    a, b = map(int, input().split())  # 입력 받기

    c = a % 10  # 밑수의 1의 자리
    d = len(num_dict[c])  # 주기 길이
    e = (b - 1) % d  # 1-based index 조정
    result = num_dict[c][e]  # 결과 값

    # 0번 컴퓨터는 없으므로 10번 컴퓨터로 변환
    if result == 0:
        result = 10  

    print(result)
