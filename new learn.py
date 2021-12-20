# patient_name = "John smith"
# patient_age = 20
# new_patient =True

# name = input("what is your name:")
# color = "likes blue"
# print(name + " " + color)

# weight = input("enter weight here (lbs): ")
# convert_kg = int(weight) * 0.45
# print(convert_kg) 
# 
# course = 'Python Course for "Beginners"'
# print (course)  

# course = '''
# # Hi Sarah, this is our first 
# # email to you

# # Thank you
# # The Support Team
# # '''
# course = 'Python for Beginners'
# # another =course[:]
# print(course [1:-1])

# first = 'Sarah'
# last = 'Akan'
# # message = first + ' [' + last +'] is a coder'
# msh = f'{first} [{last}] is a coder'
# print(msh)

# STRINGS METHODS 
from math import pi
from random import randrange

from ecommerce.shipping import calc_shipping


course = 'Python for Beginners'
#  (len(course))
# print(course.upper())
# print(course.lower())
# print(course)
# print(course.find('o'))
# print(course.replace("Beginner", "absolute beginners"))
# print('python' in course) In Operators

# print(10 ** 3)
# x = 10
# x = x + 3
# # same as
# x += 3


# x = 10
# x = x - 3
# # same as
# x -= 3

# x = 10 + 3 * 2 ** 2
# print(x)

# exponentiation 2 **3
# multiplication or Division
# addition or subtraction

# x = (2 + 3) * 10 - 3

# Math Functions
# x = 2.9
# print(round(x))
# print(abs(-2.9))
# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))  
# 


# IF STATEMENT
# is_hot =False
# is_cold = False
# if is_hot:
#     print("it's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("it is a cold day")
#     print("wear warm clothes")
# else:
#     print("it's a lovely day")
    
# print("Enjoy your day")
         
# house_price = 1000000
# good_credit = True
# if good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price 
# print(f"Down payment: ${down_payment}")

# LOGICAL OPERATORS

# AND: BOTH CONDITIONS MUST BE TRUE
# OR: AT LEAST ONE OF THE OPERATORS MUST BE TRUE
# NOT: CHANGES TRUE TO FALSE

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for loan")

# has_criminal_record = True
# has_good_credit = True

# if has_criminal_record and not has_good_credit:
#     print("Eligible for loan")

# COMPARISON OPERATORS
# temperature = 35
# if temperature > 30:
#     print("it's a hot day")
# else:
#     print("it's not a hot day")

# name = "Sarah Akan"
# if len(name) < 3:
#     print("Name must be at least 3 characters")
# elif len (name) > 50:
#     print("Name must not be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# weight = int(input('weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilo")
# else:
#     converted = weight / 0.45
#     print(f"you are {converted} pounds")

# i = 1
# while i <=5:
#     print("*" * i)
#     i = i + 1
# print("Done")

# WHILE LOOPS(GUESS GAME)
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("you won")
#         break
# else:
#     print("Sorry you failed")


# WHILE LOOPS(CAR GAME)

# command = ""
# started = False
# while True: 
#     command = input('>').lower()
#     if command == "start":
#         if started:
#             print("Car already started")
#         else:
#             started = True
#         print("Car started...")
#     elif command == "stop":
#         if not started:
#              print("car already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print(''' 
#     start - to start the car
#     stop  - to stop the car
#     quit  - to quit the game
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that!")

# for item in range(5, 10, 2):
#     print(item)
# prices =[10, 20, 30]
# total = 0
# for price in prices:
#     total +=price
# print(f"Total: {total}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print('x' * item )

# numbers = [2, 2, 2, 2, 10]
# for item in numbers:
#     output = ''
#     for count in range(item):
#         output += 'x'
#     print(output)

# name = [70, 100, 400, 1000, 200]
# largest =max(name)
# print(largest)

