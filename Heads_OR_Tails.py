import random

# Taking input and converting it to int datatype.
player1 = int(input('Player One please make a choice. Press "1" for Heads or press "2" for Tails:  '))

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

