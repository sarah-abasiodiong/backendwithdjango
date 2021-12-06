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

# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)": "😊",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#    output += emojis.get(word, word) + " "
# print(output)

# FUNCTIONS  ARE CONTAINER THAT CONTAIN FEW LINES OF CODE THAT PERFORMS SPECIFIC TASK

