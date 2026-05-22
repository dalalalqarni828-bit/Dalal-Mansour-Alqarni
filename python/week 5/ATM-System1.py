balance = 1000
while True:
    print("\n===== ATM MENU =====")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")

    choice = input("Choose an option: ")

    match choice:

        case "1":
            print(f"Current balance: {balance} SAR")

        case "2":

            while True:
                amount = int(input(
                    "Enter deposit amount (50, 100, 200, 500) or 0 to cancel: "
                ))

                match amount:
                    case 50 | 100 | 200 | 500:
                        balance += amount
                        print(f"Deposited {amount} SAR")
                        print(f"New balance: {balance} SAR")
                        break

                    case 0:
                        print("Deposit cancelled")
                        break

                    case _:
                        print("Invalid amount, try again")

        case "3":

            while True:
                amount = int(input(
                    "Enter withdraw amount (50, 100, 200, 500) or 0 to cancel: "
                ))

                match amount:
                    case 50 | 100 | 200 | 500:

                        if balance >= amount:
                            balance -= amount
                            print(f"Withdrawn {amount} SAR")
                            print(f"New balance: {balance} SAR")
                        else:
                            print("Insufficient funds")

                        break

                    case 0:
                        print("Withdraw cancelled")
                        break

                    case _:
                        print("Invalid amount, try again")

        case "0":
            print("Thank you for using the ATM")
            break

        case _:
            print("Invalid option")