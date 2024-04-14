class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return
            current_node = current_node.next

    def print_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" => ")
            current_node = current_node.next
        print(None)

    def print_backward(self):
        current_node = self.tail
        while current_node:
            print(current_node.data, end=" => ")
            current_node = current_node.prev
        print(None)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.print_forward()  # Output: 0 -> 1 -> 2 -> 3 -> None
    dll.delete(2)
    dll.print_backward()  # Output: 3 -> 1 -> 0 -> None