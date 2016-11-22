class Queue:

    def __init__(self):
        import node
        self.q = []
        self.first = node.Node(0,None,None)
        self.last = node.Node(0,None,None)

    def enqueue(self, item):
        import node
        self.q.append(node.Node(item,None,None))

    def dequeue(self):
        if len(self.q)==0:
            return None
        else:
            out = self.q[0].data
            self.q.remove(self.q[0])
            return out