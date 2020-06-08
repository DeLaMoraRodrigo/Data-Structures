"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next


    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node


    def remove_tail(self):
        if self.tail is None:
            return None

        data = self.tail.get_value()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.get_next() != self.tail:
                current = current.get_next()

            self.tail = current

        return data

    def add_to_head(self, value):
        newNode = Node(value)
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.set_next(self.head)
            self.head = newNode

    def remove_head(self):
        if self.head is None:
            return None

        data = self.head.get_value()

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return data


    def contains(self, data):
        if not self.head:
            return False

        current = self.head

        while current is not None:
            if current.get_value() == data:
                return True
 
            current = current.get_next()

        return False


    def get_max(self):
        if self.head is None:
            return None

        max_so_far = self.head.get_value()

        current = self.head.get_next()

        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()

            current = current.get_next()

        return max_so_far