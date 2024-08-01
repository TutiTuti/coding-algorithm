
N = int(input())

arr = list(range(1, N+1))
start = 0
end = N - 1
check = 0

while start != end:

    if check == 0:
        # 버리기
        start = (start + 1) % N
    else:
        # 뒤로 붙이기
        end = (end + 1) % N
        arr[end] = arr[start]
        start = (start + 1) % N
    check = (check + 1 ) % 2

print(arr[start])