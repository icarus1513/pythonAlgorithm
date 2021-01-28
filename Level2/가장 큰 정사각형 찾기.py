from itertools import chain


def solution(board):
    w = len(board[0])
    h = len(board)

    for x in range(1, h):
        for y in range(1, w):
            mins = min(board[x - 1][y - 1], board[x - 1][y], board[x][y - 1])
            if board[x][y] == 0 or mins == 0:
                continue
            board[x][y] = max(mins + 1, board[x][y])

    return max(list(chain.from_iterable(board))) ** 2