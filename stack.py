

class Stack():

    '''
    Constructor
    '''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    '''to inspect'''

    def __str__(self):
        return str(self.items)

    

if __name__ == '__main__':
    s = Stack()

    print(s)
