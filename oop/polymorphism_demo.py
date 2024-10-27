
import math


class Shape:
  """
  Represents a base shape with an abstract area() method.
  """

  def area(self):
    """
    Raises a NotImplementedError as derived classes need to implement this method.
    """
    raise NotImplementedError("Area calculation not implemented for base Shape")


class Rectangle(Shape):
  """
  Represents a rectangle with length and width attributes and area calculation.
  """

  def __init__(self, length, width):
    """
    Initializes a Rectangle object with length and width.
    """
    self.length = length
    self.width = width

  def area(self):
    """
    Overrides the base area() to calculate the rectangle's area (length x width).
    """
    return self.length * self.width


class Circle(Shape):
  """
  Represents a circle with radius attribute and area calculation.
  """

  def __init__(self, radius):
    """
    Initializes a Circle object with radius.
    """
    self.radius = radius

  def area(self):
    """
    Overrides the base area() to calculate the circle's area (pi x radius^2).
    """
    return math.pi * self.radius**2


if __name__ == "__main__":
  # Example usage (uncomment for testing without main.py)
  # rectangle = Rectangle(10, 5)
  # circle = Circle(7)
  # print(f"Rectangle area: {rectangle.area()}")
  # print(f"Circle area: {circle.area()}")
  pass