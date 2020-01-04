import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.data = DoublyLinkedList()

    def push(self, value):
        self.data.add_to_head(value)
        self.size += 1

    def pop(self):
        value = self.data.remove_from_head()
        if value: self.size -= 1
        return value

    def len(self):
        return self.size
