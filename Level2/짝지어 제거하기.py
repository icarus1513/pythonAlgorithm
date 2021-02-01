def solution(s):
    answer_list = []
    s = list(s)
    idx = 0
    while(idx != len(s)):
        answer_list.append(s[idx])
        idx += 1
        if len(answer_list) > 1:
            if(answer_list[-1] == answer_list[-2]):
                answer_list.pop()
                answer_list.pop()
    if len(answer_list) == 0:
        return 1
    else :
        return 0