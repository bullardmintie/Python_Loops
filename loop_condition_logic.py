# Task 1 -- Write a while loop with a condition that will never
# be false (an infinite loop). Inside the loop, print a statement.
# Then, use a break statement to exit the loop after 5 iterations

correct_password = "Momof2boyz"
max_attempts = 3
attempt_count = 0

while attempt_count < max_attempts:
    password = input("Please enter the password: ")
    if password == correct_password:
        print("Welcome!")
        break


# Task 2 -- Modify the infinite loop from Task 1 to include a
# condition that will eventually be true and remove the break
# statement. The loop should terminate naturally once the condition is met.

    else:
        print("Please try again!")
        attempt_count += 1

if attempt_count == max_attempts:
    print("You have reached the maximum attempts. Please try again later.")