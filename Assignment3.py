# Write a program that allows customers to:
# 1. Create an account with the account number generated if they do not have an account. All generated account number should begin with 3
# 2. log in to the program if they have an account
# 3. Edit the details of their account.
# 3. Deposit money
# 4. Withdraw money from the account if they have a sufficient amount.
# 5. Users should be able to transfer money to other users in the account
# 6. The code should be able to run 10 times.


# The account data should be stored in a dictionary that looks like this:


   
# data = {
#     '0123445677' : {
#         "name":"John Doe",
#         "password" : "p@$$word",
#         "transaction_pin": "0934",
#         "balance" : 0
#     }
# }




import random
import time
all_details ={}
user ={}
with open('my_transaction.txt', 'r') as file:
    doc = file.read()
    users = eval(doc)

while True:
    print("Welcome to Mulzact Bank")
    print("Enter C to create an account, \r\n L to login ")
    with open('my_transaction.txt', 'w') as file:
        enter = input("Enter: ").lower()
        time.sleep(3)
        if enter == "c":
            user_name = input("Enter your name:\n> ").lower()
            password = input("Enter your password:\n>").lower
            pin = input("Create your transaction pin:\n>").lower()
            current_balance = 0
            new_password= password
            new_pin = pin
            user['name'] = user_name
            user['password'] = new_password
            user['pin'] = new_pin
            user['total balance'] = current_balance
            my_list = random.randrange(300000, 900000)
            newlist = my_list
            all_details[newlist] =[user]
            print(all_details)
            
        elif enter == "l":
            account_input = int(input("Enter your Account Number: \n>"))
            password_input = input("Enter your password: ").lower()
            pin_input = input("Enter your pin: ").lower()
            if account_input == all_details and password_input == user['password'] and pin_input == user["pin"]:
                print("login successful, you can now deposit, withdraw and edit your account")
            else:
                print("Invaid account details")
                    
        if enter == "e":
            print("To edit your account please log in with your account detail")
            edit_login_account = int(input("Enter your account number:\n>"))
            edit_login_password = input("Enter your account number:\n>")
            edit_login_pin = input("Enter your account number:\n>")
            if edit_login_account == all_details and edit_login_password == user['password'] and edit_login_pin == user['pin']:
                print('login successful, you can now edit your account')
                
            else:
                print('invalid account details')
            edit_name_input = input("change your name:\n>").lower() 
            edit_password_input = input("change your password:\n>").lower() 
            edit_pin_input = input("change your pin:\n>").lower() 
            edited_name = edit_name_input
            edited_password = edit_password_input
            edited_pin = edit_pin_input
            user["name"] = edited_name
            user["password"] = edited_password
            user["pin"] = edited_pin

        if enter == "d":
            print(f" your current balance is {user['total balance']}")
            deposit_account_input = input("Enter your account number:\n>").lower() 
            deposit_password_input = input("Enter your password:\n>").lower() 
            deposit_pin_input = input("Enter your pin:\n>").lower() 
            if edit_login_account == newlist and edit_login_password == user['password'] and edit_login_pin == user['pin']:
                print('login successful, you can now deposit to your account')
                print("you can now deposit into your money")
            else:
                print('invalid account details')

            deposit = float(input("Deposit money into account:\n"))
            current_balance = deposit
            print(f"Your new balance is {current_balance}")
        if enter == "w":
            withdraw = int(input("Enter the amount you want to withdraw: "))
            if withdraw > current_balance:
                print("insufficient fund")
            elif withdraw <= current_balance:
                total_balance = current_balance - withdraw
                print(f"your transaction is successful and your new is {total_balance} ")

    transaction_history ={
        all_details: {
            "transaction_type":  "",
            "transaction_amount": "",
            "transaction_recipient": "",
            "transaction_date":  ""

        }

    }  
    with open('my_transaction.txt', 'w') as file:
    #  file.write(f'{dep}')



