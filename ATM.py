def deposit(balance, amount):

    balance = balance + amount

    print(f"The amount of ${amount} has been deposited into your account")
    print("Your new balance is:", balance)

    return balance


def wd(balance, amount):

    if amount > balance:

        print("Insufficient balance")
        return balance

    else:

        balance = balance - amount

        print(f"The amount of ${amount} has been withdrawn from your account")
        print("Your new balance is:", balance)

        return balance


def pin_change(pin, new_pin):

    if new_pin == pin:

        print("The new pin must be different from the old pin")
        return pin

    else:

        pin = new_pin
        print("PIN changed successfully")
        return pin


balance = 5000
pin = 1234

print("Welcome to the ATM")

pin_enter = int(input("Enter your pin: "))

if pin_enter == pin:

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("5. Pin Change")

    opt = 0

    while opt != 4:

        opt = int(input("\nChoose option: "))

        if opt == 1:

            print("Your balance is $", balance)

        elif opt == 2:

            dep = int(input("How much money do you want to deposit: "))
            balance = deposit(balance, dep)

        elif opt == 3:

            wa = int(input("How much money do you want to withdraw: "))
            balance = wd(balance, wa)

        elif opt == 4:

            print("Thanks for using this ATM")

        elif opt == 5:

            new_pin0 = int(input("Enter your new PIN: "))
            pin = pin_change(pin, new_pin0)

        else:

            print("Invalid option")

else:

    print("PIN Invalid")