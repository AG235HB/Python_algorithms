#Double linked list with cycling...
class LinkedList:
    
    def __init__(self):
        self.ll = None
        self.nodes=0
        self.first_node = None
        self.last_node = None

    def print_func(self, func):
        import node
        n = func
        try:
            return str(n.data)
        except AttributeError:
            return "E"
        #if func is None:
        #    return None
        #else:
        #    return str(func)
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

    def step_right(self, steps):
        for i in range(0,steps,1):
            if self.ll.next == None:
                break
            self.ll = self.ll.next

    def step_left(self, steps):
        for i in range(0,steps,1):
            if self.ll.prev == None:
                break
            self.ll = self.ll.prev

    def show(self, i):
        log = open("log.txt","a")
        log.write("\n")
        log.write("Nodes:" + str(self.nodes) + "\n")
        currentNode = self.ll
        for j in range(0,i,1):
            log.write("|")
            print("=========================")
            try:
                log.write("P:"+self.print_func(currentNode.prev))
                print("P:"+self.print_func(currentNode.prev))
            except AttributeError:
                log.write("ERR")
                print("error")
            finally:
                print("_")
            try:
                log.write(" C:"+self.print_func(currentNode))
                print("C:"+self.print_func(currentNode))
            except AttributeError:
                log.write("ERR")
                print("error")
            finally:
                print("_")
            try:
                log.write(" N:"+self.print_func(currentNode.next))
                print("N:"+self.print_func(currentNode.next))
            except AttributeError:
                log.write("ERR")
                print("error")
            finally:
                print("_")

            if currentNode.next == None:
                continue
            else:
                currentNode = currentNode.next
        log.close()

    def cycle(self):
        currentNode = self.ll
        last = self.ll
        while currentNode.next != None:
            currentNode = currentNode.next
        first = self.ll
        while currentNode.prev != None:
            currentNode = currentNode.prev
        last = currentNode
        if currentNode.prev == None:
            print "cycling next to prev"
            for i in range(0,self.nodes-1,1):
                currentNode = currentNode.next
            currentNode.next = last
            last.prev = currentNode
            self.first_node = currentNode
            self.last_node = last
        else:
            print "CARAMBA"

    def show_current(self):
        try:
            print("P:"+self.print_func(self.ll.prev))
        except AttributeError:
            print("error")
        #finally:
        #    print("_")
        try:
            print("C:"+self.print_func(self.ll))
        except AttributeError:
            print("error")
        #finally:
        #    print("_")
        try:
            print("N:"+self.print_func(self.ll.next))
        except AttributeError:
            print("error")
        #finally:
        #    print("_")

    def del_current(self):
        import node

        if self.ll == None:
            return None
        else:
            currentNode = self.ll
            self.ll = self.ll.next
            self.ll.prev = currentNode.prev
            print self.ll.data
            self.ll.prev.next = self.ll
            self.nodes -= 1
            return currentNode.data