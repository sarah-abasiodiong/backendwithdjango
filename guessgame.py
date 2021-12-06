
import random
# import time
# def play_game(trial, scores):
with open('my_game.txt', 'r') as file:
    doc = file.read()
    users = eval(doc)

print("welcome to this game")
while True:
    input_data = input("Enter l to login or s to signup.\n Enter any other key to quit.\n").lower()
    with open('my_game.txt', 'w') as file:
        if input_data =="l":
            username = input("username: ")
            password = input("Password: ")

            user = users.get(username)

            if user is not None and user['password'] == password:
                print(f"Enter H for help or any other key to continue, yourhighscore is {user['high_score']}")
                user_input =input(">").lower()

                help_ = '''
                This is a simple game where you have to guess a word and if your word is equal
                to the computer's choice then you win!!!
                '''
                if user_input =="h":
                    print(help_)
                trial = 3
                scores = 0
                while trial >0:
                    my_list =['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
                    random.shuffle(my_list)
                    print("\n", my_list)
                    user_choice = input("\n Guess the word:\n>").lower()
                    computer = random.choice(my_list)

                    if user_choice in my_list:

                        if user_choice == computer:
                            print("you win")
                            trial +=1 
                            print(f"\n {trial} trail(s) left \n)")  

                            scores +=3
                            continue
                        else:
                            print(f"computer selected {computer}")
                            print (f"your new highscore is {user['high_score']}")
                            print("Try again")
                    else:
                        print("invalid input. Try again")
                    trial -=1
                    print((f"\n{trial} trials left ]\n"))
                if scores > user ['high_score']:
                    user["high_score"] =scores
            else:
                print("Please enter a valid username and password")
        elif input_data =="s":
            print()
            username = input("Username: ")
            password = input("Password: ")

            users[username] = {
                'password': password,
                'high_score': 0
            }
        

        else:
            print("\n Good bye")                
            break

with open('my_game.txt', 'w') as file:
     file.write(f'{users}')


# def calc(a , b):
#     c = (a + b )/ 2

#     return c
# print(calc(2, 3))

# write a function that in any number and return true or false depend on it self

# def find_prime(n):
#     if n <=1:
#         return False
     
#     if n == 2:
#          return True

#     for factor in range(2, n):
#         if n %factor == 0:
#             return False
  
#     else:
#         return True
# print(find_prime(7))

# def add_num(**args):
#     return sum(args)

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5,]
# print(add_num(*data))


# def adsss(**kwargs):
#     print(kwargs)

# def ads(a, b, c):
#     return a*b+c

# a = {'a':3, 'b' : 4, 'c' : 2}
# #adsss(**a)
# print(ads(**a))


#         # for i in range(10): 
        
#     #         print("Welcome to this Mousi guess game")
#     #         print("Do you have account enter P to login with your password \r\n enter S to sign up\r\n ")

#     #         user_input = input('>').lower()
#     #         if user_input == "S":
#     #             user_name = input("Enter your name:\n> ").lower()
#     #             user_password = input(" Create your password:\n>").lower
#     #             name = user_name
#     #             password = user_password
#     #             highscore = 0
        
#     #         if user_input == "P":
#     #             password_input = input("Enter your password here: ")
#     #             if password_input == password:
    #                 print("Login successful")
    #                 print("""
    #                 This is a simple game where you have to guess a word 3 times and if your word is equal
    #                 to the computer's choice then you win points on each time you but if you don't guess correctly you loose!!!

    #                 Select from the given list words.
    #                 """)
    #                 my_list =['cherry', 'queen', 'ball', 'ace', 'hearts', 'jack']
    #                 random.shuffle(my_list)
    #                 print(my_list)
    #                 user_choice = input("Guess the word:\n>").lower()
    #                 computer = random.choice(my_list)
    #                 if user_choice in my_list:
    #                     if user_choice ==computer:
    #                         print (f"You win and your highscore is {highscore}   ")
    #                 else:
    #                         print(f"Computer selected {computer}")
    #                         print('try again')
    #         else:
    #             print("invalid input. Game over!!!")

