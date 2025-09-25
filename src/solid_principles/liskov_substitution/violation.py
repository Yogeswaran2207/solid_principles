class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        # Incorrectly overrides the area method
        return self.width + self.height  # This violates the expected behavior


def calculate_area(shape: Shape):
    return shape.area()


# Example usage
rectangle = Rectangle(5, 10)
square = Square(5)

print(f"Rectangle area: {calculate_area(rectangle)}")  # Expected: 50
print(f"Square area: {calculate_area(square)}")  # Expected: 25, but will return 10 due to violation