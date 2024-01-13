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
                print("")
                User()

            User.deposit_money(deposit_amount)
            print("")
            print("The sum of ₦{} was deposit succesful in to your account".format(deposit_amount))
            print("")
            User.check_balance()
            print("")
            User.another_transaction_prompt()

        except:
            print("Please, try again later")
            print("")
            quit()

    elif banking_selection == "3":
        print("a")
    elif banking_selection == "4":
        print("")
        print("Thanks for banking with us!")
        print("")
        quit()
    else:
        print("Please Enter 1-4")

#    time.sleep(60)



