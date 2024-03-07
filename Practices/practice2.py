#set difference
A = {2, 3, 5}
B = {1, 2, 6}

# method 1 - difference using -

print("diff with -:", A -B)

print("diff with difference():", A.difference(B))

# set symmetric difference

# method 1. - using ^

print('using ^:', A ^ B)

# method 2. - using symmetric_difference

print('using symmetric_difference: ', A.symmetric_difference(B))

# check if two sets are equal

if A == B:
    print('Equal')
else:
    print('Not Equal')

    