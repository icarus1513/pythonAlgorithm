class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            tmp = []
            tmp.append(s[i])
            for j in range(i+1,len(s)):
                ## str 안에 있는 문자 확인하기
                char = s[j]
                if char in tmp :
                    break
                    if answer < subs_len :
                        answer = subs_len
                else:
                    tmp.append(char)
            subs_len = len(tmp)
            if answer < subs_len :
                    answer = subs_len
        return answer