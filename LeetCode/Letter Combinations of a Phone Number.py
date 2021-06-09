class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []
        for char in digits:
            letter = num[char]
            if not answer:
                for i in letter:
                    answer.append(i)
            else:
                tmp = []
                for j in letter:
                    for i in range(len(answer)):
                        tmp.append(answer[i] + j)
                answer = tmp
        return answer
