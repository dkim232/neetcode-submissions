class MinStack:

    def __init__(self):
        self.stack = []
        self.levelMin = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.levelMin:#pushing onto empty stack
            self.levelMin.append(val)
        else:#not an empty stack
            curMin = self.levelMin[-1]
            newMin = min(val, curMin)
            self.levelMin.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.levelMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.levelMin[-1]