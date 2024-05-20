class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def traverse_dll(self):
        current=self.head
        s=0
        while current.next:
            current =current.next
        while current:
            l=current.data
            s=s*10+l
            current=current.prev
        return s
    def delete_node(self, n):
        current = self.head
        t = 0
        while current:
            t = t + 1
            if t == n:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                break  
            current = current.next

        # Printing the linked list after deletion
        self.print_forward()

l1=DoublyLinkedList()
l1.append(2)
l1.append(4)
l1.append(3)
l1.append(1)
l1.print_forward()
n=input("enter the nth node to delete from the end of the list:")
l1.delete_node(n)