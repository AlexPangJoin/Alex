#  Python Weight Converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds? (K or L)")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight,1)} {unit}")
else:
    print(f"This {unit} is not valid")

# Python Temperature Converter

unit = input("What is the measurement of temperature in Celsuis or Fahrenheit (C/F): ")
temp = float(input("Enter the Temperature: "))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = (round(temp-32)*5/9,1)
    print(f"The temperature in Celsuis is: {temp}°C")

else:
    print(f"{unit} is an invalid unit of measurement")