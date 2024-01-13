#!/usr/bin/python3
import json

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

    def prompt_yesno(self):
        print("")
        print("1.) Yes")
        print("2.) No")
        print("")

    def check_balance(self):
        with open("account_info.json", "r") as f:
            data = json.load(f)
        print("")
        print("Your balance is ₦",end="")
        print(data["account_balance"])
        print("")

    def deposit_money(self, amount):
        if type(amount) != int:
            print("Please Enter a Valid Amount")
        elif amount < 0:
            print("Are you depositing or withdrawing?")
        else:
            self.amount = amount

            with open("account_info.json", "r") as f:
                data = json.load(f)
                old_balance = data["account_balance"]
                new_balance = old_balance + self.amount
                with open("account_info.json", "w") as f:
                    data["account_balance"] = new_balance
                    json.dump(data, f)

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
