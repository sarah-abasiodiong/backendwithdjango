# import datetime
# class Shoe():
#     brand = "Nike"
# # MAGIC METHOD
#     def __init__(self, type, size, price):
#         self.type = type
#         self.size = size
#         self.price = price
    
#     def __str__(self):
#         return f'{self.type} {self.size} {self.price}'
    
#     def __add__(self, other):
#         if isinstance(other, Shoe):

#             return self.price + other.price


#         raise TypeError(f"Expected type {type(self)} but got {type(other)}")

#     def __get_yob(self):
#         ''''This is a private method that callculates the year of birth.
#         Return:
#             [int]
#         '''
        

#         year = datetime.now().year
#         return year - self.age
#     def child_support(self):
#         if self.__get_yob() <=1990:
#             return 2500
#         else:
#             return 0
# # INSTANCE METHOD
#     def discount(self):
#         ''''This function calculates the discount given to a customer if he or she buy a certain amount
#         Returns: [int]: [10 percent of the discount given]
#         '''
#         discount_price = 5000
#         if self.price >= discount_price:
#             discount_price = self.price *0.1

#             return discount_price
#         else:
#             return 0
    
#     @property
#     def take_home_salary(self):
#         return self.price + self.discount 
    
# shoe1 = Shoe("sandal", 32, 1000)
# shoe2 = Shoe("kitto", 42, 10000)


# # print(shoe1.discount())
# # print(shoe2.discount())
# # print(shoe1 + shoe2)
# class New(Shoe):
#     def __init__(self, type, size, price, country):
#         self.country = country
#         super().__init__(type, size, price)
    
#     @property
#     def join_everything_together(self):
#         return self.size + self.price


# import1 = New("Puma", 45, 50000, "uk")
# import2 = New("Addidas", 48, 60000, "England")

# print(import1 + import2)

# d def new_line():
#     print('.')


# def three_lines():
#     new_line()
#     new_line()
#     new_line()


# def nine_lines():
#     three_lines()
#     three_lines()
#     three_lines()

# def twenty_five():
#     nine_lines()
#     nine_lines()
#     three_lines()
#     three_lines()
#     new_line()


# twenty_five()

# def add_value(func):
#     def wrapper():
#         original_result = func()
#         modified =original_result.split("!")[0] + " world!" 
#         return modified
#     return wrapper


# @add_value
# def greet():
#     return 'Hello!'

# print(greet())


user = {}

def authenticate(func):
    def inner():
        username = input("Username:\n>")
        password = input("Password:\n>")

        if user.get(username) != None and user.get(username)['password'] == password:
            return save_payment
        else:
            print("Invalid login")
            return
    return inner




@authenticate
def save_payment():
    print("Your payments has been saved!")


save_payment() 






from datetime import datetime


class Employee():
    
    company = "OK-HI"
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f'{self.name} {self.age} {self.salary}'
    
    
    def __add__(self, other):
        if isinstance(other, Employee):
            
            return self.salary + other.salary
        
        raise TypeError(f"Expected type {type(self)} but got {type(other)}")


    def __get_yob(self):
        """This is a private method that calculates the year of birth.
        Returns:
            [int]: [year of birth]
        """
        
        year = datetime.now().year
        return year - self.age
    
    
    def bonus(self):
        """This function calculates the bonus of an employee if the age is greater or equal to a threshold age.
        Returns:
            [int]: [10 percent of the employee's salary]
        """
        bonus_age = 30
        if self.age >= bonus_age:
            bonus_amount = self.salary * 0.1
            
            return bonus_amount
        
        else:
            return 0
        
        
    def child_support(self):
        if self.__get_yob()  <= 1990:
            return 2500
        
        else:
            return 0
            
    
    @property
    def take_home_salary(self):
        return self.salary + self.bonus() + self.child_support()
    
    

employee1 = Employee("John Doe", 32, 32000)
employee2 = Employee("Jane Doe", 29, 30000)
# employee3 = Employee("Me", 3, 3333)

# print(employee1)
# print(employee1. child_support())
# print(employee2.child_support())

# print(employee1 + employee2)

print(employee1.take_home_salary)




class EngineeringTeam(Employee):
    
    def __init__(self, name, age, salary, track):
        self.track = track
        super().__init__(name, age, salary)
        
        
        
    
        
        
engieering1 = EngineeringTeam("Desmond", 12, 2000000, "Fullstack")
engieering2 = EngineeringTeam("Jack", 15, 2000030, "Backend")

print(engieering1 + engieering2)