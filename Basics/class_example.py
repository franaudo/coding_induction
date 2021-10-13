

class Rectangle():
    def __init__(self, paramter_a, paramter_b):
        self.a = paramter_a
        self.b = paramter_b
        self.area = self.a * paramter_b
        self.perimeter = self.compute_perimeter()

    def compute_perimeter(self):
        return (self.a+self.b)*2


# Inheritance example
class Square(Rectangle):
    def __init__(self, paramter_a):
        super().__init__(paramter_a, paramter_a)


if __name__ == "__main__":
    rec = Rectangle(10, 20)
    sq = Square(10)

    rec.area
    sq.area
