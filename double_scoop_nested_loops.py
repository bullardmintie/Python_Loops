# Simulate a mood tracker that records your mood at three different
# times of the day (morning, afternoon, evening) for each day of the week.
# Use nested loops to implement this: the outer loop should iterate over
# the days, and the inner loop should iterate over the times of the day.
# For each time, randomly select a mood from a predefined list and print it.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["Morning", "Afternoon", "Evening"]
mood = ["Happy", "Sad", "Energetic", "Calm"]

import random

for x in range(len(days)):
    print("On " + days[x])
    for y in range(len(time_of_day)):
        print("in the " + time_of_day[y])
        print(random.choice(mood))