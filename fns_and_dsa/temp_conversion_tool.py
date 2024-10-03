# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
def main():
    while True:
          temperature = float(input("Enter the temperature to convert: "))
          unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
          if unit == "C":
            converted_temp = convert_to_fahrenheit
            unit_label = "°C"
            result_unit = "°F"
          elif unit == 'F':
            converted_temp = convert_to_celsius
            unit_label = "°F"
            result_unit = "°C"
          else:
           raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
           print(f"{temperature}{unit_label} is {converted_temp:.2f}{result_unit}")
