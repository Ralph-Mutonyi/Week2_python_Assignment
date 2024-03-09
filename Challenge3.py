full_name = input("What is your name?:")
age = int(input("How old are you?:"))
favourite_color = input("What's your favourite color?:")

personal_info = {
    "full_name": full_name,
    "age": (age),
    "favourite_color": favourite_color,
}

print(personal_info)

# better and improved code below

#incorperate an error handling measure incase the user doesnt enter required input

while True:
    try:
        full_name1 = str(input("What is your full name?:"))
        age1 = int(input("How old are you?:"))
        favourite_color1 = str(input("What is your favourite color?:"))
        break
    except ValueError:
        print("Please enter a valid age(number).")

personal_info = {
    "full name": full_name1,
    "age": age1,
    "Fav color": favourite_color1,
}

print(personal_info)