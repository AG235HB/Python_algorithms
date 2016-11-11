class LinkedList:

    def __init__(self):
        import node
        #self.ll = []
        self.ll = None

    def add_node(self, value):
        import node
        #if len(self.ll)==0:
        #    new = node.Node(value)
        #    new.next = new
        #    new.prev = new
        #    self.ll.append(new)
        #else:
        #    new = node.Node(value)
        #    new.next = self.ll[0]
        #    new.prev = self.ll[len(self.ll)-2]
        #    self.ll.append(new)

        self.ll = node.Node(value, self.ll)

    #def del_node(self, node):
    #    import node

    def insert_after(self, llnode, value):
        import node

        new = node.Node(value)
        new.next = llnode.next
        new.prev = llnode
        llnode.next = new

    def show(self):
        for i in range(0,len(self.ll),1):
            print(str(i) + ' ' + str(self.ll[i].data))
        return None