def solution(routes):
    answer = 0
    routes.sort(key = lambda x :x[1])
    for i in routes:
        if answer == 0:
            answer += 1
            camera = i[1]
        elif camera < i[0] :
            answer += 1
            camera = i[1]
    return answer