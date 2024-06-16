# Task 1 -- Loop through a slice of the genres list from the
# previous question and print out the genres. Use slicing to
# create a sublist of genres from the second to the fourth track.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genres_slice = genres[1:4]

print(genres)
print(genres_slice)


# Task 2 -- Use a list comprehension to create a new list that contains
# each genre with the word "Music" appended to it. Print this new list.

new_genres = [x for x in genres]

new_genres.append('Music')
print(new_genres)


# Task 3 -- Write a loop using range() to print out a countdown from
# 10 to 1, followed by the message "The beat drops now!".

for num in range(10, 0, -1):
    print(num)
print("The beat drops now!")