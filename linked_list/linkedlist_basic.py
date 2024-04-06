class CustomList:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def __len__(self):
        return self.size

    def __repr__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"


# Example usage:
custom_list = CustomList()
custom_list.append(1)
custom_list.append(2)
custom_list.append(3)

print(custom_list[0])  # Output: 1
print(len(custom_list))  # Output: 3
print(custom_list)  # Output: [1, 2, 3]
