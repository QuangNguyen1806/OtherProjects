from collections import deque

class MidStack:
    def __init__(self):
        self.stack = []
        self.deque = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def push(self, e):
        self.stack.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack.pop()

    def mid_push(self, e):
        if len(self.stack) % 2 == 0:
            mid_index = len(self.stack) // 2
        else:
            mid_index = (len(self.stack) // 2) + 1
        
        while len(self.stack) > mid_index:
            self.deque.appendleft(self.stack.pop())

        self.stack.append(e)

        while self.deque:
            self.stack.append(self.deque.popleft())

