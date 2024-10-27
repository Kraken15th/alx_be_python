def draw_pattern(size):
  """
  Draws a square pattern of asterisks with the given size.
  """
  for row in range(size):
    for col in range(size):
      print("*", end="")
    print()  # Move to the next line after each row

if __name__ == "__main__":
  while True:
    try:
      size = int(input("Enter the size of the pattern (positive integer): "))  # Convert input to integer
      if size <= 0:
        print("Invalid size. Please enter a positive integer.")
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a positive integer.")

  draw_pattern(size)
