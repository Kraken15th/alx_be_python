Here's the match_case_calculator.py script that performs calculations based on user input using a match-case statement:

Python
def main():
  """
  Prompts the user for numbers and an operation, performs the calculation using match-case, and displays the result.
  """
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ").lower()

    match operation:
      case "+":
        result = num1 + num2
        print(f"The result is {result:.2f}.")
      case "-":
        result = num1 - num2
        print(f"The result is {result:.2f}.")
      case "*":
        result = num1 * num2
        print(f"The result is {result:.2f}.")
      case "/":
        if num2 == 0:
          print("Cannot divide by zero.")
        else:
          result = num1 / num2
          print(f"The result is {result:.2f}.")
      case _:
        print("Invalid operation. Please choose +, -, *, or /.")
  except ValueError:
    print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
  main()
