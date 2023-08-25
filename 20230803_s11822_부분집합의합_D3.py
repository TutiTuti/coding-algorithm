def find_subset(i):
    global c
    for w in range(2):
        b[i-1] = w
        if i-1 == 0:
            num = sum_subset(b)
            if num[0] == n and num[1] == k:
                c += 1
        else:
            find_subset(i - 1)

            
def sum_subset(bit):
    sum = 0
    count = 0
    for i in range(len(bit)):
        if bit[i]:
            count += 1
            sum += A[i]
    return [count, sum]


A = [1,2,3,4,5,6,7,8,9,10,11,12]
b = [0] * 12
T = int(input())
for t in range(1,T+1):
    c = 0
    n, k = map(int, input().split())
    find_subset(12)
    print(f'#{t} {c}')