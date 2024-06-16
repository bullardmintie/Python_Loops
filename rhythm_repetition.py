# Task 1 -- Using the provided genres list, write a for loop that
# prints out each genre with a custom message. Extend this task by
# adding a counter that displays the number of the track before the genre.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number = 1

for x in genres:
    print(f"Track {track_number}: {x} is just a part of the music world!")
    track_number += 1


# Task 2 -- Convert the for loop from Task 1 into a while loop. Ensure
# it performs the same function but also includes a condition to stop
# the loop if a certain genre is played for instance Hip-hop.

c = 0

while c < len(genres):
    current_genre = genres[c]
    if current_genre == 'Hip-hop':
        print(f"Track {c + 1}: {current_genre} is just a part of the music world!")
        print("The music stopped because Hip-hop is playing.")
        break
    else:
        print(f"Track {c + 1}: {current_genre} is just a part of the music world!")
        c += 1


# Task 3 -- Using the range() function, loop through the genres list by
# index. For each genre, print out the track number and a message that the
# light show is ready. Modify the loop to skip a genre if it's not suitable
# for the light show, for instance Classical genre.

index = 0

while index < len(genres):
    current_genre = genres[index]
    print(f"Track {track_number}: {current_genre} The light show is ready!")
    track_number += 1
    index += 1

if current_genre == "Classical":
    print("Not suitable for the light show!")
else:
    print("Enjoy the light show!")