Here's the temp_conversion_tool.py script demonstrating temperature conversion with global variables:

Python
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor to convert F to C
CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5

def convert_to_celsius(fahrenheit):
  """
  Converts a temperature from Fahrenheit to Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  """
  Converts a temperature from Celsius to Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
  """
  Prompts user for temperature and unit, performs conversion, and displays the result.
  """
  try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit == 'C':
      converted_temp = convert_to_fahrenheit(temperature)
      unit_label = "°C"
      converted_unit_label = "°F"
    elif unit == 'F':
      converted_temp = convert_to_celsius(temperature)
      unit_label = "°F"
      converted_unit_label = "°C"
    else:
      raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    print(f"{temperature:.1f}{unit_label} is {converted_temp:.2f}{converted_unit_label}")
  except ValueError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()
