# Get user input for size
while True:
 size = int(input("Enter the size of the pattern (positive integer): "))
 if size > 0:
   break
else:
 print("Invalid input. Please enter a positive integer.")
"except ValueError:"
print("Invalid input. Please enter a positive integer.")
# Print the pattern# Print the pattern
for i in range(size):
 for j in range(size):
  print("*", end="")
  print()  # Move to next line