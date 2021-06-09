class Solution:
    def isValid(self, s: str) -> bool:
        # dic = {'(' : 0, '{' : 0, '[' : 0}
        # for i in s:
        #     if i == '(' or i == '{' or i == '[' :
        #         dic[i] += 1
        #     else:
        #         if i == ')' :
        #             if dic['('] <= 0 :
        #                 return False
        #             else :
        #                 dic['('] -= 1
        #         elif i == '}':
        #             if dic['{'] <= 0 :
        #                 return False
        #             else :
        #                 dic['{'] -= 1
        #         elif i == ']':
        #             if dic['['] <= 0 :
        #                 return False
        #             else :
        #                 dic['['] -= 1
        # if dic['('] != 0 or dic['{'] != 0 or dic['['] != 0:
        #     return False
        # return True
        dic = []
        for i in s:
            if i == '(' or i == '{' or i == '[' :
                dic.append(i)
            else :
                if i == ')' :
                    if not dic:
                        return False
                    elif dic[-1] == '(':
                        dic.pop(-1)
                    else:
                        return False
                elif i == '}':
                    if not dic:
                        return False
                    elif dic[-1] == '{':
                        dic.pop(-1)
                    else :
                        return False
                elif i == ']':
                    if not dic:
                        return False
                    elif dic[-1] == '[' :
                        dic.pop(-1)
                    else:
                        return False
        if not dic :
            return True
        return False