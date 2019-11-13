import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because you can delete and insert from either the left(head) or the right(tail) and we're done with no need to traverse/loop anything
        self.storage = DoublyLinkedList()


    def enqueue(self, item):
        self.storage.add_to_tail(item)
        # increment size counter
        self.size += 1

    def dequeue(self):
        # decrement size counter
        if self.size > 0:
            self.size -= 1
        # remove the head and return it
        return self.storage.remove_head()

    def len(self):
        return self.size





