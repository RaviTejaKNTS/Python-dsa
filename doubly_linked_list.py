class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("There is no Doubly Linked List")
            return
        itr = self.head
        dllpf = " "
        while itr:
            if itr.next:
                dllpf += str(itr.data) + "-->"
            else:
                dllpf += str(itr.data)
            itr = itr.next
        print(dllpf)
        
    def print_backward(self):
        if self.head is None:
            print("There is no Doubly Linked List")
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        dllpb = " "
        while itr:
            if itr.prev:
                dllpb += str(itr.data) + "-->"
            else:
                dllpb += str(itr.data)
            itr = itr.prev
        print(dllpb)

    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, self.head)
            self.head = node
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, itr, None)
        itr.next = node


    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print("Invalid Index Value")
            return 
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr, itr.next)
                itr.next.prev = node
                itr.next = node
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        if self.head == None:
            for data in data_list:
                self.insert_at_end(data)

    def remove_at_beginning(self):
        if self.head is Node:
            print("The List is already empty")
            return 
        self.head = self.head.next
        self.head.prev = None

    def remove_at_end(self):
        if self.head is None:
            print("The List is empty")
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def remove_at(self, index, data):
        if self.head is None:
            print("The list is empty")
            return 
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.prev.next = itr.next
                itr.next.prev = itr.prev
            count += 1
            itr = itr.next

    def insert_after_value(self, value, data):
        if self.head is None:
            print("there is no list in the first place")
            return 
        if self.head.data == value:
            node = Node(data, self.head, self.head.next)
            self.head.next.prev = node
            self.head.next = node
            return
        itr = self.head 
        while itr:
            if itr.data == value:
                print(itr.next.data)
                node = Node(data, itr, itr.next)
                itr.next.prev = node 
                itr.next = node
                return
            itr = itr.next
        

    def remove_value(self, value):
        if self.head is None:
            print("there is no list")
            return 
        if self.head.data == value:
            self.head = self.head.next 
            self.head.prev = None
        itr = self.head 
        while itr:
            if itr.data == value:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next 
            itr = itr.next


dll = Doubly_Linked_List()
dll.insert_values([2, 3, 4, 5, 6])
dll.print_forward()
dll.print_backward()
dll.remove_value(4)
dll.print_forward()
dll.print_backward()