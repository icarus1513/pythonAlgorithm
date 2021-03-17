# #defaultdict 사용해보기
# def solution(genres, plays):
#     answer = []
#     tmp = dict()
#     arr = []
#     if len(genres) == 1:
#         return [0]
#     for i in range(len(genres)):
#         if genres[i] in tmp:
#             tmp[genres[i]] += plays[i]
#             arr.append([i,genres[i],plays[i]])
#         else :
#             tmp[genres[i]] = plays[i]
#             arr.append([i,genres[i],plays[i]])

#     arr = sorted(arr, key = lambda x : (x[1], -x[2], x[0]))
#     print(arr)
#     ## 장르별 시간 뽑기
#     return answer

from collections import defaultdict


def solution(genres, plays):
    answer = []
    g_d = defaultdict(lambda: 0)
    t_l = defaultdict(lambda: [])

    for i in range(len(genres)):
        g_d[genres[i]] += plays[i]
        t_l[genres[i]].append((plays[i], i))

    g_d = sorted(g_d.items(), key=lambda x: x[1], reverse=True)

    for i in t_l:
        t_l[i] = sorted(t_l[i], key=lambda x: x[0], reverse=True)[:2]

    while len(g_d) > 0:
        g_max = g_d.pop(0)
        for i in t_l:
            if i == g_max[0]:
                if len(t_l[i]) > 1:
                    answer.append(t_l[i][0][1])
                    answer.append(t_l[i][1][1])
                else:
                    answer.append(t_l[i][0][1])

    return answer