# GETTING THE HIGHEST NUMBER IN A LIST WITH FOR LOOP
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# 2DIMENSIONAL LIST
# (A TWO DIMENSIONAL LIST IS A LIST WHERE EACH
# ITEM IN THAT LIST IS A LIST)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# # matrix[0][1] = 20
# # print(matrix[0][1])
# for row in matrix:
#     for item in row:
#         print(item)
# LIST METHODS
# numbers = [5, 5, 2, 1, 7, 6, 4] 
# uniques= []
# for number in numbers:
#     if number not in uniques
#     uniques.append(number)
# print(uniques)
# numbers.append(20)
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# numbers.index(5)
# numbers.count(5)
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# print(numbers2)
# print(50 in numbers)

# # UNPACKING IN PYTHON
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# x, y, z =coordinates

# DICTIONARIES
# customer = {
#     "name": "Sarah Akan",
#     "age": "25",
#     "is_verified": True
# }
# # customer["name"] = "Usiereidara" (changing a key value)
# customer["birthday"] ="Feb 14 1996"
# print(customer.get("birthdate", "Feb 14 1996"))

# CHANGING NUMBER INTO WORDS EXERCISE
# phone = input("Phone:")
# digit_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = ""
# for char in phone:
#     output += digit_mapping.get(char, "!") + " "
# print(output)

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output

# message = input(">")
# print(emoji_converter(message))


# HOW TO EXCEPT ERRORS IN YOUR CODE
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be 0 ")
# except ValueError:
#     print("Invalid value")

# class Point:
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 50
# print(point2.x)

# CONSTRUCTORS ARE FUNCTIONS THAT GET CALLED AT THE POINT OF CREATING A OBJECT
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
    
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# point = Point(10, 20)
# point.x = 11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name


#     def talk(self):
#         print(f'Hi, I am {self.name}')


# sarah = Person("Sarah Akan")
# sarah.talk()

# usiere = Person("Usiereidara")
# usiere.talk()

# INHERITANCE IS A MECHANISM FOR REUSING CODES

# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")

# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")

# dog1 = Dog()
# Dog.walk()


# How to create and import modules
# import converter
# from converter import kg_to_lbs

# kg_to_lbs(100)

# print(converter.kg_to_lbs(70))

# from utils import find_max

# numbers = [10, 3, 6, 2]
# maximum = find_max(numbers)       
# print(maximum)


# PACKAGES IN PYTHON (THEY ARE ANOTHER WAY TO ORGANIZE OUR CODE)
# 1
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# 2
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# 3
# from ecommerce import shipping

# shipping.calc_shipping()


# BUILT_IN_MODULES





#CALCULATING A SQUARE OF A NUMBER
# # def square(number):
#     return number * number

# print(square(3))







# FUNCTIONS  ARE CONTAINER THAT CONTAIN FEW LINES OF CODE THAT PERFORMS SPECIFIC TASK

# # COMPLETE BANK APP
# import random
# import time
# import ast

# def write_to_file(type, data):
#     if type == 'customer':
#         file = 'bankapp_v3/customers.txt'
#     elif type == 'transaction':
#         file = 'bankapp_v3/transactions.txt'
        
#     with open(file, 'w') as doc_file:
#         doc_file.write(f'{data}')
    

# def read_file_data():
#     trans_file = 'bankapp_v3/transactions.txt'
#     customer_file = 'bankapp_v3/customers.txt'
    
#     with open(customer_file, 'r') as customer:
#         cus_data = customer.read()
#         customer_data = ast.literal_eval(cus_data)
#     with open(trans_file, 'r') as transaction:
#         trans_data = transaction.read()
#         transaction_data = ast.literal_eval(trans_data)   

#     return customer_data, transaction_data

# user_data, transaction_record = read_file_data()

# keep_running = True


# def update_transaction_record(amount, trans_type, transaction, account_num):
#     """This function takes in the amount and other transaction details. Then it updates the transaction dictionary. It doesn't return anything."""
    
#     trans_data = {
#         'amount':amount,
#         'trans_type':trans_type,
#         'transaction':transaction
#         }
                        
#     transaction_record[account_num].append(trans_data)

