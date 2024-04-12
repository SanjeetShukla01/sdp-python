
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:           # Insert as first element
            self.head = new_node
            return                  # Exits the function if linked list was empty and this node is first node
        last_node = self.head       # Set last_node to head, & start traversing to last node using while loop
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node   # Once got the last node, set the last_node.next = new_node.

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head       # head points to first node. this step adds that address to new_node.next
        self.head = new_node            # set head = new node

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print([current_node.data, current_node.next], end=" -> ")
            current_node = current_node.next
        print("None")

    def size_of_ll(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position:
            new_node.next = self.head
            self.head = new_node
        else:
            while (current_node is not None) and position+1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index not present")


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
    print(ll.size_of_ll())
    ll.delete(2)
    ll.print_list()  # Output: 0 -> 1 -> 3 -> None
    print(ll.size_of_ll())
