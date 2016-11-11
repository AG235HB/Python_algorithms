class Stack:

    def __init__(self):
        import node
        self.stck = []
        self.top = 0

    def push(self, item):
        import node
        itm = node.Node(item)
        self.stck.append(itm)
        self.top += 1
        return None

    def pop(self):
        if len(self.stck)==0:
            return None
        else:
            self.stck.remove(self.stck[len(self.stck)-1])
            self.top -= 1

    def peek(self):
        if len(self.stck)==0:
            return None
        else:
            return self.stck[self.top-1].data

    def show(self):
        for item in self.stck:
            print(item.data)