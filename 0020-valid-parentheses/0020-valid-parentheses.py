class Solution:
    def isValid(self, s: str) -> bool:
        PAR = {")":"(", "}":"{", "]":"["}
        open_b = PAR.values()
        closed_b = PAR.keys()
        stk = deque()
        for p in s:
            if p in open_b:
                stk.append(p)
            elif p in closed_b:
                if not stk or PAR[p] != stk.pop():
                    return False 
        return len(stk) == 0