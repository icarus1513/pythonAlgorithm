def solution(citations):
    citations.sort()
    len_cit = len(citations)
    for idx,value in enumerate(citations):
        if value >=  len_cit - idx:
            return len_cit-idx
    return 0


