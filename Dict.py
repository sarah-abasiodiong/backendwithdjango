# my_dict ={
#          "name": "Sarah",
#           "class":"python",
#           "country": "U.S.A"
# }

# my_class = my_dict["class"]
# my_dict["height"] = 100

# my_username = input('Enter your username:\n>')
# my_dict['username'] = my_username
# # print(my_dict)

# new_dict ={}

# name = input("Enter your name:\n>")
# school = input("Enter your school:\n>")
# class_input = input("Enter your class:\n>")
# state = input("Enter your state:\n>")
# marital_status = input("Enter your status:\n>")

# new_dict['name'] = name
# new_dict['school'] = school
# new_dict['class'] = class_input
# new_dict['state'] = state
# new_dict['marital_status'] = marital_status

# print(new_dict)
# # All_details
# # user ={}

# # firstname = input("Enter your firstname:\n>")
# # lastname =  input("Enter your lastname:\n>")
# # age = int(input("Enter your age:\n>"))
# # yob =  str(2021 - age)
# # username  = firstname [0:3] + lastname [1:] + yob [3:]



# # user['firstname'] = firstname
# # user['lastname'] = lastname
# # user['age'] = age
# # user['yob'] = yob
# # user['username'] = username

# # All_details[username] =[user]


# print(user)


# detail_me ={
#     "name": "Desmond",
#     "occupation": "Backend Dev",
#     "location": "Silicon",
#     "zone": "U.S.A"
# }

# # detail_me["zone"] = "country"
# detail_me["cuuntry"] = detail_me.pop("zone")
# print(detail_me)


# first_list =[2, 3, 4, 5, 6, 7, 8]
# second_list =[4, 9, 16, 25, 36, 49, 64]
# zipped = zip(first_list,second_list)
# dictionary = dict(zip(first_list,second_list))
# tuples = tuple(zip(first_list,second_list))
# sets =set(zip(first_list,second_list))
# # ouput = dict(pre_output)
# # ouput = list(pre_output)
# # ouput = tuple(pre_output)

# print(zipped)
# print(dictionary)
# print(lists)
# print(lists)
# print(tuple)
# print(sets)



# first_list =[2, 3, 4, 5, 6, 7, 84, 9, 16, 25, 36, 49, 64]
# Max = max(first_list)
# Min = min(first_list)


# average =2 + 3 + 4 + 5 +6 +7 + 84 + 9 + 16 + 25 + 36 + 49 + 64
# total_average = average/13
# print(sum(first_list))
# print(len(first_list))
# # print(total_average)
# print(max(first_list))
# # print(min(first_list))
# print(range(0,5))
# print(list(range(0,5)))

# my_fun = lambda a, b, c: (-b + (b**2 - 4*a*c))**0.5/2*a
# print(my_fun(1,2,3)) 

# equation = lambda word: word.lower() 

# print(equation("I LOVE MYSELF"))

# YOU = lambda unique: list(set(unique.lower().split()))
# print(YOU("This a boy good that is very is good"))


# my_func =lambda x:x**2

# my_list = [33, 32, 4, 6, 21, 12]

# mapped = map(my_func, my_list)
# print(list(mapped))

# print(my_func(my_list[3]))









# student_age = input("Enter student ages here:\n>")
# studentage = student_age.split(",")
# new_func =lambda num: int(num)
# mapped = list(map(new_func, studentage))
# student_sum = sum(mapped)
# student_len = len(mapped)
# highest_age =max(mapped)
# lowest_age = min(mapped)
# average = student_sum /student_len
# total_age = student_sum
# total_num = student_len

# print (student_sum)
# print (student_len)
# print (highest_age)
# print (lowest_age)
# print (average)
# print (total_age)
# print (total_num)


# students = input("Enter student ages here:\n>")
# ages = list(map(lambda x:int(x), students.splits()))
# print ("The oldest person is {} years old".format(max(ages)))
# print ("The youngest person is {} years old".format(min(ages)))
# print ("The average age is {} year old".format())
# print (lowest_age)
# print (average)
# print (total_age)
# print (total_num)


