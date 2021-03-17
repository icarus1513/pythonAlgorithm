def solution(n, results):
    answer = 0
    win, lose = {}, {}
    for i in range(1, n + 1):
        win[i], lose[i] = set(), set()

    for i in range(1, n + 1):
        for j in results:
            if j[0] == i:
                win[i].add(j[1])
            if j[1] == i:
                lose[i].add(j[0])
        for tmp in lose[i]:
            win[tmp].update(win[i])
        for tmp in win[i]:
            lose[tmp].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer