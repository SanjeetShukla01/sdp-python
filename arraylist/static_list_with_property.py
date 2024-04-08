class ArrayListProp:
    def __init__(self, size: int, initial_data=None) -> None:
        """
        Initializes a new ArrayList instance with the specified size.
        :param size: The initial size of the ArrayList.
                     It must be a non-negative integer.
                     If the size is negative, a ValueError is raised.
        """
        if size < 0:
            raise ValueError("ArrayList size can not be Negative")
        self._size = size
        self._data = initial_data if initial_data else [None] * size
        self._data_type = "hetero" if initial_data else None

    @property
    def data(self):
        print("Returning data...")
        return self._data

    @property
    def size(self):
        print("Returning size...")
        return self._size

    @size.setter
    def size(self, size_value):
        if size_value < 0:
            raise ValueError("ArrayList size can not be Negative")
        self._size = size_value

    @property
    def data_type(self):
        print("Returning data type...")
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value


    def __getitem__(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("ArrayList Index out of Range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("ArrayList Index out of Range")
        self.data[index] = value
        self.data_type = type(value)

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        return str(self.data)

    def _add_to_next_empty(self, data):
        """
        Add an element to the next empty location in the list.

        :param data: The element to add.
        :return: A message indicating the result of the operation.
        """
        for _ in range(self.size):
            if self.data[_] is None:
                self.data[_] = data
                return "Element added at index {}".format(_)
        return "List is full, cannot add more elements"

    # Implementing Basic methods of python list

    def add_element(self, data):
        """
        Generally python list stores element of various types
        But this function is an implementation of type check
        To ensure that next element type is same as the type of first element.
        To implement this method, Lots of assumptions need to be made
        1. That list is filled in a sequence starting from position zero
        :param data:
        :return:
        """
        if all(elem is None for elem in self.data):
            self.data[0] = data
            self.data_type = type(data)
            return "Element added at index 0, list_data_type set to {}".format(self.data_type.__name__)

            # If elements already exist
        elif self.data_type == "hetero":
            # List is heterogeneous, add the element to the next empty location without type check
            return self._add_to_next_empty(data)

        elif all(isinstance(elem, self.data_type) for elem in self.data if elem is not None):
            # Check if the new element has the same data type as list_data_type
            if isinstance(data, self.data_type):
                return self._add_to_next_empty(data)
            else:
                raise TypeError("New element has a different data type than list data_type")
        else:
            return self._add_to_next_empty(data)
