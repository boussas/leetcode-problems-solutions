class MinStack:

    def __init__(self):
        self.l=[]
        self.minL=[]

    def push(self, val: int) -> None:
        self.l.append(val)
        v=self.minL[-1] if self.minL else val
        self.minL.append(min(val,v))

    def pop(self) -> None:
        self.l.pop()
        self.minL.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minL[-1]