"""
👾💻Final Challenge: Create a program that simulates an ATM withdrawal process. 

The program should:
Allow the user to input an amount to withdraw.
Raise an exception if the input is invalid (non-numeric or negative). ✅
Ensure that the withdrawal doesn’t exceed the account balance, raising an appropriate exception. ✅
Always display the remaining balance, even if an error occurs.
"""

import time


def atm_withdraw(amount: float, account_balance: float):

    if not isinstance(amount, float) or amount < 0:
        raise ValueError("Error: Please enter a positive numeric amount.")

    if amount > account_balance:
        raise ValueError("Error: Insufficient funds.")

    print("Withdrawal successful.")
    time.sleep(0.5)

    return account_balance - amount


def atm():
    user_account = {
        "account_holder": "John Doe",
        "account_balance": 1500.00,
        "account_number": "1234567890",
        "account_type": "Checking",
    }

    withdraw_amount = float(input("Please enter the amount to withdraw: "))
    time.sleep(0.5)

    try:
        remaining_balance = atm_withdraw(
            withdraw_amount, user_account["account_balance"]
        )

        user_account["account_balance"] = remaining_balance
    except ValueError as e:
        print(e)
    else:
        print(f"Remaining balance: {remaining_balance}")
        time.sleep(0.5)


# Program execution

atm()
