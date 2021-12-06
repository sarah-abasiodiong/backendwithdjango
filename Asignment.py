#  1. Join the items of this list to a string sentence. Print the result on the terminal. 
sentence = "I Know Very Well That "
my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
my_new_list1 = " " .join(my_list)
complete_sentence = sentence + my_new_list1
print(complete_sentence)


# 2. Change the value of True in this list to False. Print the result on the terminal

list = ['this', "brown", 55, "oxen", True, 0.85]
list [4] = False
print(list)


# 3. Given the list below:
our_list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
our_list2 = our_list1 [2] [2] [0] + our_list1 [2] [3]
print(our_list2)


#     Get 5000 and 500 out of the list and add them together.
#    Print the result on the terminal
