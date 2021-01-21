def solution(record):
    answer = []
    arr = dict()
    history = []
    for i in record:
        tmp = i.split()
        if tmp[0] == "Enter" :
            arr[tmp[1]] = tmp[2]
            history.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == "Leave" :
            history.append([tmp[1], "님이 나갔습니다."])
        elif tmp[0] == "Change" :
            arr[tmp[1]] = tmp[2]

    for i in history :
        answer.append(arr[i[0]] + i[1])
    return answer