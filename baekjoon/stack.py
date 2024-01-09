class Stack:
    def __init__(self):
        self.dat = []
        self.pos = 0
    def push(self, item):
        self.dat.append(item)
        self.pos += 1
    def pop(self):
        self.pos -= 1
        return self.dat.pop()
    def top(self):
        return self.dat[-1]

def main():
    stack = Stack()
    stack.top()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    print(stack.top()) # 3
    stack.pop()
    stack.pop()
    print(stack.top()) # 5
    stack.push(10)
    stack.push(12)
    print(stack.top()) # 12
    stack.pop()
    print(stack.top()) # 10

main()
 