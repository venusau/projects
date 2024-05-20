class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        if not self.head:
            self.head=Node(data)
        else:
            nn=Node(data)
            current=self.head
            while current.next:
                current=current.next
            current.next=nn
    def prepend(self, data):
        nn=Node(data)
        if not self.head:
            self.head=nn
        else:
            nn.next=self.head
            self.head=nn
            
    def traverse_node(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Print None to indicate the end of the linked list

# Create a linked list
linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
sixth_node = Node(6)
fifth_node.next = sixth_node
fourth_node.next = fifth_node
third_node.next = fourth_node
second_node.next = third_node
linked_list.head.next = second_node
linked_list.append(7)
linked_list.append(8)
linked_list.prepend(0)
# Traverse and print the linked list
linked_list.traverse_node()
