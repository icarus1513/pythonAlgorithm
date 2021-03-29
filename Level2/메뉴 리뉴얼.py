from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        tmp = []
        for menu in orders:
            comb = combinations(sorted(menu), i)
            tmp += comb
        count = Counter(tmp)
        if len(count) != 0 and max(count.values()) != 1:
            answer += [''.join(f) for f in count if count[f] == max(count.values())]

    return sorted(answer)