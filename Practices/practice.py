Countries = {
    "Nepal": "kathmandu", 
    "Italy": "Rome",
    "England": "London"

}

Countries["japan"] = "Tokyo"

print(Countries)

Numbers = {
    1: "One",
    2: "Two",
    3: "three "
}

print(Numbers)

student_id = {
    111: "erick",
    112: "Kylie",
    113: "Butters"
}

print(student_id)

student_id[112] = "stan"

print("changed student-id:", student_id)

#membership test

print(114 in student_id)

print(114 not in student_id)

#iterating through dictionary-  use a loop

for student_id in student_id:
    print(student_id)

