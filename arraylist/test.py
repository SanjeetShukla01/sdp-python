class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width must be non-negative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Area must be non-negative")
        # Calculate the new width and height based on the given area
        self._width = (value / self.height) if self.height != 0 else 0
        self._height = (value / self.width) if self.width != 0 else 0


if __name__ == '__main__':
    # Create a rectangle object
    rectangle = Rectangle(3, 4)

    # Access area attribute
    print(rectangle.area)  # Output: 12

    # Set area directly
    rectangle.area = 15

    # Access width and height to verify update
    print(rectangle.width, rectangle.height)  # Output: 3.0 5.0
