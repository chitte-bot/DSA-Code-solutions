class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack after push:")
s.display()

print("Popped element:", s.pop())

print("Stack after pop:")
s.display()
