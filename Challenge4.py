# a program that accepts user input to create two sets of integers.
# Then intersect both sets

User_set1 = (input("Input numbers  separated by commas: "))

User_set2 = (input("Input numbers separated by commas: "))

set1 = set(map(int, User_set1.split(",")))

set2 = set(map(int, User_set2.split(",")))


print(set1.intersection(set2))


