#  Python Weight Converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds? (K or L)")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"This {unit} is not valid")

print(f"Your weight is {weight} {unit}")