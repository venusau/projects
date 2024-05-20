class Node:
    def __init__(self, data):
        self.data=data 
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def append(self, data):
        nn=Node(data)
        if not self.head:
            self.head=nn
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=nn
    def print_node(self):
        current=self.head
        while(current.next):
            print(current.data,end="->")
            current=current.next
        print("none")
l=Linked_list()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.print_node()