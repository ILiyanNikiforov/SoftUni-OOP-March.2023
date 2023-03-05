class Stack:
    def __init__(self):
        self.data = []

    def push(self, element:str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


my_stack = Stack()

my_stack.push("1")
my_stack.push("2")
my_stack.push("3")
my_stack.push("4")

print(my_stack)
print(my_stack.pop())
print(my_stack.top())
print(my_stack)