# new1 = lambda me: list(me)
# lists = ["adam Freeman", "Alisa Banks", "Ngozi Chukuoma", "John Doe"]
# new = list(map(new1, lists))
# print(new)

# a_list = ["RED", "BLUE", "PURPLE", ]
# results = list(map(list, a_list))
# print(results)


# my_list = ["adam Freeman", "Alisa Banks", "10", "20",  "Ngozi Chukuoma", "24" "John Doe"]
# only_numbers = filter(lambda x: x.isdigit(), my_list)
# print(list(only_numbers))





# Max = max(first_list)
# Min = min(first_list)


# average =2 + 3 + 4 + 5 +6 +7 + 84 + 9 + 16 + 25 + 36 + 49 + 64
# total_average = average/13
# print(sum(first_list))
# print(len(first_list))
# # print(total_average)
# print(max(first_list))
# # print(min(first_list))
# print(range(0,5))
# print(list(range(0,5)))





# get_data = input("Enter data here: ")
# print(get_data) 

# date_of_birth = input()
# year_of_birth = input()
# # print()

# year = 2021
# user_input = int(input("Enter your age: \n>"))
#print (int(user_input))
# yob = year - user_input
# year_to_100 = 100 - user_input
# year_100 = year + year_to_100 

# print(f"You were born in {yob} and it would take you {year_to_100} years to be 100. And that would be in {year_100}")

# people_age = input("Enter: \n>")
# people = people_age.split(',')
# print(people)
# print(":".join)

# import random
# import time
# from datetime import datetime

# dice = [1, 2, 3, 4, 5, 6]
# print("Shuffling......")
# time.sleep(3)
# random.shuffle(dice)
# print('shuffle complete, Computer selecting.......please wait')

# time.sleep(3)

# computer_choice = random.choice(dice)
# # pop_sample = random.sample(dice, 3)
# print(f'Computer selected {computer_choice}')
# print(pop_sample)

# date = datetime.now()

# # print(date.isoweekday, weekday)
# print(date)
# # string_format = datetime.strftime(date,'%A, %d of %B, %Y')
# string_format = datetime.strftime(date,'%d-%b-%y')
# string_format1 = datetime.strftime(date,'%d/%B/%Y')
# string_format2 = datetime.strftime(date,'%B-%Y')
# string_format3 = datetime.strftime(date,'%a. %d %b., %Y')
# # string_format = datetime.strftime(date,'%d-%b-%y')

# print(string_format)
# print(string_format1)
# print(string_format2)
# print(string_format3)

# write a program that take input from the users
# user_age= (input("Enter your age:\n>"))
# if user_age.isdigit():
#     user_age =int(user_age)
#     if user_age < 18: 
#         print("Your are not eligible to vote")
#     elif user_age <=50:
#          print ("You are eligible to vote")
#     else:
#         print("you are overaged")
# else: 
#     print("Invalid Input")

# user_score= int(input("Enter your score:\n>"))

# if user_score < 50: 
#   print("Grade E8 ")
# elif user_score<=70:
#          print ("Grade C6")
# elif user_score>=100:
#     print("Grade A1")
# else:
#      print("")

# import random
# import time

# game = ["name", "musa", "Amina", "gender", "male", "age", "ball", "game", "cherry", "queen" ]
# random.shuffle(game)

# computer_choice = random.choice(game)
# user = input("Enter your name:\n>")
# print(f"Welcome {user} to the Guessing Game, Enter h for instrustion or s to start ")
# user_continue =input("Enter\n>")

# if user_continue == "h":
#     print("Guess a word and if it matches with what the computer picks, you win but if it doesn't matches you lose")
# elif user_continue == "s":
#      print(["name", "musa", "Amina", "gender", "male", "age", "ball", "game", "cherry", "queen" ])
# else:
#     print()
# user_choice = input("Guess a word:")

# time.sleep(3)

# print(f'Computer selected {computer_choice}')


# import random
# from typing_extensions import ParamSpec


# print("Welcome to this game")
# print("Enter H for help or any other key to continue")
# user_input = input('>').lower()
# help_ ="""
# This is a simple game where you have to guess a word and if your word is equal
# to the computer's choice then you win!!!

