class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()


# Example usage
rectangle = Rectangle(10, 5)
circle = Circle(7)

calculator = AreaCalculator()
print(calculator.calculate_area(rectangle))  # Outputs: 50
print(calculator.calculate_area(circle))     # Outputs: 153.86

# Violation: If we want to add a new shape, we need to modify the AreaCalculator class
# This can lead to bugs and maintenance issues as the codebase grows.