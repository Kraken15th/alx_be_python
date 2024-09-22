# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Get user input for operation
operation = input("Choose the operation (+, -, *, /): ")
# Perform calculation using Match Case
# case "+":
print(num1 + num2)
# case "-":
print(num1 - num2)
# case "*":
print(num1 * num2)
# case "/":
print(num1 / num2)
if num2 == 0:
 print ("Cannot divide by zero.")
else:
 print(num1 / num2)
# case _:
print ("Invalid operation.")
# Display the result
print (f"The result is [result].")