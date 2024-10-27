class Calculator:
  """
  Represents a calculator with static and class methods for performing calculations.
  """
  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Static method to perform addition. Doesn't require class or instance access.
    """
    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Class method to perform multiplication. Uses class attribute and prints a message.
    """
    print(f"Calculation type: {cls.calculation_type}")
    return a * b


if __name__ == "__main__":
  # Example usage (uncomment for testing without main.py)
  # sum_result = Calculator.add(10, 5)
  # print(f"The sum is: {sum_result}")
  # product_result = Calculator.multiply(10, 5)
  # print(f"The product is: {product_result}")
  pass