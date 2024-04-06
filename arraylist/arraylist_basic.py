class ArrayList:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("ArrayList size can not be Negative")
        self.size = size
        self.data = [None] * size
        self.data_type = None

    def __getitem__(self, index: int):
        if index < 0 or index > self.size:
            raise IndexError("ArrayList Index out of Range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("ArrayList Index out of Range")
        self.data[index] = value

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        return str(self.data)

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
        if not any(self.data):
            self.data[0] = data
            self.data_type = type(data)
            return

            # Find the last non-empty position in the list
        last_index = self.size - 1
        while self.data[last_index] is None:
            last_index -= 1

        # Get the data type of the last element
        last_element_type = type(self.data[last_index])

        # Check if the new element is of the same type as the last element type
        if isinstance(data, last_element_type):
            # Find the first empty position after the last non-empty position
            empty_index = last_index + 1
            while empty_index < self.size and self.data[empty_index] is not None:
                empty_index += 1

            # If there's an empty position available, add the new element
            if empty_index < self.size:
                self.data[empty_index] = data
            else:
                print("List is full. Cannot add more elements.")
        else:
            raise TypeError("New element is not of the same type as the list data type")




