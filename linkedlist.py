class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            next = self.head
            while next is not None:
                print(next.data,'---->',end="")
                next = next.ref
        print('',end="\n")
    def add_begin(self,data):
        node = Node(data)
        node.ref = self.head
        self.head = node
    
    def add_end(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = node
    
    def add_after(self,data,number):
        new_node = Node(data)
        n = self.head
        while n.ref is not None:
            if n.data == number:
                new_node.ref = n.ref
                n.ref = new_node
                return
            else:
                n = n.ref
        print(number," not found in the list")
    
    def jls_extract_def(self, jls_extract_var):
        return jls_extract_var

    def add_before(self,data,number):
        if self.head is None:
            return -1
        elif self.head.data == number:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == number:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                return
            else:
                n = n.ref
        print(end="\n")
        jls_extract_var = ' not found'
        print(number,self.jls_extract_def(jls_extract_var),end="\n")
        



            


ll = LinkedList()
ll.traverse()
ll.add_begin(10)
# ll.traverse()
ll.add_begin(20)
ll.add_end(45)
ll.add_begin(120)
ll.add_end(145)
ll.add_after(35, 120)
ll.add_after(21, 20)
ll.add_after(21, 200)
ll.traverse()
ll.add_before(1, 20)
ll.traverse()
ll.add_before(-1, 0)
ll.traverse()