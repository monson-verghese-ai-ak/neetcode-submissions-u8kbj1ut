class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        closed_brckts = [')', '}', ']']
        open_brckts = ['(', '{', '[']
        dic = {
            open_brckts[i]:closed_brckts[i] for i in range(len(closed_brckts))
        }
        for i in s:
            if i in open_brckts:
                stk.append(i)
            else:
                if len(stk) == 0:
                    return False
                elif dic[stk[-1]] != i:
                    return False
                else:
                    stk.pop()
        if len(stk) > 0:
            return False
        return True