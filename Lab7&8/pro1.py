class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Key not found in the list")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")




if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.display()  
    
    ll.delete(20)
    ll.display()  
