# Task 1

# A program that accepts user input to create a list of integers. The sums up all the integers in the list
# List comprehension

Request_User = input("Enter the numbers separated by commas:")

original_list = list(map(int, Request_User.split(",")))

List_added = sum(original_list)

print("The list is:", original_list)

print("The sum of the list is:", List_added)








