first_integer = 99
# print(first_integer)

new_home = "So I could just type something reallu long!" 
# print(new_home)
# print(type(new_home))


my_verdict = True
#nt(my_verdict)

random_items =['music', "sports", True, "Fasle", 99.0]
#print (random_items)

states = {"Kebbi", "Imo", "Lagos", "Delta" }
# print(states)

my_info = {"name" : "musa", "gender" : "male", "age"  : 11}
# print(my_info)

my_info = {"name" : ["musa", "Amina"], "gender" : "male", "age"  :[11, 15]}
# print(my_info)

the_remainder = 55 % 6
# print(the_remainder)


quick_check = 49 ==109
# print(quick_check)

test_check = 49 != 49
# print(test_check)

final_verdict = not((58>=42) or (60 !=60)) or (("Rain" == "rain") and not (82.2 >= 82.2))
# print (final_verdict)

feedback = 20 is 20 
# print(feedback)

first = [29, "True", "Sunny"]
second = [29, "True", "Sunny"]
output = first == second
# print(output)

check_member = "e w" in "monry makes the world go round"
# print(check_member)
list_of_scores =[ 63, 78, 90, 52, 99, 81]
# check_scores


first_phrase = "The boy"
second_phrase = "in my class is handsome"

full_sent = first_phrase + " " + second_phrase
# print(full_sent)


new_chunk = second_phrase[ -23:-12 ]
# print(new_chunk)


weather = "sunny"
temperature = "39 degrees"
weather_report = "it is quite {} with a temperature of {} ".format(weather, temperature)
# print(weather_report)

# using f string
weather_report2 = f"it is quite {weather} with a temperature of {temperature}"
# print(weather_report2)

source_of_income = 'The nation\'s crude oil'

new_weather_report = "!It is quite sunny despite the downpour all through the night!"
mod_one = new_weather_report.title()
# print(mod_one)

mod_two = new_weather_report.startswith("it ")
# print(mod_two)

mod_three = new_weather_report.find("day")
# print(mod_three)

mod_four = new_weather_report.split(" ")
# print(mod_four)

mod_five = " ".join(mod_four)
# print(mod_five)

mod_six = new_weather_report.count("the")
# print(mod_six)

mod_seven = new_weather_report.replace("p", " ")
# print(mod_seven)

mod_eight = new_weather_report.rstrip("!")
# print(mod_eight)

new_collection =[6, True, 12, 9, False, "name", "Bentley", "Football", 9.7, None, 8.5]
desired_item = new_collection[4]

desired_portion =new_collection[-6: -2: 2]
# print(new_collection)

new_collection[5] = "school"
# print(new_collection)

new_collection[1 : : 3] = ["money", "Food", "iKOYI", "Glass" ]
# print(new_collection)

# short_list = [3, 6, 7]
# short = [8, 9, 10]
# new_list = short_list + short
# # print(new_list)

sports = ["Basketball", "Boxing", "Swimming"]
stars = ["Kobe Bryant", "Mike Tyson", "Michael Phelps"]

sports.extend(stars)
# print(sports)

new_collection.remove(9)

new_collection.append("Biscuit")
# print(new_collection)

backup_collection = new_collection.copy()
# print(backup_collection)

new_collection.insert(2, "Holiday")
# print(new_collection)

sports.sort(reverse= True)
# print(sports)

scores =(58, 73, 85, 67)
desired_score =scores[-1]
# print(desired_score)

grocery_card1 ={"Ham", "Burger", "Youghurt", "Eggs", "Cookies", "Bread", "Sausage"}
grocery_card2 ={"Beverage", "Cookies", "Wine", "Frozen Turkey", "Burger", "Eggs"}
# print(grocery_card1)
# print(grocery_card2)
grocery_card1.discard("Ham")
grocery_card1.add("Cheese")
# print(grocery_card1)

full_card = grocery_card1.union(grocery_card2)
# print(full_card)
# grocery_card1.update(grocery_card2)
# print(grocery_card1)

# grocery_card2.difference_update(grocery_card1)
# print(grocery_card2)

common_groceries = grocery_card1.intersection(grocery_card2)
# print(common_groceries)

grocery_card1.symmetric_difference_update(grocery_card2)
# print(grocery_card1)

# Dictionary
customer_info ={
    "name" :["adam Freeman", "Alisa Banks", "Ngozi Chukuoma", "John Doe"],
    "gender" : ["Male", "Female", "Female", "Male"],
    "nationality" : ["American", "Canadian", "Nigerian", "British"]
}

all_names = customer_info["name"]
# print(all_names)
all_names[2]="Ngozi Nnamdi"
# print(all_names)

all_entries = customer_info.items()
# print(all_entries)

customer_info.update({"age " : [31, 34, 20, 22]})
# print(all_entries)

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

# my_self = "I AM A BOY"
# lower = my_self.lower()
# print( lower.replace(" ", "-"))

# text ="""
#  Data Science is a subset of AI which deals with the use of processes,
#  algorithms and systems to glean out insight from structured and unstructured data.
#  This entails Data Mining, Data Wrangling, Data Analysis, Statistics, Data Visualization, 
#  Database Management and Predictive Analytics/Machine Learning
# """
# findit = input("Enter the word you want to search for. \n>").lower()
# text = text.lower()
# print(f'\n{text.count(findit)} result(s) found. \n')
# print(text.replace(findit, findit.upper()))

# firstname = input("Firstname:" )
# lastname = input("Lastname:" )
# newname = lastname [0:3] + firstname [-3:]
# print(newname.lower())



# a = [1,2,3,4,5,6,7,[2,1,2 3,4]]
# a.inset(5, i just got interview)
# a[-1 .insert(2, boy)]
# print(a[-1])

# print(-1)

# 
# a_list = ['This', 'is', 'a', 'list', 'and', 'I', 'am', 'happy', 'about', 'this', 'list']
# print(a_list.pop(4)) 
# print(a_list.remove('This'))
# print(a_list)

# a = input ('Enter your word: ')
# a_list.remove(a)

# popped = a_list.pop(a_list.index ('about'))
# print (popped)

# a_list[0], a_list[4] = 'and', 'This'
# print(a_list)

# a_list.sort()
# # c_list = a_list.copy()

# # a_list[0] = 'changed'

# # print(a_list)
# # print(b_list)
# # print(c_list)

# my_list =[54, 44, 27, 79, 91, 41]
# index_4 = my_list.pop(4)
# my_list.insert(1, index_4)
# my_list.append(index_4)
# print(my_list)

# a = {1, 5, 7, 2}
# b = {5, 2, 9, 6}

# c = a.union(b)
# print(a)
# print(c)

# a.update(b)
# print(a)

# c = a.intersection(b)
# print(c)
# a.intersection_update(b)
# print(a)


# c = a.difference(b)
# print(c)
# a.difference_update(b)
# print(a)

# c = a.symmetric_difference(b)
# print(c)
# a.symmetric_difference_update(b)
# print(a)

# english = input("Enter number here: ")
# french = input("Enter number here: ")

# english1 = (set(english.split(' ')))
# french1 = (set(french.split(' ')))

# both = english1.union(french1)

# print(len(both))

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# print("original list", sample_list)

# sample_list = list(set(sample_list))
# print("uni")
# unique_list = tuple(sample_list)
# print(unique_list)

#

