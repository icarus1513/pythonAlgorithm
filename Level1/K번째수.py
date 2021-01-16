def solution(array, commands):
    answer = []
    c_len = len(commands)
    for k in range(c_len):
        i = commands[k][0] - 1
        j = commands[k][1]
        list = array[i:j]
        list = sorted(list)
        print(list)
        answer.append(list[commands[k][2] - 1])

    return answer