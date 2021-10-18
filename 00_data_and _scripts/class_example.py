# Create a class
class Rectangle():
    """Rectange object

    Paramters
    ---------
    parameter_a : float
        lenght of one side of the rectangle
    parameter_b : float
        lenght of the other side of the rectangle

    Attributes
    ----------
    a : float
        lenght of one side of the rectangle
    b : float
        lenght of the other side of the rectangle
    area : float
        area of the rectangle
    perimeter : float
        perimeter of the rectangle
    """

    def __init__(self, paramter_a, paramter_b):
        self.a = paramter_a  # Note that the name of the parameter does not need to match the name of the attribute
        self.b = paramter_b
        self.area = self.a * paramter_b  # attributes can be created directly from the parameters...
        self.perimeter = self.compute_perimeter()  # ...or calling a method

    # this is class method. it accessible only from within an istance of this class
    def compute_perimeter(self):
        """compute the perimeter of the rectangle

        Returns
        -------
        float
            perimeter value
        """

        return (self.a+self.b)*2


# Inheritance example: the Square object has the same attributes and methods as
# the Rectangle, unless overwritten (using the same name for something else)
class Square(Rectangle):
    """Square object

    Paramters
    ---------
    parameter_a : float
        lenght of one side of the rectangle
    """

    def __init__(self, paramter_a):
        super().__init__(paramter_a, paramter_a)


if __name__ == "__main__":
    rec = Rectangle(10, 20)
    sq = Square(10)

    rec.area
    sq.area
