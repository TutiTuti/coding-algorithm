n = input()
MOD = 900528
code = input()
answer = 0
char_to_index = {ch: i for i, ch in enumerate(n)}
lenN = len(n)
lenCode = len(code)


for i in range(1, lenCode):
    answer += pow(lenN, i, MOD)

for i in range(lenCode):
    target = code[i]
    j = char_to_index[target]
    tmp = pow(lenN, lenCode - i - 1, MOD)
    answer += j * tmp
    answer %= MOD
answer += 1
print(answer % MOD)
