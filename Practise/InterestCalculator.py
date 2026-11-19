
principle = 0
time = 0
rate = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principla can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the Interest Rate: "))
    if rate <= 0:
        print("Interest rate can't be less than zero")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less or equal to zero")
    else:
        break

total = principle * pow((1 + rate/100),time)
print(f"Balance after {time} year/s: ${total: .2f}")
