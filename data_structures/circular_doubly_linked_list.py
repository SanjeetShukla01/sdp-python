class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev=self.tail
            new_node.next=self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.append(data)
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if not self.head:
            print("List is empty")
            return

        current_node = self.head
        while True:
            if current_node.data == data:
                if current_node.next == current_node:  # Only one node in the list
                    self.head = None
                    self.tail = None
                    return
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = current_node.prev
                return
            current_node = current_node.next
            if current_node == self.head:
                break

    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()


# Example usage:
if __name__ == "__main__":
    cdl = CircularDoubleLinkedList()
    cdl.append(11)
    cdl.append(24)
    cdl.append(32)
    cdl.prepend(0)
    cdl.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 0 ->
    cdl.delete(24)
    cdl.print_list()  # Output: 0 -> 1 -> 3 -> 0 ->
