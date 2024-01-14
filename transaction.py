#!/usr/bin/python3
import json
import datetime
import random

class Transaction:
    transaction_id = 0

    def __init__(self):
        Transaction.transaction_id += 1

    def prompt(self):
        print("--------------------------------------------------")
        print("--------------------------------------------------")
        print("----------------Welcome to BankXYZ----------------")
        print("")
        print("1.) - Check Balance")
        print("2.) - Deposit Money")
        print("3.) - Withdraw Money")
        print("4.) - Quit")
        print("")

    def another_transaction_prompt(self):
        print("Do you want to perform another transaction?")
        print("")
        print("1.) Yes")
        print("2.) No")
        print("")
        yesno = input("Enter an option: ")
        print("")
        try:
            if yesno == "1":
                User = Transaction()
            elif yesno == "2":
                print("")
                print("Thanks for banking with us!")
                print("")
                quit()
        except Exception:
            self.another_transaction_prompt()

    def check_balance(self):
        with open("account_info.json", "r") as f:
            data = json.load(f)
        print("")
        print("Your balance is ₦",end="")
        print(data["account_balance"])
        print("")

    def deposit_money(self, amount):
        """Makes changes to account_info"""
        self.amount = amount

        with open("account_info.json", "r") as f:
            data = json.load(f)
            old_balance = data["account_balance"]
            new_balance = old_balance + self.amount
            with open("account_info.json", "w") as f:
                data["account_balance"] = new_balance
                json.dump(data, f)

    def deposit_success_prompt(self, deposit_amount):
        """Returns a success message"""
        print("")
        print("The sum of ₦{} was succesfully depositted into your account".format(deposit_amount))
        print("")

    def withdraw_money(self, amount):
        if type(amount) != int:
            raise TypeError("Please Enter a Valid Amount")
        elif amount < 0:
            raise ValueError("To little to withdraw")
        else:
            self.amount = amount
            with open("account_info.json", "r") as f:
                data = json.load(f)
                old_balance = data["account_balance"]
                new_balance = old_balance - self.amount
            with open("account_info.json", "w") as f:
                data["account_balance"] = new_balance
                json.dump(data, f)

    def happy_quit(self):
        print("")
        print("Thanks for banking with us!")
        print("")
        exit()

    def sad_quit(self):
        print("")
        print("Please, try again later")
        print("")
        quit()

    def print_receipt_prompt(self):
        print("")
        print("Do you want to print receipt?")
        print("")
        print("1.) Yes")
        print("2.) No")
        print("")
        print_yesno = input("Enter an option: ")
        print("")
        try:
            if print_yesno == "1":
                self.print_receipt()
            elif print_yesno == "2":
                self.another_transaction_prompt(self)
        except Exception as err:
            print(f"Unexpected {err}, {type(err) = }")

    def print_receipt(self):
        now = datetime.datetime.now()
        transaction_date = now.strftime("%Y-%m-%d %H:%M:%S")
        receipt_number = random.randint(1, 9) * 100000 + random.randint(0, 99999)
        client_number = random.randint(1, 9) * 100 + random.randint(0, 999)
        pan_1 = random.randint(1, 9) * 1000000 + random.randint(0, 999999)
        pan_2 = random.randint(1, 9) * 1000 + random.randint(0, 99)
        trans_ref = random.randint(1, 9) * 100 + random.randint(0, 99999)

        print("__________________________________________________")
        print("__________________________________________________")
        print("__________________________________________________")
        print("")
        print("------------------*** BANKXYZ ***-----------------")
        print("")
        print("--------------*** CUSTOMER'S COPY ***-------------")
        print("")
        print("TERMINAL                     ATM")
        print("RECEIPT NO                   {}".format(receipt_number))
        print("DATE & TIME                  {}".format(transaction_date))
        print("CARD                         MASTERCARD")
        print("CLIENT                       0000{}".format(client_number))
        print("PAN                          {}*****{}".format(pan_1, pan_2))
        print("TRANSACTION REF              NGR|LG|{}".format(trans_ref))
        print("AMOUNT                       {}".format(self.amount))
        print("STATUS                       APPROVED")
        print("")
        print("__________________________________________________")
        print("__________________________________________________")
        print("__________________________________________________")
