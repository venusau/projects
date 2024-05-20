#  Python code to generate the reverse of a linked list 
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

#  ""this"" ->  keyword 
#  it is a reserved keyword in the java or javascript which represents the current execution context 
#  The same for the python we use something called ''self'' -> keyword 

class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,  data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current = current.next
            current.next= new_node
    def prepend(self, data):
        new_node=Node(data)
        if not self.head:
            self.head= new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def add_node_in_position(self, data, position):
        new_node = Node(data)
        
        if position == 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        counter = 0

        while current.next and counter < position - 1:
            current = current.next
            counter += 1
        
        new_node.next = current.next
        current.next = new_node
            


    def traverse(self):
        if not self.head:
            print("Linked list is empty")
        else:
            current=self.head
            while current:
                print(current.data, end=" -> ")
                current=current.next
            
linked_list = Linkedlist()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

linked_list.traverse() # 1 -> 2 -> 4 -> 5 -> 6 ->
print("\n\n")
linked_list.prepend(0)
linked_list.traverse() # 0 -> 1 -> 2 -> 4 -> 5 -> 6 ->
print("\n\n")
linked_list.add_node_in_position(3, 3)
linked_list.traverse()