# Python Banking Program

def show_balance(Balance):
    print(f"Your balance is ${Balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(Balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > Balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    Balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(Balance)
        elif choice == "2":
            Balance += deposit()
        elif choice == "3":
            Balance -= withdraw(Balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank you! Have a nice day")

main()
