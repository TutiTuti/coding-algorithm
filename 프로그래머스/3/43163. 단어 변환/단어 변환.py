def solution(begin, target, words):
    if target not in words:
        return 0

    answer = bfs(begin, target, words, 0, 987654321)
    return answer


def bfs(begin,target,words, n, answer):

    if begin == target:
        return min(answer, n)

    if n >= answer:
        return answer
    for i in words:
        for j in range(len(begin)):
            now = list(begin)
            word = list(i)
            now.pop(j)
            word.pop(j)
            # print("".join(now),  "".join(word))
            if "".join(now) == "".join(word):
                words.remove(i)
                answer = bfs(i, target, words, n+1, answer)
                words.append(i)
    return answer