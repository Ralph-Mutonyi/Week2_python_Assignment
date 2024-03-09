# create a list of words
# use list comprehnsion to create a new list that only contains words that have odd no of characters


list_of_football_clubs = ["Real Madrid", "Manchester city", "bayern muchen", "Juventus", "ac milan", "Liverpool", "Napoli", "Inter Milan", "Tottenham", "atletico Madrid", "Barcelona"]

odd_character_clubs_only =[i for i in list_of_football_clubs if len(list_of_football_clubs) % 2 != 0]

print(odd_character_clubs_only)