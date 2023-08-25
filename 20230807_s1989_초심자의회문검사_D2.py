T = int(input())
for t in range(1, T+1):
    ans = 1
    word = input()
    for i in range(len(word)//2):
        if word[i] != word[-i -1]:
            ans = 0
            break
    print(f'#{t} {ans}')