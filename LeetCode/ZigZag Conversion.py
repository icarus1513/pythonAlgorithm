class Solution:
    def convert(self, s: str, numRows: int) -> str:
        routine = numRows * 2 - 2
        answer = ""
        zigzag = [[] for row in range(numRows)]
        if numRows == 1:
            return s
        for idx, val in enumerate(s):
            if idx % routine < numRows:
                index = idx % routine
                zigzag[index].append(val)
            else:
                # idx % routine
                index = routine - (idx % routine)
                zigzag[index].append(val)
        for i in zigzag:
            answer += "".join(i)
        print(answer)
        return answer
