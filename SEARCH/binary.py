class BinaryTree:
    def __init__(self):
        self.nodes = 0
        self.bt = None

    def add_to_parent_recurrent(self, parent, value):
        #print "add_to_parent_recurrent"
        #print parent.data
        #st = "PARENT:" + str(parent.data) + " VALUE:" + str(value)
        #st += "PARENT LEFT:" + str(parent.left) + " PARENT RIGHT:" + str(parent.right)

        #print "PARENT:" + str(parent.data) + " VALUE:" + str(value)
        #print "PARENT LEFT:" + str(parent.left) + " PARENT RIGHT:" + str(parent.right)
        from structs import btnode
        if value < parent.data:
            #print "try add to left"
            if parent.left is None:
                parent.left = btnode.BinaryTreeNode(value, None, None, parent)
                #print "to left " + str(parent.left.data)
            else:
                #print "left again"
                self.add_to_parent_recurrent(parent.left, value)
        elif value >= parent.data:
            #print "try add to right"
            if parent.right is None:
                parent.right = btnode.BinaryTreeNode(value, None, None, parent)
                #print "to right " + str(parent.right.data)
            else:
                #print "right again"
                self.add_to_parent_recurrent(parent.right, value)
        #else:
        #    print "CARAMBA"
        #return st


    def add(self, value):
        from structs import btnode
        if self.nodes == 0:
            self.bt = btnode.BinaryTreeNode(value, None, None, None)
            self.nodes += 1
            print self.bt.data
        else:
            self.add_to_parent_recurrent(self.bt, value)
            self.nodes += 1
