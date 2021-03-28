def solution(n, stations, w):
    answer = 0
    idx = 0
    st = 1
    while st <= n:
        if idx < len(stations) and st >= stations[idx] - w:
            st = stations[idx] + w + 1
            idx += 1
        else:
            st += 2 * w + 1
            answer += 1

    return answer