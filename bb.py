class stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
s=stack()

print(s.isempty())
s.push(6)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isempty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())