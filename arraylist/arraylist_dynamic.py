class DynamicList:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = self.create_array(self.capacity)

    @staticmethod
    def create_array(capacity):
        return [None] * capacity

    def append(self, element):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = element
        self.size += 1

    def resize(self, new_capacity):
        new_array = self.create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __len__(self):
        return self.size

    def __repr__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
