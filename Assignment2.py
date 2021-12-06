# 1. 
# Write a Python program that accepts the radius of a circle from the user and computes the area. 

# Answer 1
# radius = float(input("Enter radius of circle:\n> "))
# computed = 3.14159 * radius * radius
# print("Area of circle =", computed)

#corrections 1
# import math
# r = int(input("Enter radius:\>"))
# print(math.pi * (r**2))


# 2. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.

# Answer 2
# user_input = input("Enter number here\n>")
# user_input1 = user_input.split(",")
# print(tuple(user_input1))
# print(list(user_input1))

# correction 2
# seq = input("Enter numbers separated by comma:\n>")
# to_list = seq.split(',')
# to_tuple = tuple(to_list)
# print(to_list)
# print(to_tuple)

# 3. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# Answer 3
# user_firstname =input("Enter your name here:")
# user_lastname = input("Enter your name here:")
# print( user_firstname[::-1] + " " + user_lastname[::-1])

# # correction 3
# name = input("Enter your name:\n>")
# names = name.split()
# print (name[1] + " " + names[0])



# 4. Write a Python program to concatenate all elements in a list into a string and return it

# Answer 4
# def concatenate_list_data(list):
#     result = ''
#     for element in list:
#         result += str(element)
#     return result
# print(concatenate_list_data([1, 5, 12, 2]))


# correction 4
# elements = ["this", "girl", "is" "26"]
# elements =list(map(str, elements))
# print(" ".join(elements))





