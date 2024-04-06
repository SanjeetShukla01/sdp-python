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
        :param data:
        :return:
        """
        if not self.data:
            self.data_type = type(data)

        # Check if the type of the new element matches the type of the first element
        if isinstance(data, self.data_type):
            self.data.append(data)
        else:
            raise TypeError(f"Invalid type. Expected {self.data_type}, got {type(data)}")


