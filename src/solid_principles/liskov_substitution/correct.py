class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def calculate_area(shape: Shape) -> float:
    return shape.area()

# Example usage
rectangle = Rectangle(5, 10)
square = Square(4)

print(f"Area of rectangle: {calculate_area(rectangle)}")  # Output: 50
print(f"Area of square: {calculate_area(square)}")        # Output: 16