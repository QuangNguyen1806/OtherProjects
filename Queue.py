class ArrayStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)
        

class Queue:
    def __init__(self):
        self.enqueue_stack = ArrayStack()
        self.dequeue_stack = ArrayStack()

    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()

    def enqueue(self, item):
        self.enqueue_stack.push(item)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            if self.enqueue_stack.is_empty():
                return None
            else:
                self._transfer_elements()
        return self.dequeue_stack.pop()

    def _transfer_elements(self):
        while not self.enqueue_stack.is_empty():
            self.dequeue_stack.push(self.enqueue_stack.pop())

    def __len__(self):
        return self.enqueue_stack.size() + self.dequeue_stack.size()

    def first(self):
        if self.dequeue_stack.is_empty():
            if self.enqueue_stack.is_empty():
                return None
            else:
                self._transfer_elements()
        return self.dequeue_stack.top()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Dequeue:", q.dequeue())  # Output: 1
    q.enqueue(4)
    print("Dequeue:", q.dequeue())  # Output: 2
    print("Dequeue:", q.dequeue())  # Output: 3
    print("Dequeue:", q.dequeue())  # Output: 4
    print("Dequeue:", q.dequeue())  # Output: None
    print("Is empty?", q.is_empty())  # Output: True
    print("Length:", len(q))  # Output: 0
