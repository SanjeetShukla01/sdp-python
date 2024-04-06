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
        if all(elem is None for elem in self.data):
            self.data[0] = data
            self.data_type = type(data)
            return "Element added at index 0, list_data_type set to {}".format(self.data_type.__name__)

            # If elements already exist
        else:
            # Check if all existing elements have the same data type
            if all(isinstance(elem, self.data_type) for elem in self.data if elem is not None):
                # Check if the new element has the same data type as list_data_type
                if isinstance(data, self.data_type):
                    for i in range(self.size):
                        if self.data[i] is None:
                            self.data[i] = data
                            return "Element added at index {}".format(i)
                    return "List is full, cannot add more elements"
                else:
                    raise TypeError("New element has a different data type than list data_type")
            else:
                # List is heterogeneous, add the element to the next empty location without type check
                for i in range(self.size):
                    if self.data[i] is None:
                        self.data[i] = data
                        return "Element added at index {}".format(i)
                return "List is full, cannot add more elements"




