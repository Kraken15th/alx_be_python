# Get user input for number
number = int(input("Enter a number to see its multiplication table: "))
print("Multiplication Table for:", number)
for i in range(1, 11):
 product = number * i
 print(f"{number} * {i} = {product}")
 