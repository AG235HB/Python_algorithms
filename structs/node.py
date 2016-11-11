class Node:
    
    def __init__(self, value, next):
        self.data = value
        self.next = next
        self.prev = None

    def set_node(self, value):
        #print(value)
        self.data = int(value)
        #print(self.data)

    def set_next(self, value):
        self.next = int(value)