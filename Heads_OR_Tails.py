import random

# Taking input and converting it to int datatype.
while True:
    player1 = input('Player One please make a choice. Press "1" for Heads or press "2" for Tails:  ')
    if player1.isdigit():
        player1 = int(player1)
        if player1 == 1 or player1 == 2:
            break
        else:
            print('Invalid Entry. Please type either "1" or "2" ')
    else:
        print('Please enter a digit')


# generating a random result using Random Module.
result = random.randint(1,2)

# Validating the result and the winner.
if result==1:
    if result==player1:
        print('\n The result is Heads. Player 1 wins!!!')
    else:
        print('The result is Heads. Player 2 wins!!!')

elif result==2:
    if result==player1:
        print('\n The result is Tails. Player 1 wins!!!')
    else:
        print('The result is Tails. Player 2 wins!!!')

