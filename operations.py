#!/usr/bin/python3
import time
Transaction = __import__('transaction').Transaction


while True:
    User = Transaction()
    User.prompt()

    banking_selection = input("Enter an option: "  )
    if banking_selection == "1":
        User.check_balance()
        User.another_transaction_prompt()

    elif banking_selection == "2":
        print("")
        print("How much would you like to deposit today?")
        print("")

        deposit_amount_test = input("Please input an amount: ₦")
        try:
            deposit_amount = int(deposit_amount_test)
            if deposit_amount < 500:
                print("")
                print("Minimum Deposit is ₦500")
                print()
                quit()

            elif deposit_amount > 500000:
                print("")
                print("Maximum Deposit is ₦500000")
                print("")
                quit()

            User.deposit_money(deposit_amount)
            User.deposit_success_prompt(deposit_amount)
            User.print_receipt_prompt()
            print("")
            User.another_transaction_prompt()

        except:
            quit()

    elif banking_selection == "3":
        print("a")
    elif banking_selection == "4":
        User.happy_quit()
    else:
        print("")
        print("Select options 1 to 4 to Proceed")
        print("")




