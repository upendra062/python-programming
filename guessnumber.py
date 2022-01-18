# No of guesses number took to finish
# game over

# winning_number = 20
#
# print("This is a number guessing game")
# input_number = int(input("Guess your number between 1 to 100:\n"))
# guess=1
# game_over=False
#
# while not game_over:
#     if(winning_number == input_number):
#         print(f"You Win!, and you guess the number in (guess) time")
#         game_over=True
#     else:
#         if(winning_number > input_number):
#             print("You Guess too low! ")
#             guess += 1
#             input_number =int(input("Guess again"))
#         else:
#             print("You Guess too high! ")
#             guess +=1
#             input_number =int(input("Guess again"))


# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n")
    else:
        print("you won\n")
        print(number_of_guesses,"no. of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")