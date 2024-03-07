student_id = {112, 113, 114, 116, 118, 115}
print("Student ID:", student_id)

mixed_set = {"hello", 101, -2, "bye"} # set of diff data types
print("set of different datatypes:", mixed_set)


# empty set
empty_set = set()

empty_dictionary = {}

print(type(empty_dictionary), "and ", type(empty_set))

numbers = {2, 4, 6, 6, 2, 8}

print(numbers)

numbers.add(10)

print("updated set:", numbers)

companies = {"lacoste", "Ralph Lauren"}

print(companies)

tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print("Updated set:", companies)

# remove ane element from a set

languages = {"swift", "java", "python"}

print("initial set:", languages)

for I in languages:
    print(I)

removedValue = languages.discard("python")

print("set after remove():", languages)

print(all(languages))

# finding no. of set elements

even_num = { 2, 6, 7, 8}
print("set:", even_num)
print("total set length:", len(even_num))

 # python operatios
# union of sets

A = {1, 3, 5, 0, 4}

B = {0, 2, 4}

#method 1 - using |
print("union using |:", A | B)

# method 2 - using union()
print("union using union():", A.union(B) )

#intersection
# method 1 - intersection using &
print('Intersection using &: ', A & B)

# method 2 - intersection using intersection()
print('intersection using inteserction():', A.intersection(B))


 
