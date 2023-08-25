def count(arr):
    counting = [0]*10
    ans = []
    for i in arr:
        counting[change[i]] += 1
        
    for i in range(10):
        for _ in range(counting[i]):
            ans.append(key[i])

    return ans

change = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9,
}

key = list(change.keys())

T = int(input())
for t in range(1, T+1):
    n, m = input().split()
    sw_arr = list(input().split())
    ans_arr = count(sw_arr)
    print(f'#{t}')
    print(*ans_arr)