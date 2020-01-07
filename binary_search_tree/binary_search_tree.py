import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value #value of current node
        self.left = None #left subtree
        self.right = None #right subtree

    # Insert the given value into the tree
    def insert(self, value):
        #current node has no value
        if not self.value:
            self.value = value
            return
        #value is less than current node and no left subtree exists
        #initiate a left subtree with value
        elif value < self.value and not self.left:
            self.left = BinarySearchTree(value)
        #value is less than current node and left subtree exists
        #run insert on the left subtree
        elif value < self.value and self.left:
            self.left.insert(value)
        #value is greater than current node and no right subtree exists
        #initiate a right subtree with value
        elif value > self.value and not self.right:
            self.right = BinarySearchTree(value)
        #value is greater than current node and right subtree exists
        #run insert on the right subtree
        elif value > self.value and self.right:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if current node is the target value
        if target == self.value:
            return True
        #target is less than current node and left subtree exists
        elif target < self.value and self.left:
            return self.left.contains(target)
        #target is greater than current node and Rigth subtree exists
        elif target > self.value and self.right:
            return self.right.contains(target)
        #target value does not equal current node value and no subtree exists
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        #check if a right subtree exists and go down it
        if self.right:
            return self.right.get_max()
        #no right subtree; return current node value
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #invoke callback function with current node value
        cb(self.value)
        #do the same for the left subtree
        if self.left:
            self.left.for_each(cb)
        #...and the right subtree
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node: return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if not node: return
        #initialize a queue
        queue = Queue()
        #add node to queue
        queue.enqueue(node)
        #while the queue isn't empty
        while queue.len() > 0:
            #grab and remove the top  node in the queue
            node = queue.dequeue()
            #print the node
            print(node.value)
            #add the nodes children to the queue
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    #! it's asking for preorder traversal
    def dft_print(self, node):
        if not node: return
        #print current node
        print(node.value)
        #travel down the left subtree
        if node.left: self.dft_print(node.left)
        #travel down the right subtree
        if node.right: self.dft_print(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if not node: return
        print(node.value)
        if node.left: self.pre_order_dft(node.left)
        if node.right: self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node: return
        #travel down the left subtree
        if node.left: self.post_order_dft(node.left)
        #travel down the right subtree
        if node.right: self.post_order_dft(node.right)
        #print current node
        print(node.value)