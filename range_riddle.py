# Write a program that prints off different moods for each day of the week.
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
# Using the range() function, loop through the days of the week and for
# each day, randomly select a mood from the list and print it. Ensure that
# your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were
# feeling happy." "On Thursday you were feeling sad."

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mood = ["Happy", "Sad", "Energetic", "Calm"]

import random

for x in range(len(days)):
    print("On " + days[x] + " you were feeling " + (random.choice(mood)))