class MaxStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def push(self, e):
        if self.is_empty():
            self.stack.append((e, e))
        else:
            current_max = self.stack[-1][1]
            new_max = max(current_max, e)
            self.stack.append((e, new_max))

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack[-1][0]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack.pop()[0]

    def max(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack[-1][1]

