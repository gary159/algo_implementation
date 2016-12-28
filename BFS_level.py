'''
Implementing a FIFO queue in Python to explore a graph by level. Printing each level
Objective: Not to use the prebuilt Collections.deque

Big-O analysis:
 - Queue:
      - Time: all functions are O(1)
      - Space: O(n)
 - BFS with linked list queue:
      - Time: O(Vertices + Edges)
      - Space: O(n)

Author: Gary Sztajnman
'''


class TreeNode(object):
    def __init__(self,val=None):
        self.val=val
        self.children=[]


class QueueNode(object):
    def __init__(self,node=None,level=None):
        self.node=node
        self.next=None
        self.level=level


class queue(object):
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __repr__(self):
        return 'This queue has {} node(s)'.format(self.length)

    def dequeue(self):
        '''
        Pop the first element of the queue
        '''
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = node.next
        self.length-=1
        return node

    def enqueue(self, TreeNode, level):
        '''
        Add 1 node to the tail of the queue
        '''
        node = QueueNode(TreeNode, level)
        if not self.head:
            self.head = self.tail = node
        else:
            previous = self.tail
            self.tail = node
            self.tail.next = previous
            previous.next = self.tail
        self.length+=1

    def notempty(self):
        '''
        Return False if queue is empty
        '''
        return self.length


def BFS_level(root, level=0):
    '''
    Explore a graph using BFS keeping track of each level.
    input: TreeNode
    '''
    if not isinstance(root,TreeNode):
        raise TypeError, 'Input is not a TreeNode'
    q = queue()
    q.enqueue(root,level)
    visited = set([root])
    print '...Start graph exploration by level'
    print 'level : {}'.format(level)

    while q.notempty():
        node = q.dequeue()
        # Updating and printing level
        if node.level != level:
            level = node.level
            print 'level : {}'.format(node.level)
        # Exploring graph using BFS
        print '\tNode : {}'.format(node.node.val)
        for child in node.node.children:
            if child not in visited:
                visited.add(child)
                q.enqueue(child,node.level+1)


##################################################################
if __name__ == "__main__":
    ## Filling a graph for example
    Groot = TreeNode(0)
    Groot.children += [TreeNode(1),TreeNode(2),TreeNode(3)]
    Groot.children[0].children = [TreeNode(4),TreeNode(5)]
    Groot.children[2].children = [TreeNode(6)]
    Groot.children[0].children[0].children = [TreeNode(7), Groot.children[1]]

    ## Exploring the graph
    BFS_level(Groot)