# Select from the given list words.
# """
# if user_input == 'h':
#     print(help_)
# my_list =['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
# random.shuffle(my_list)
# print(my_list)
# user_choice = input("Guess the word:\n>").lower()
# computer = random.choice(my_list)
# if user_choice in my_list:
#   if user_choice ==computer:
#         print ("You win")
#   else:
#         print(f"Computer selected {computer}")
#         print('try again')
# else:
#     print("invalid input. Game over!!!")



# # bluid a simple ATM
# # create a simple bank app that allows user to signs up
# # {the key of the dict is going to be account number, the value from of the key will 
# # be another dict with{name:, password:, transaction pin: current balance} }

# # welcome to xyz bank 
# # do you have an account or you want to create account and 
# # then ask the person details and then generate account number and the
# #  generated account number must start with 3, but if the person has an account already, 
# let the person login with his account number and password




# print("Welcome to password validated")
# create_password = input('Create a password:\n>')
# if create_password.isalnum() and not create_password.isdigit() and not create_password.isalpha():
#     print("Strong password")
# else:
#     print("weak password try again")

# num =int(input("Enter a number:\n>"))
# prime =True
# if num <=1:
#     prime = False
# if num == 2:
#     prime =True
# for factor in range(2,num):
#     if num%factor == 0:
#         prime == False
#         break
# if prime:
#     print("Prime Number")
# else:
#     print("Not Prime")



# password = input('Create a password:\n>')
# if password.isnumeric():
#    print("invalid password, password must consist of a upper case, lower case, special character and numbers")
# elif password.isalpha():
#     print("invalid password, password must consist of a upper case, lower case, special character and numbers")
# elif password.isdigit():
#     print("invalid password, password must consist of a upper case, lower case, special character and numbers")
# elif password.islower():
#     print("invalid password, password must consist of a upper case, lower case, special character and numbers")
# elif password.isupper():
#     print("invalid password, password must consist of a upper case, lower case, special character and numbers")
# # elif special_characters:
# #     print('invalid password')
# else:
#     # password = True
#     print('Valid Password')



# corrections
# password = input("Enter your password. Password must contain:\r\n at least an integer, \r\na capital letter, \r\na small letter, \r\n a specialcharacter \r\n and must be more than 8 characters\r\n>")
# special_char = ['@', '$', '#']
# isvalid = True

# if len(password) < 6:
#     print("password length should not be less than 6")
#     isvalid=False
# if len(password) > 16:
#     print("password length should not be more than 16")
#     isvalid = False
# if not any(char.isdigit() for char in password):
#     print("Password should contain at least a number")
# if not any(char.islower() for char in password):
#     print("Password should contain at least a lowercase letter [a-z]")
#     isvalid =False
# if not any(char.isupper() for char in password):
#     print("Pasword should contain at least a special character [A-Z]")
#     isvalid = False
# if not any(char in special_char for char in password):
#     print("Pasword should contain at least a special character [@$#]")
#     isvalid = False
# if isvalid:
#     print("Password is valid")
# else:
#     print("Invalid Password")




# WEEK 5

# my_list = []

# for i in range(5):
#     my_list.append(i**2)

# a_list = [i**2 for i in range(5)]
# print(a_list)

# b_list = [element+1 for element in range(10) if (element+1)%2==0]
# print(b_list)

# my_dict ={element: element**2 for element in range(10)}
# print(my_dict)


# string = "here are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even "
# my_dict1 = {}
# for i in string.split():
#     my_dict1[i] = my_dict1.get(i, 0) + 1
# # {element: string.split() for element in string }
# print(my_dict1)

import time
# count = 10
# while count >= 0:
#     print(count)
#     count -=1
#     time.sleep(3)

count_number = int(input("Enter a number: "))
if count_number >= 0:
    while count_number >0:
        print(count_number)
        count_number-=1
else:
    while count_number <= 0:
        print(count_number)
        count_number +=1
time.sleep(3)



# while True:
#     if count_number %2 ==0:
#         count_number +=1 
#     else:
#         count_number %2 ==count_number
#         count_number -=1


#     print(count_number)
   
    



