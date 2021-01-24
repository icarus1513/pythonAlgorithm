from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    ## 모든경우의 수
    tmp = []
    for i in range(1, col + 1):
        tmp.extend(combinations(range(col), i))

    ## 유일성 만족
    first = []
    for i in tmp:
        arr = [tuple([item[key] for key in i]) for item in relation]
        if len(set(arr)) == row:
            first.append(i)

    ## 희소성 만족

    answer = set(first[:])
    for i in range(len(first)):
        for j in range(i + 1, len(first)):
            if len(first[i]) == len(set(first[i]).intersection(set(first[j]))):
                answer.discard(first[j])
    return len(answer)


#재풀이