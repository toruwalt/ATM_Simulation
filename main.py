#!/usr/bin/python3
#import ATM.transaction
T = __import__('transaction').Transaction

u = T()
u.check_balance()
u.deposit_money(1500)
u.check_balance()
u.withdraw_money(1000)
u.check_balance()
