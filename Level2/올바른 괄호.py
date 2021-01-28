def solution(s):
    answer = True
    list = []  ## 스택
    for i in s:
        if i == "(":
            list.append(i)
        else:
            try:
                list.pop()
            except:
                return False

    if len(list) != 0:
        return False

    return True