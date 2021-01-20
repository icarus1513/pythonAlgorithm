def boom(b, m, n):
    pop = set()
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
    for i, j in pop:
        b[i][j] = 0
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop)


def solution(m, n, board):
    count = 0
    tmp = list(map(list, zip(*board)))
    while True:
        pop = boom(tmp, m, n)
        if pop == 0: return count
        count = count + pop
