class DynamicList:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._array = self.create_array(self.capacity)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Array size must be a non negative Integer")
        self._size = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity must be non negative Integer")
        self._capacity = value

    @property
    def array(self):
        return self._array

    @staticmethod
    def create_array(capacity):
        return [None] * capacity

    def append(self, element):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self.create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self._array = new_array
        self.capacity = new_capacity

    def _shift_left(self, index):
        for _ in range (index, self.size-1):
            self._array = self._array[_+1]
        self._array[self.size-1] = None
        self._size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize(self.capacity*2)

        for _ in range(self.size, index, -1):
            self._array[_] = self._array[_-1]
            self._array[index] = element
            self._size += 1

    def remove(self, element):
        for _ in range(self.size):
            if self._array == element:
                self._shift_left(_)
                return
            raise ValueError("Element not found")

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def pop(self, index=None):
        if index is None:
            index = self.size-1
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        element = self._array[index]
        self._shift_left(index)
        return element

    def __len__(self):
        return self.size

    def __repr__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
