import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}

        def dp(idxS, idxP):
            if (idxS, idxP) not in memory:
                if idxP == len(p):
                    answer = idxS == len(s)
                else:
                    first_match = idxS < len(s) and p[idxP] in {s[idxS], '.'}
                    if idxP + 1 < len(p) and p[idxP + 1] == '*':
                        answer = dp(idxS, idxP + 2) or (first_match and dp(idxS + 1, idxP))
                    else:
                        answer = first_match and dp(idxS + 1, idxP + 1)
                memory[idxS, idxP] = answer
            return memory[idxS, idxP]

        return dp(0, 0)
