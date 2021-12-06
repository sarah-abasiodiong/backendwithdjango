import random
# # import time

# users ={
#     "sirdesmond":{
#         "password": 'qwertuiop',
#         "high_score": 0
#     }
# }
# print("welcome to this game")
# while True:
#     input_data = input("Enter l to login or s to signup.\n Enter any other key to quit.\n").lower()
#     if input_data =="l":
#         username = input("username: ")
#         password = input("Password: ")

#         user = users.get(username)

#         if user is not None and user['password'] == password:
#             print("Enter H for help or any other key to continue")
#             user_input =input(">").lower()

#             help_ = '''
#             This is a simple game where you have to guess a word and if your word is equal
#             to the computer's choice then you win!!!
#             '''
#             if user_input =="h":
#                 print(help_)
#             trial = 3
#             scores = 0
#             while trial >0:
#                 my_list =['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
#                 random.shuffle(my_list)
#                 print("\n", my_list)
#                 user_choice = input("\n Guess the word:\n>").lower()
#                 computer = random.choice(my_list)

#                 if user_choice in my_list:

#                     if user_choice == computer:
#                         print("you win")
#                         trial +=1 
#                         print(f"\n {trial} trail(s) left \n)")  

#                         scores +=3
#                         continue
#                     else:
#                         print(f"computer selected {computer}")
#                         print("Try again")
#                 else:
#                     print("invalid input. Try again")
#                 trial -=1
#                 print((f"\n{trial} trials left ]\n"))
#             if scores > user ['high_score']:
#                 user["high_score"] =scores
#         else:
#             print("Please enter a valid username and password")
#     elif input_data =="s":
#         print()
#         username = input("Username: ")
#         password = input("Password: ")

#         users[username] = {
#             'password': password,
#             'high_score': 0
#         }

#     else:
#         print("\n Good bye")                
#         break
#     print(users)

