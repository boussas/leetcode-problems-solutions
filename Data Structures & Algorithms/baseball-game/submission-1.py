class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l = []
        for op in ops :
            if op =="+" :
                l.append(l[-1]+l[-2])

            elif op == "D" :
                l.append(2*l[-1])

            elif op == "C" :
                l.pop()
            else :
                a = int(op) 
                l.append(a)
        return sum(l)


                                