# def generate_acc_num():
#     num = [str(i) for i in range(10)]
#     acc = ['9']
#     acc.extend([random.choice(num) for i in range(9)])
#     account_num = "".join(acc)
    
#     if account_num in user_data.keys():
#         return generate_acc_num()
    
#     return account_num

# while keep_running:
#     user_activity = input("Enter s to signup, l to login and anyother key to quit\n>>").lower()
#     if user_activity=='s':
#         name = input("Name:\n>>")
#         pin = input("Enter 4 digit pin:\n>>")
        
#         account_num =generate_acc_num()
#         data = [('name', name), ('pin', pin), ('balance', 0)]
#         user_data[account_num] = {}
#         user_data[account_num].update(data)
        
#         #create empty transaction record
        
#         transaction_record[account_num] = []
        
#         print(f"Your account has been successfully activated. Your account number is {account_num}. And your current balance is NGN0.\nPlease login to deposit and perform other transactions.\n\n")
        
        
#     elif user_activity=='l':
#         print("Enter login details below".title())
#         account_num = input("Account num:\n>>")
#         pin = input("Enter 4 digit pin:\n>>")
        
#         account_details = user_data.get(account_num, False)
#         if account_details and account_details.get('pin')==pin:
#             logged_in=True
#             while logged_in:
#                 action = input(f"""Welcome, {account_details.get('name')}!
# What would you like to do?
#     a for account statement
#     b for balance
#     d for deposit
#     t for transfer
#     w for withdrawal
# Press any other key to logout\n>>""").lower()
#                 if action == 'w':
#                     amount = float(input("Enter amount to withdraw\n>>"))
                    
#                     if amount >= account_details.get('balance', 0):
#                         time.sleep(2)
#                         print("Insufficiant funds")
                        
                    
#                     else:
#                         account_details['balance']-=amount
#                         print('Please take your cash')
                        
#                         #save transaction detail
#                         update_transaction_record(amount,"Debit", "Withdrawal", account_num)
                        
#                 elif action == 'd':
#                     amount = float(input("Enter amount to deposit\n>>"))
                    
                    
#                     account_details['balance']+=amount
#                     print('Deposit complete')
                    
#                     #save transaction detail
#                     update_transaction_record(amount,"Credit", "Deposit", account_num)
                        
                      
#                 elif action == 't':
#                     amount = float(input("Enter amount to transfer\n>>"))
#                     recepient_account = input("Enter destination account number\n>>")
                    
#                     recepient = user_data.get(recepient_account, False)
#                     if recepient:
#                         if amount >= account_details.get('balance', 0):
#                             print("Insufficient funds. GERROUT!")
#                         else:
#                             account_details['balance']-=amount
#                             #save transaction detail
                        
#                             update_transaction_record(amount,"Debit", "Transfer", account_num)
                        
#                             recepient['balance']+=amount
                            
#                             #save transaction detail
                        
#                             update_transaction_record(amount,"Credit", "Transfer", recepient_account)
                            
#                             print("Transfer successful. Gerrout!")
                            
#                     else:
#                         print('No active customer for this account number. Gerrout!')
                        
#                 elif action == 'b':
#                     print(f"Your current balance is NGN{account_details['balance']}\n")
                    
#                 elif action == 'a':
                    
#                     if len(transaction_record[account_num]) > 0:
#                         last_5_transactions = transaction_record[account_num][-5:]
#                         print("Here is your last 5 transactions")
#                         for transaction in last_5_transactions:
#                             print("Amount: ", transaction['amount'])
#                             print("Transaction Type: ", transaction['trans_type'])
#                             print("Transaction Ref.: ", transaction['transaction'])
#                             print()
#                     else:
#                         print("You have not made any transactions. Please make a transaction.")
                        
#                 else:
#                     break    
                
#         else:
#             print("Please enter a valid account number and pin")

#     else:
#         print("Sorry to see you go.")
#         break

# write_to_file('transaction',transaction_record)
# write_to_file('customer',user_data)