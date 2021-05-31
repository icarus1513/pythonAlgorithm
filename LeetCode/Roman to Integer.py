class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'M': 1000, 'CM': 900, 'D': 500, 'CD' : 400, 'C': 100, 'XC' : 90, 'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4, 'I' : 1}
        cnt = 0
        answer = 0
        while True:
            if cnt < len(s) - 1:
                temp = s[cnt] + s[cnt + 1]
                if temp in sym:
                    answer += sym[temp]
                    cnt += 2
                else:
                    answer += sym[s[cnt]]
                    cnt += 1
            elif cnt == len(s) - 1:
                    answer += sym[s[cnt]]
                    break
            else:
                break
        return answer