# name = input("Enter your name: ")
# age = float(input("Enter your age: "))
# age = age + 1

# print(f"Hello, {name}!")
# print(f"You are {age} years old.")



# adejective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")
# adjective2 = input("Enter one adjective to describe the experience: ")

# print(f"Today, I went to a {adejective} park.")
# print(f"At the park, I saw three {noun}.")
# print(f"{noun} is {verb}ing.")
# print(f"It was a {adjective2} experience!")



# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# height = float(input("Enter the height of the rectangle: "))

# area = length * width
# volume = length * width * height

# print(f"The area of the rectangle is: {area}cm^2")
# print(f"The volume of the rectangle is: {volume}cm^3")



item = str(input("What item would you like to buy?"))
price = float(input("What is the price of the item?"))
quantity = int(input("How many items would you like to buy?"))

totalcost = price * quantity
print(f"The total cost of {quantity} {item} is: ${round(totalcost, 2)}")

