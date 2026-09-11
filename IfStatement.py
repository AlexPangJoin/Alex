
# for i in range(3):
#     age = int(input("How old are you? "))

#     if age >= 100:
#         print("Do you really want to use this website at this age?")
#     elif age >= 18:
#         print("Congratulation, you are signed up")
#     elif age <= 0:
#         print("Are you kidding me?")
#     else:
#         print("You have to be 18+ to enter this website")

#     if input ("Type 'stop' to exit, or press Enter to continue: "). lower() == "stop":
#         break

name = str(input("Enter your name: "))

if name == "":
    print("Please type your name first")
else:
    print(f"Hello {name}")


Soccerfan = True

if Soccerfan:
    team = str(input("What team do you support?"))
    print (f"I like {team} as well")
else:
    print("Get out")