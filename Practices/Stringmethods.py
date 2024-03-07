#string and string methods

string1 = "python programming"

print(string1, "Datatype of string1:", type(string1))

# access first index

print(string1[0])

# negative indexing 

print(string1[-3])

# slicing - get a specific range of characters (use:)

print(string1[1:4])

# strings are immutable
# multistring lines


# string operations

str1 = "hello, world"

str2 = "Hello, world"

str3 = " i love kenya"

# compare str1 and str2

print (str1 == str2)

# joining 2 or more string using +

result1 = str1 + str3

print(result1)

# iterate through a string

for I in str3:
    print(I)

#length of a string
    
print(len(str3))

#membership operator

print("i" in str3 )

print('h' not in str3)

# other methods
#.upper() - to upper case
#.lower() - to lower case
#partition()- returns a tuple


#escape sequences in python - escape some characters present in a string

example = "he said, \"what's there?\""

print(example)

example1 = 'he said, "what\'s there?"'

print(example1)

# python string formatting(f-strings)= formated string literal
# make it easy to print variables
# more flexible and dynamix way of creating strings
name = 'carthy'

country = 'UK'

print(f'{name}  is from {country}')


