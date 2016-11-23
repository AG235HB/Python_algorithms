#Double linked list with cycling...
class LinkedList:
    
    def __init__(self):
        self.ll = None
        self.nodes=0
        self.first_node = None
        self.last_node = None
        self.was_cycled = False

    def print_func(self, func):
        import node
        n = func
        try:
            return str(n.data)
        except AttributeError:
            return "E"
    def add(self, value):
        #THIS WORKS WELL
        import node
        self.nodes += 1

        if self.ll == None:
            self.ll = node.Node(value,self.ll,self.ll)
            self.first_node = self.ll
        else:
            self.ll = node.Node(value,self.ll.prev,self.ll)
            self.ll.next.prev = self.ll
            self.last_node = self.ll
        if self.was_cycled:
            self.cycle()

    def step_right(self, steps):
        for i in range(0,steps,1):
            if self.ll.next == None:
                break
            self.ll = self.ll.next
        self.last_node = self.ll
        self.first_node = self.ll.prev

    def step_left(self, steps):
        for i in range(0,steps,1):
            if self.ll.prev == None:
                break
            self.ll = self.ll.prev
        self.last_node = self.ll
        self.first_node = self.ll.prev

    def show(self, i):
        log = open("log.txt","a")
        log.write("\n")
        log.write("Nodes:" + str(self.nodes) + "\n")
        log.write("FIRST:" + str(self.first_node.data) + " LAST:" + str(self.last_node.data) + "\n")
        currentNode = self.ll
        for j in range(0,i,1):
            log.write("|")
            try:
                log.write("P:"+self.print_func(currentNode.prev))
            except AttributeError:
                log.write("ERR")
            try:
                log.write(" C:"+self.print_func(currentNode))
            except AttributeError:
                log.write("ERR")
            try:
                log.write(" N:"+self.print_func(currentNode.next))
            except AttributeError:
                log.write("ERR")

            if currentNode.next == None:
                continue
            else:
                currentNode = currentNode.next
        log.close()

    def cycle(self):
        currentNode = self.ll
        if self.was_cycled:
            last = self.ll
            while currentNode.next != None:
                currentNode = currentNode.next
            first = self.ll
            while currentNode.prev != None:
                currentNode = currentNode.prev
            last = currentNode
            print("FIRST:" + str(self.first_node.data) + " LAST:" + str(self.last_node.data))
            for i in range(0,self.nodes-1,1):
                currentNode = currentNode.next
                    #print currentNode.data
            currentNode.next = last
            last.prev = currentNode
            self.first_node = currentNode
            self.last_node = last
        else:
            self.ll.prev = self.first_node
            self.ll.prev.next = self.ll

    def show_current(self):
        try:
            print("P:"+self.print_func(self.ll.prev))
        except AttributeError:
            print("error")
        try:
            print("C:"+self.print_func(self.ll))
        except AttributeError:
            print("error")
        try:
            print("N:"+self.print_func(self.ll.next))
        except AttributeError:
            print("error")

    def del_current(self):
        import node
        if self.ll == None:
            return None
        else:
            currentNode = self.ll
            self.ll = self.ll.next
            self.ll.prev = currentNode.prev
            self.ll.prev.next = self.ll
            self.last_node = self.ll
            self.nodes -= 1
            return currentNode.data