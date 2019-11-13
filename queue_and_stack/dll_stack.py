from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Actually with a stack a single linked list is better because we can
        # pop and push to the head alone.
        # self.storage = storage_dll

    def push(self, value):
        pass

    def pop(self):
        pass

    def len(self):
        pass
