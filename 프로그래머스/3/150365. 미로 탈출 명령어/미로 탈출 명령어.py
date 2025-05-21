import heapq;
def solution(n, m, x, y, r, c, k):
    answer = 'z' * k

    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]
    dl = ["d", "r", "l", "u"]


    lst = []
    heapq.heappush(lst, ["", 0, x, y])

    while lst:
        record, cnt, row, col = heapq.heappop(lst)
        if cnt == k:
            if row == r and col == c:
                return record
            else:
                continue

        # if cnt >= k or ((abs(row - r) + abs(col - c)) % 2 != (k - cnt) % 2):
        #     continue

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 1 <= nr <= n and 1 <= nc <= m:
                dist = abs(nr - r) + abs(nc - c)
                remain = k - cnt - 1
                if remain >= dist and (remain - dist) % 2 == 0:
                    heapq.heappush(lst, [record + dl[i], cnt + 1, nr, nc])


    return "impossible"