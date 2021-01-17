def solution(arr):
    answer = []
    now = arr[0]
    answer.append(now)
    for i in range (1,len (arr)) :
        if now == arr[i] :
            continue
        else :
            now = arr[i]
            answer.append(now)
    return answer