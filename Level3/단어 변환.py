def solution(begin, target, words):
    answer = 0
    visit = [0] * len(words)
    cnt = []
    tmp = 0
    def dfs(word,depth,visit,cnt):
        if word == target:
            cnt.append(depth)
            return
        else:
            for i in range(len(words)):
                if visit[i] == 1:
                    continue

                tmp = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    visit[i] = 1
                    dfs(words[i],depth+1,visit,cnt)
                    visit[i] = 0

    dfs(begin,0,visit,cnt)
    if len(cnt) != 0 :
        answer = min(cnt)
    return answer