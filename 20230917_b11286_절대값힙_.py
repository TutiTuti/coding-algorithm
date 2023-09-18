'''
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0

'''
import sys; sys.stdin=open('./20230917_b11286_절대값힙_.py', encoding='utf-8'); qsdasqwd=input()


def compare(s, p): # 자식 부모 인덱스가 주어졌을 때 
    # 자식 노드의 절대값이 더 작을 때  or 자식,부모 노드의 절대값이 같으나 실제 값은 자식 노드의 값이 더 작다면 1리턴 아니면 0리턴
    return arr[s][0] < arr[p][0] or ( arr[s][0] == arr[p][0] and arr[s][1] < arr[p][1])



def arr_push(value):
    global bot # 현재 리스트 끝 번호
    bot += 1 # 리스트 += 1
    arr[bot] = value # 리스트 끝에 입력받은 값을 넣는다.
    s = bot # 끝 번호 복사
    p = s >> 1 # 끝 인덱스의 부모 인덱스 번호
    while p: # 부모인덱스가 root 번호가 아닐 때 까지
        if compare(s, p): # 자식 부모 노드 크기 비교헀을 때 자식이 더 작다면
            arr[s], arr[p] = arr[p], arr[s] # 위치 바꿔주기
        else: # 자식, 부모가 같은 크기인 위치까지 왔다는 것
            break # break 아래는 볼 필요도 없음 어차피 (더 크니까)
        p >>= 1 # 자식 노드 위치로 이동
        s >>= 1 # 자식의 자식 노드 위치로 이동 

def arr_pop():
    global bot
    if not bot: # empty list
        return 0, 0
    tmp = arr[1]
    end_node = arr[bot]
    bot -= 1 # 맨윗값 뺐으니 리스트 크기를 1 줄여줌
    arr[1] = end_node # 맨 끝을 root node 로 올림

    p = 1 # root에 가장 큰 값이 왔으니 다시 bot 까지 내려줘야함
    while p <= bot:
        m = p # 가장 큰값의 위치
        l, r = m << 1 , (m << 1) | 1 # 왼, 우 자식의 위치
        if l <= bot and compare(l, m): # 왼쪽노드값이 bot보다는 위에있고 값이 더 작다면
            m = l # m위치를 l로 옮겨줌
        if r <= bot and compare(r, m): # 우측노드값이 bot보다는 위에있고 값이 더 작다면
            m = r
        if m ^ p : # m옮길려는 위치와 p의 값이 다르다면
            arr[m], arr[p] = arr[p], arr[m]
            p = m # 위치를 바꾸었으니 가장 큰값 위치 이동
        else:
            break # 값이 같다면 > 연속되는 수 > 바꿀필요가 없다.
    return tmp # 처음 꺼냈던 가장 작은 값을 리턴


N = int(input())

arr = [[0,0] for _ in range(100_101)]
bot = 0
for _ in range(N):
    num = int(input())
    if num:
        arr_push([abs(num), num])
    else:
        print(arr_pop()[1])