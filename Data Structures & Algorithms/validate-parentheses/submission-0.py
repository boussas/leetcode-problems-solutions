class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        l=[]
        for ch in s:
            if ch in d:
                if not l:
                    return False
                if l[-1]!=d[ch]:
                    return False
                else:
                    l.pop()
            else:
                l.append(ch)
        return not l