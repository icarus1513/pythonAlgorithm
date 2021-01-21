from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0 :
        return len(cities) * 5
    else :
        for i in cities:
            i = i.lower()
            if i in cache :
                answer += 1
                cache.remove(i)
            else :
                answer += 5
                if len(cache) >= cacheSize:
                    cache.popleft()
            cache.append(i)
    return answer