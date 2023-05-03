"""
Linked list in Python via OOP
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:

    head = None
    tail = None

    def __init__(self, head=None, tail=None):
        if head:
            self.head = head
        if tail:
            self.tail = tail
        
    def add_node(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_node(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == data:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    return
                current_node = current_node.next
                
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

def test_doubly_linked_list():
    # create a new doubly-linked list
    my_list = DoublyLinkedList()

    # check that the list is empty
    assert my_list.head is None
    assert my_list.tail is None

    # add some nodes to the list
    my_list.add_node(1)
    my_list.add_node(2)
    my_list.add_node(3)

    # check that the list contains the expected nodes
    assert my_list.head.data == 1
    assert my_list.head.next.data == 2
    assert my_list.tail.data == 3
    assert my_list.tail.prev.data == 2

    # remove a node from the list
    my_list.remove_node(2)

    # check that the list no longer contains the removed node
    assert my_list.head.next.data == 3
    assert my_list.tail.prev.data == 1

    # add some more nodes to the list
    my_list.add_node(4)
    my_list.add_node(5)

    # check that the list contains the new nodes
    assert my_list.head.next.next.data == 4
    assert my_list.tail.prev.data == 4

    # remove the head node from the list
    my_list.remove_node(1)

    # check that the list no longer contains the removed node
    assert my_list.head.data == 3
    assert my_list.head.prev is None

    # remove the tail node from the list
    my_list.remove_node(5)

    # check that the list no longer contains the removed node
    assert my_list.tail.data == 4
    assert my_list.tail.next is None

    # remove the last node from the list
    my_list.remove_node(4)

    # check that the list no longer contains any nodes
    assert my_list.head is None
    assert my_list.tail is None

def main():
    # create a new doubly-linked list
    my_list = DoublyLinkedList()

    # add some nodes to the list
    my_list.add_node(1)
    my_list.add_node(2)
    my_list.add_node(3)

    # remove a node from the list
    my_list.remove_node(2)

    # print the contents of the list
    my_list.print_list()

if __name__=="__main__":
    # test_doubly_linked_list()
    main()