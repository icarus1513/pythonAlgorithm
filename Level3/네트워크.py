from collections import deque


def dfs(computers, visit, start):
    queue = deque([start])
    while queue:
        j = queue.pop()
        if visit[j] == 0:
            visit[j] = 1
        for i in range(0, len(computers)):
            if computers[j][i] == 1 and visit[i] == 0:
                queue.append(i)


def solution(n, computers):
    answer = 0
    visit = [0] * n
    start = 0
    while 0 in visit:
        if visit[start] == 0:
            dfs(computers, visit, start)
            answer += 1
        start += 1
    return answer