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
l1=DoublyLinkedList()
l1.append(2)
l1.append(4)
l1.append(3)
l1.print_forward()
s1=l1.traverse_dll()
l2=DoublyLinkedList()
l2.append(5)
l2.append(6)
l2.append(4)
l2.print_forward()
s2=l2.traverse_dll()
a=s1+s2
#a_str = str(a)
#a_reversed_str = a_str[::-1]
#a = int(a_reversed_str)

while a!=0:
    n=a%10
    print(n, end=" <-> ")
    a=a//10
print("None")