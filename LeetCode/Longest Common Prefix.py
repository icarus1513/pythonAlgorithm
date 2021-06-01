class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # start = strs[0]
        # for i in range(1,len(strs)):
        #     tmp = ""
        #     for char in start:
        #         if char in strs[i]:
        #             tmp += char
        #     start = tmp
        # return start
        strs = sorted(strs, key=lambda x: len(x))

        if len(strs) == 0:
            return ""
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]