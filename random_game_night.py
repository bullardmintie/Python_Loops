# Create a game where a player has a list of items. They have to
# guess which item in the list was selected. Use random.choice()
# to select the item and take the user's guess via input. Provide
# feedback on whether they guessed correctly or not.

super_heroes = ["superman", "supergirl", "batman", "spiderman", "captain america", "iron man"]
guess = input("Guess which super hero is most popular? ")

import random

picked = random.choice(super_heroes)
print(picked)

if guess == picked:
    print("Good job! You're right!!")
else:
    print("Oops...try again!")