from random import choice
scp, scc = 0, 0
while scp <5 and scc < 5:
    comp = choice(['rock', 'paper', 'scissors'])
    player = input("Your hand: ")
    if player in ['rock','paper','scissors']:
        if player == 'rock':
            if comp == 'rock':
                print("A tie.")
            elif comp == 'scissors':
                print("You won.")
                scp += 1
            else:
                print("Computer won.")
                scc += 1
        elif player == 'paper':
            if comp == 'rock':
                print("You won.")
                scp += 1
            elif comp == 'scissors':
                print("Computer won.")
                scc += 1
            else:
                print("It's a tie.")
        else: 
            if comp == 'paper':
                print("You won.")
                scp += 1
            elif comp == 'rock':
                print("Computer won.")
                scc += 1
            else:
                print("It's a tie.")
    else:
        print("Incorrect input.")
if scc == 5: print("Game ended. You lost.")
else: print("Game ended. You won")