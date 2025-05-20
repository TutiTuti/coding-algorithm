def solution(n, bans):
    bans = sorted(bans, key=calOrd)

    for word in bans:
        cnt = calOrd(word)
        if cnt <= n:
            n += 1
    res = []
    while n > 0:
        n -= 1  # 보정

        res.append(calChr(n % 26 + 1))
        n //= 26

    return ''.join(reversed(res))


def calChr(n):
    return chr(n + 96)

def calOrd(n):
    cnt = 0
    for i, j in enumerate(reversed(n)):
        cnt += (ord(j) - 96) * 26 ** i
    return cnt
