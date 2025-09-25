class LargeInterface:
    def method_a(self):
        pass

    def method_b(self):
        pass

    def method_c(self):
        pass

class ClassImplementingLargeInterface(LargeInterface):
    def method_a(self):
        print("Method A implementation")

    def method_b(self):
        print("Method B implementation")

    def method_c(self):
        raise NotImplementedError("Method C is not implemented")  # Unused method

# The ClassImplementingLargeInterface class is forced to implement method_c,
# even though it does not use it, violating the Interface Segregation Principle.