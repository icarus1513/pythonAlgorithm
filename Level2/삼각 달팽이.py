from itertools import chain


def solution(n):
    num = 1
    x, y = -1, 0
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    pid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            pid[x][y] = num
            num += 1
    answer = [i for i in chain(*pid) if i != 0]
    return answer