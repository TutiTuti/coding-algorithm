T = int(input())
for t in range(1, T + 1):
    target = input()
    word = input()
    ans = 0
    for i in range(len(word) - len(target) + 1):
        if word[i] == target[0]:
            index =0
            flag = 1
            for j in range(i, i+len(target)):
                if word[j] != target[index]:
                    flag = 0
                if flag:
                    ans = 1
                index += 1
    print(f'#{t} {ans}')
