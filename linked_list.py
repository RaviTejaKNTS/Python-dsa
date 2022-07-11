class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            if itr.next:
                llstr += str(itr.data) + "-->"
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)


    def get_length(self):
        count = 0 
        itr = self.head 
        while itr:
            count += 1
            itr = itr.next
        return count


    def insert_at_begining(self, data):   
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)


    def insert_at(self, index, data):
        if index < 0 and index >= self.get_length():
            print("Index value out of range")
            return    
        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def remove_at_begining(self):
        if self.head is None:
            print("There is no node to remove")
            return
        self.head = self.head.next


    def remove_at_end(self):
        if self.head is None:
            print("There is no Linked List")
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None


    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break 
            count += 1
            itr = itr.next


    def insert_after_value(self, value, data):
        if self.head is None:
            return 
        if self.head.data == value:
            self.head.next = Node(data, self.head.next)
            return
        itr = self.head 
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next


    def remove_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next        
        print("value not found")

    
ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")
ll.print()
ll.remove_value("orange")
ll.print()
ll.remove_value("figs")
ll.print()
ll.remove_value("banana")
ll.remove_value("mango")
ll.remove_value("apple")
ll.remove_value("grapes")
ll.print()