
class ArrayList:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("ArrayList size can not be Negative")
        self.size = size
        self.data = [None]*size

    def __getitem__(self, index: int):
        if index<0 or index > self.size:
            raise IndexError("ArrayList Index out of Range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index<0 or index>self.size:
            raise IndexError("ArrayList Index out of Range")
        self.data[index]=value





    def __str__(self) -> str:
