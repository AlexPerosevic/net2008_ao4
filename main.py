
def calculate_power(base, exponent):
  if exponent == 0:
    # If it is, return 1
    return 1
  return base * calculate_power(base, exponent - 1)
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
result = calculate_power(base, exponent)
print("The result is: ", result)
